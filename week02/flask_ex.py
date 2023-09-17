from flask import Flask

app = Flask(__name__)

@app.route("/")
def first_page():
    return "<a href='/'>첫페이지</a> <a href='/hello'>hello</a><p>첫페이지 입니다.</p>"


@app.route("/hello")
def hello_world():


    return "<a href='/'>첫페이지</a> <a href='/hello'>hello</a><p>Hello, World!</p>"


@app.route("/gugu/<dan>")
def gugudan(dan):
    dan = int(dan)
    resp = ""
    resp += "<html>\n"
    resp += '<meta charset="utf-8">\n'
    resp += "<body>\n"
    resp += f"<h2>구구단 {dan}단</h2>\n"
    resp += "<div>\n"

    for i in range(1, 10):
        resp += f"{dan:2d} * {i:2d} = {dan * i:3d}<br>\n"
    resp += "</div>\n"
    resp += "</body>\n"
    resp += "</html>\n"


    return resp

app.run(host="0.0.0.0")