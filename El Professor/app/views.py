from app import app
from flask import render_template
from flask import request
from app import daten


@app.route("/")
def index():
    return render_template("public/index.html")


@app.route("/modules")
def modules():

    # Dictionary mit den Modulinformation
    modulinformation = {
        "MIKR": "schriftlich",
        "ENG": "elektronisch",
        "INMA": "projektarbeit (100%)"
    }

    return render_template("public/modules.html", modulinformation=modulinformation)


@app.route("/newentry", methods=['GET', 'POST'])
def newentry():

    # Senden des neuen Eintrages, Form --> newentry.html Zeile 29
    if request.method == 'POST':
        new_entry = request.form['eintrag']
        rueckgabe_string = "Your new Entry: " + new_entry + "!"
        # ab hier probieritis von demos:
        # UnboundLocalError: local variable 'eintrag' referenced before assignment
        zeitpunkt, eintrag = daten.eintrag_speichern(eintrag)

        return rueckgabe_string

    return render_template("public/newentry.html")


@app.route("/overview")
def overview():
    # ab hier probieritis von demos:
    eintraege = daten.eintraege_laden()

    eintraege_liste = ""
    for key, value in eintraege.items():
        zeile = str(key) + ": " + value + "<br>"
        eintraege_liste += zeile

    return eintraege_liste

    return render_template("public/overview.html")
