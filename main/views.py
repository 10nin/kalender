# coding=utf-8

import re
from bottle import Bottle, request, HTTPResponse, static_file, jinja2_template as template

app = Bottle()


@app.routes('/list/<request_date:re:\d{6}')
def show_monthly_schedule(request_date=''):
    """List of 'requestdate' month schedule.
    :arg request_date: request date information of YYYYMM formatted string.
    :return request date schedule page."""
    pass


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
