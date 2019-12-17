from app import app
from flask import render_template


@app.route("/")
def index():
    return render_template("public/index.html")


@app.route("/overview")
def overview():
    return render_template("public/overview.html")


@app.route("/modules")
def modules():

    # Dictionary mit den Modulinformation
    modulinformation = {
        "MIKR": "schriftlich",
        "ENG": "elektronisch",
        "INMA": "projektarbeit (100%)"
    }

    return render_template("public/modules.html", modulinformation=modulinformation)


@app.route("/newentry")
def newentry():
    return render_template("public/newentry.html")
