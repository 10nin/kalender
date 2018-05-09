# coding=utf-8

from bottle import Bottle, request, HTTPResponse, static_file, jinja2_template as template
from main import  utils

app = Bottle()


@app.route("/")
def show_root():
    return template("calendar.html", month=6)


@app.route("/list/<request_date:re:\d{6}>")
def show_monthly_schedule(request_date=''):
    """List of 'request_date' month schedule.
    :arg request_date: request date information of YYYYMM formatted string.
    :return request date schedule page."""

    if not utils.valid_date(request_date):
        # if date invalid then return bad request error.
        return HTTPResponse(status=400, body='Request date was invalid. it accept between 201801 and 201912.')

    year, month = utils.split_request_date(request_date)
    days = utils.generate_days(year, month)

    # generate request_date days
    return template("calendar.html", month=month, days=days)


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


if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True, reloader=True)
