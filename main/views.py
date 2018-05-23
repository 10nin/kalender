# coding=utf-8

from bottle import Bottle, run, redirect, request, HTTPResponse, static_file, jinja2_template as template
from bottle_log import LoggingPlugin
from beaker.middleware import SessionMiddleware
from main import utils, controllers

session_ops = {
    'session.type': 'cookie',
    'session.cookie_expires': True,
    'session.auto': True,
    'session.key': utils.get_unique_str(128),
    'session.timeout': '600',
}
app = Bottle()
app.install(LoggingPlugin(app.config))
apps = SessionMiddleware(app, session_ops)


@app.route("/")
def show_root():
    return template("login.html", title="Kalendar - ログイン", message='')


@app.route("/", method="POST")
def login_proc():
    group_code = request.forms.group_code
    password = request.forms.passwd
    c = controllers.Controller("../setup.cfg")
    if c.is_login_success(groupcode=group_code,passwd=password):

        redirect("/menu")
    else:
        return template("login.html", title="Kalendar - ログイン", message='グループIDかパスワードが間違っています')


@app.route("/menu")
def show_main_menu():
    return template("menu.html", title="Kalendar - メインメニュー")


@app.route("/list")
@app.route("/list/<request_date:re:\d{6}>")
def show_monthly_schedule(request_date=''):
    """List of 'request_date' month schedule.
    :arg request_date: request date information of YYYYMM formatted string.
    :return request date schedule page."""
    if len(request_date) == 0:
        request_date = utils.get_current_date()
        redirect("/list/" + request_date)

    if not utils.valid_date(request_date):
        # if date invalid then return bad request error.
        # TODO: change error message
        return HTTPResponse(status=400, body='Request date was invalid.')

    year, month = utils.split_request_date(request_date)
    days = utils.generate_days(year, month)
    prev_month, next_month = utils.get_prev_and_next_month(year, month)

    title = f"Kalendar - {year}年{month}月の予定"
    # generate request_date days
    # TODO: implement show active groups.
    return template("calendar.html", title=title, year=year, prev_month=prev_month, month=month, next_month=next_month, days=days)


@app.route('/schedule')
@app.route('/schedule/<request_date:re:\d{6}>')
def show_schedule_input(request_date=''):
    if len(request_date) == 0:
        request_date = utils.get_current_date()
        redirect("/schedule/" + request_date)

    if not utils.valid_date(request_date):
        # if date invalid then return bad request error.
        return HTTPResponse(status=400, body='Request date was invalid.')
    year, month = utils.split_request_date(request_date)

    title = f"Kalendar - {year}年{month}月の活動予定入力"
    return template("schedule_input.html", title=title, year=year, month=month)

# TODO: implement help page
# ---- Static Routes ----
@app.route("/static/css/<file_path:re:.*\.css>")
def css(file_path):
    """Route for style sheet"""
    return static_file(file_path, root="static/css")


@app.route("/static/img/<file_path:re:.*\.(jpg|png|gif|ico|svg)>")
def img(file_path):
    """Route for image files."""
    return static_file(file_path, root="static/img")


@app.route("/static/js/<file_path:re:.*\.js>")
def js(file_path):
    """Route for javascripts."""
    return static_file(file_path, root="static/js")


# session utility functions
def set_session_val(k, v):
    _s = request.environ["beaker.session"]
    _s[k] = v
    _s.save()

def get_session_val(k):
    _s = request.environ['beaker.session']
    return _s[k] if k in _s else ''

def delete_session_val(k):
    _s = request.environ['beaker.session']
    if k in _s:
        del _s[k]

if __name__ == '__main__':
    run(app=apps, host="localhost", port=8080, debug=True, reloader=True)
