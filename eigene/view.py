import sys
import os

# Stellt sicher, dass das Modul gefunden wird
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from programmCollection import programms  # Importiert die Liste der Programme
import installController  # Importiert die Installationsfunktion

def getSoftwareNumber():
    choices = ""
    choicesTuple = ()
    indexList = {}
    choiceList = []

    nameList = ""
    index = 0

    # Erstellt die Programmliste mit Indexen
    for key in programms:
        nameList += f"{index}. {programms[key].name}\n"
        indexList[index] = programms[key].name  # Speichert die Zuordnung von Index zu Programmnamen
        index += 1

    try:
        # Benutzer wählt Programme per Zahl
        choices = input(f"""Please choose numbers separated with , :
{nameList}""")

        # Konvertiere die Eingabe in eine Tupelliste
        choicesTuple = tuple(choices.strip().split(","))

        # For-Schleife zur Umwandlung der Eingaben in Programmnamen
        for choiceNumber in choicesTuple:
            if choiceNumber.isdigit():  # Prüft, ob es eine Zahl ist
                choiceList.append(indexList[int(choiceNumber)])  # Holt den passenden Programmnamen

        # Starte die Installation für alle gewählten Programme
        installController.installSoftware(choiceList)

        print("✅ Software modules successfully installed.")
    except:
        print("❌ Fehler! Bitte gib nur Zahlen ein und trenne sie mit Komma (,)!")  
        getSoftwareNumber()  # Wiederhole die Eingabe

# 🏁 Startet das Programm
if __name__ == "__main__":
    getSoftwareNumber()
