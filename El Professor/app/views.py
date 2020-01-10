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


@app.route("/newentry/", methods=['GET', 'POST'])
def newentry():

    # Senden des neuen Eintrages, Form --> newentry.html Zeile 29
    if request.method == 'POST':
        modul_name = request.form['eintrag']
        typ = request.form['typ']
        content = request.form['content']
        deadline = request.form['deadline']

        rueckgabe_string = "You successfully added: " + content + " to your list. Deadline: " + deadline + "!"
        modul_name, typ, content, deadline = daten.eintrag_speichern(modul_name)


        # return rueckgabe_string --> zeigt String nach Eingabe an

        return render_template("public/newentry.html", rueckgabe_string=rueckgabe_string)

    else:
        return render_template("public/newentry.html")


@app.route("/overview")
def overview():
    # ab hier probieritis von demos:
    eintraege = daten.eintraege_laden()

    """
    # braucht es nicht hier, solange es im HTML steht
    eintraege_liste = ""
    for key, value in eintraege.items():
        zeile = str(key) + ": " + value + "<br>"
        eintraege_liste += zeile
    """

    return render_template("public/overview.html", eintraege=eintraege)
