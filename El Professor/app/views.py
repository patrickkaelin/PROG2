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
    return render_template("public/modules.html")