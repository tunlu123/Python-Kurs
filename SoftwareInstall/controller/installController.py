import os # importiere globales Paket os (von Python)
from model import programmCollection # importiere von Ordner "x" die Scriptdatei "y" 




def installSoftware(keyListe): 
        """Diese Definition nimmt den Parameter keyListe an
         In dieser For-Schleife gehen wir die keyListe durch und erhalten pro Schritt einen Key. 
         Diese Variabel Key deklarieren wir nach for. 
         In der For Schleife greifen wir auf das OS Modul zu, in diesem Modul OS greifen wir auf die Methode system() zu.
         Der Methode System übergeben wir als Parameter einen string, welcher mit generischen string literals befüllt wird. 
         Am Ende geben wir den Programmnamen in der Console aus mit dem Hinweis dass es installiert wurde.
         """

        for key in keyListe:
                os.system(f"choco upgrade {programmCollection.programms[key].name}  --version={programmCollection.programms[key].version} --confirm" )
    
                print(f"{programmCollection.programms[key].name} wurde jetzt installiert")


