# Wir wollen ein Script schreiben
# Dieses Script soll mit APT git installieren
# Die Funktion um Git zu installieren, soll ein Methode sein
# Die Funktion soll einen Parameter entgegen nehmen, welches mit einem 
# If statement das Programm welches installiert werden soll Wählt

import os
import time

def getSoftwareNumber():
    try:
        return int(input(f"""Please choose a number:
1. Git
2. Zip
"""))
    except:
        print("Please choose a number only!")
#        print("Start sleep")
#        time.sleep(5)
#        print("End sleep")
        getSoftwareNumber()

def convertNumber(number):

    name= ""

    if number == 1:
        name = "Git"
    if number == 2:
        name = "zip"
    
    installSoftware(name)



def installSoftware(name):

    if name == "Git":
        os.system("sudo apt install git -y")
    if name == "zip":
        os.system("sudo apt install zip -y")
    
    print(f"{name} wurde jetzt installiert")
        
#def chooseSoftware(number):




convertNumber(getSoftwareNumber())
