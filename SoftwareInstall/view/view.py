from controller import installController
from model import programmCollection

indexDictionary = {}
"""IndexDictionary ist ein Dictionary welches im Programmablauf dynamisch generiert wird"""

nameList : str = ""
"""Die nameList ist einer konstruierter String im Schema 'Zahl +'"""

def Start():
    """Diese Methode stößt den Installationsablauf an"""
    initializeInstallation()

def generateIndexDictionary():
    """Diese Methode generiert das indexDictionary dynamisch
    Dafür nimmt es sich das komplette Dictionary aus der programmCollection programms.
    Es weisst dem indexDictionary den Key als integer zu und das entsprechende Programm als value
    """
    index : int = 0

    for key in programmCollection.programms:
        nameList += ( str(index) + f" {programmCollection.programms[key].name}\n")
        indexDictionary[index] = programmCollection.programms[key].name
        index += 1
     

def getProgramm(choice):
    """Diese Methode sucht das entprechende Programm aus dem Dictionary in der programmCollection in der Variabel programms raus.
    Dafür wandeln wir den erhaltene Zah als String zu einem Integer um,
    Mit diesem Integer als key suchen wir dann im indexDictionary, das Programm als value heraus.
    Mit dem return statement geben wir anschließend das Programm zurück.
    """

#   choiceList = []
#   choiceList.append(indexList[int(choicesNumber)])
#   installController.installSoftware(choiceList)

    choiceAsInt = int(choice) 
    indexKey = indexDictionary[choiceAsInt]
    return programmCollection.programms[indexKey]


def initializeInstallation():
    """Hier initialisieren wir die Installation. Wir geben die nameList in Kombination eines vorläufigen Strings ins Terminal aus. 
     Wir erwarten dabei eine Eingabe und speichern diese in die Variabel choices.
     Diese Variabel wandeln wir dann entsprechend mit .split(',') und tupel() in ein tupel um. 
     Dabei werden die Werte durch das ',' getrennt und in das Tupel eingetragen. 
     Ebenfalls werden dabei Leerzeichen vor und hinter den Zahlen mit der Methode .strip() entfernt.

     Nach dem umwandeln des Tupel, können wir mit einer For Schleife drüber gehen und unsere Auswahl entsprechend weiter geben.
     in der Variabel Programm speichern wir das Ergebniss von getProgramm(...). Get Programm erhält als Parameter die derzeitige 
     Nummer aus dem Tupel.
     mit programm.InstallProgramm() rufen wir auf der entsprechenden Klasse die Methode installProgramm() auf.

     Das ganze geschieht in einem try - except block. Das bedeutet, sollte der Code im try block einen Fehler haben, so rutscht er 
     automatisch in dem except block. 

     Im except block wird dann den Fehler ausgegeben, sowie dass man eine nummer seperiert mit einem Komma.
     Im Anschluss wird die Methode noch einmal aufgerufen. Dies nennt man Rekursive Methodcall.  
     """
    choices = ""
    choicesTuple = ()

    generateIndexDictionary()

    try:
        choices = input(f"""Please choose numbers seperated with , :
{nameList}
""")

        choicesTuple = tuple(choices.strip().split(","))  

        for choicesNumber in choicesTuple:
            programm = getProgramm(choicesNumber)
            programm.installProgramm()

            print("Software modules successfully installed.")

    except Exception as e:
        print(e)
        print("Please choose a number only and seperat it with a , !")
        initializeInstallation()


