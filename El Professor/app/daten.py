from datetime import datetime
import json
# von persistente daten demos


def speichern(datei, key, value):
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[str(key)] = value

    print(datei_inhalt)

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file)


def eintrag_speichern(eintrag):
    datei_name = "eintraege.json"
    zeitpunkt = datetime.now()
    speichern(datei_name, zeitpunkt, eintrag)
    return zeitpunkt, eintrag


def eintraege_laden():
    datei_name = "eintraege.json"

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt
