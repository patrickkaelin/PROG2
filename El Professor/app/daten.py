from datetime import datetime
import json
from flask import request


def speichern(datei, key, value1, value2, value3, value4):
    """
    opens JSON-file
    and saves all input-values in it

    """
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[str(key)] = value1, value2, value3, value4

    print(datei_inhalt)

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file)


def eintrag_speichern(eintrag):
    """
    assigns inputs to a variable
    returns all the information

    """
    datei_name = "eintraege.json"
    zeitpunkt = datetime.now()
    modul_name = request.form['eintrag']
    typ = request.form['typ']
    content = request.form['content']
    deadline = request.form['deadline']
    speichern(datei_name, zeitpunkt, eintrag, typ, content, deadline)
    return eintrag, typ, content, deadline


def eintraege_laden():
    """
    loads JSON-file if there's one
    otherwise creates a new, empty JSON-file

    """
    datei_name = "eintraege.json"

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt
