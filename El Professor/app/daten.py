from datetime import datetime
import json
from flask import request
# von persistente daten demos


def speichern(datei, key, value1, value2, value3, value4): #hier geändert values hinzugefügt
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[str(key)] = value1, value2, value3, value4 #hier geändert values hinzugefügt

    print(datei_inhalt)

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file)


def eintrag_speichern(eintrag):
    datei_name = "eintraege.json"
    zeitpunkt = datetime.now()
    modul_name = request.form['eintrag']
    typ = request.form['typ']
    content = request.form['content']
    deadline = request.form['deadline']
    speichern(datei_name, zeitpunkt, eintrag, typ, content, deadline) # 3 hinzugefügt
    return eintrag, typ, content, deadline # zeitpunkt entfertn, 3 hinzugefügt


def eintraege_laden():
    datei_name = "eintraege.json"

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt
