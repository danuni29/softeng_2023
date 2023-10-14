from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def first_page():
    return render_template("index.html")


@app.route("/about")
def about_me():
    return render_template("about_me.html")


@app.route("/about")
def about_me_func():
    return render_template("about_me.html")



@app.route("/blog")
def blog_list_func():
    return render_template("blog_list.html")



app.run(host="0.0.0.0", debug=True)