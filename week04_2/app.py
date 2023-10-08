from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def first_page():
    return render_template("index.html")


@app.route("/about")
def about_me():
    return render_template("about.html")


@app.route("/about")
def about_me_func():
    return render_template("about.html")



@app.route("/blog")
def blog_list_func():
    return render_template("blog_list.html")

@app.route("/blog")
def blog_list():
    datasets=[
        {"title": "제목1", "content": "내용1"},
        {"title": "제목2", "content": "내용2"},
        {"title": "제목3", "content": "내용3"},
        {"title": "제목4", "content": "내용4"}
    ]
    return render_template("blog_list.html", posts=datasets)



app.run(host="0.0.0.0", debug=True)