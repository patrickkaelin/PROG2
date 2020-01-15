from app import app
from flask import render_template
from flask import request
from app import daten

import csv
import random
import itertools


@app.route("/")
def index():
    """
    Homepage
    Function opens, reads and returns random motivationquotes from a csv-file

    """
    path = "data/motivationquotes.csv"
    file = open(path)
    quotes = csv.reader(file)
    lines = [line for line in quotes]
    merged = list(itertools.chain(*lines))

    random_quote = str(random.choice(merged))

    return render_template("public/index.html", random_quote=random_quote)


@app.route("/newentry/", methods=['GET', 'POST'])
def newentry():
    """
    New Entry Page
    Function saves all the informations from the input-fields in a JSON-file
    Returns a message after submit

    """
    if request.method == 'POST':
        modul_name = request.form['eintrag']
        typ = request.form['typ']
        content = request.form['content']
        deadline = request.form['deadline']


        rueckgabe_string = "You successfully added: " + content + " to your list. Deadline: " + deadline + "!"
        modul_name, typ, content, deadline = daten.eintrag_speichern(modul_name)


        return render_template("public/newentry.html", rueckgabe_string=rueckgabe_string)

    else:
        return render_template("public/newentry.html")


@app.route("/overview")
def overview():
    """
    Overview-Page
    Returns all entries categorically

    """
    eintraege = daten.eintraege_laden()

    return render_template("public/overview.html", eintraege=eintraege)
