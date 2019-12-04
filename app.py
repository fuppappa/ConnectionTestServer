from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)


@app.route("/iframe")
def iframe():

    return render_template("iframe.html")


@app.route("/redirect")
def redirecto():
    return redirect(url_for("html_other_css"))


@app.route("/otherjs")
def html_other_js():
    return render_template("html_other_js.html")


@app.route("/injs")
def html_in_js():
    return render_template("html_in_js.html")


@app.route("/othercss")
def html_other_css():
    return render_template("html_other_css.html")


@app.route("/incss")
def html_in_css():
    return render_template("html_in_css.html")


@app.route("/index")
@app.route('/')
def index():
    htmlincss = url_for("html_in_css")
    htmlothercss = url_for("html_other_css")
    htmlinjs = url_for("html_in_js")
    htmlotherjs = url_for("html_other_js")

    return render_template("index.html")


if __name__ == '__main__':
    app.debug = True
    app.testing = False
    app.run(host="0.0.0.0", port="5555")
