from NO_TOUCHIE import JSONmaker

from bottle import route, run, static_file


@route("/")
def index():
    return static_file("index.html", root="")


@route("/main.js")
def main():
    return static_file("main.js", root="")


@route("/grid.csv")  # MAY BE UNNEEDED
def grid():
    return static_file("grid.csv", root="")


@route("/JSONmaker")
def JSONmaker():
    return JSONmaker.csvtoarray()

"""
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