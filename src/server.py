import bottle
"""
import process
import process2
import process3
"""

from bottle import route, run, static_file, request


@route("/")
def index():
    return static_file("index.html", root="")


@route("/main.js")
def main():
    return static_file("main.js", root="")


@route("/grid.csv")
def grid():
    return static_file("grid.csv", root="")


@route("/JSONmaker")
def JSONmaker():
    return static_file("JSONmaker", root="")

"""
@route("/process")
def processing():
    return process.reformat(10, 10)

@route("/process2")
def processing2():
    sq = request.query["sq"]
    return process2.dotheneedful(sq)

@route("/process3")
def processing3():
    q = request.query["gamename"]
    return process3.gib(q)
"""

run(host='0.0.0.0', port=8080, debug=True)