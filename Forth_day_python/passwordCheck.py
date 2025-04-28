#!/usr/bin/env python3

# password in variabel (input())
# variabel zum definieren der mindestlänge
# variabel zum definieren enthält zahl
# variabel zum definieren enthält sonderzeichen
# if abfrage  
# output ob password den Anforderungen entspricht

# Abfrage des Passworts im Terminal
password = input("Passwort eingabe: ")

#Deklaration minimum Länge
minLength = 8

#Deklaration bool variable ist Passwort minimum Länger
isPasswordMinLength = False

#Deklaration Ob das Passwort eine Zahl enthält
containsNumber = False

#Deklaration on das Passwort eine Sonderzahl enthält
containsSpecialChar = False

#Prüfung ob das eingegebene Passwort die Mindestlänge hat
if password.__len__() >= minLength:
    isPasswordMinLength = True

# Prüfung ob das eingegebene Passwort eine zahl enthält
for char in password:
    # Die for schleife über einen String um die einzelnen Buchstaben zu erhalten
    if char.isnumeric():
        containsNumber = True
        break

# Prüfung ob das eingegebene Passwort ein Sonderzeichen enthält
for char in password:
    print(char)
    if not char.isalnum():
        containsSpecialChar = True
        break

# Prüfung ob alle Kriterien erfüllt sind

if isPasswordMinLength and containsNumber and containsSpecialChar:
    print("Password is safe")
else:
    print("Password is not safe")


#Konzept "Wie gehe ich mit unbekannten Lösungswegen um"

# Variabel benennung
path = "./"
fileName = "password.txt"

# Öffnen eines Dateistreams
datei = open((path + fileName),"a+")

# In die Datei schreiben
datei.write("\n" + password)

# Ausgabe der Inhalte der Datei
print(datei.read())

# Dateistream schließen
datei.close()

# Andere Form des stream öffnen mit automatisches schließen
with open("beispiel.txt", "a+") as datei:
    datei.write(f"\n{password}")
