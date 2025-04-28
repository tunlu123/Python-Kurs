from typing import overload

def iAmADefinition():
    print("Ich bin eine tolle Funktion")

def iAmAnotherDefinition(parameter):
    if type(parameter) == str:
        print("Line 8: " + parameter)
    else:
        print("Line 10: " + str(parameter))

iAmAnotherDefinition(23)
iAmAnotherDefinition("Stephan")

# Keywort name(parameter):
    # Logik

def addition(num1 : int , num2 :int):
    print(num1)
    print(num2)
    if type(num1) == int and type(num2) == int:
        print(num1 + num2)
    else:
        print(int(num1) + int(num2))

x = input("die erste Zahl bitte: ")
y = input("die zweite Zahl bitte: ")


addition(x,y)

# Deklariere eine Funktion
# nehme eine Eingabe entgegen
# prüfe ob ein übergebener Wert ein float ist
# gebe in das Terminal zurück, wenn der wert ein float ist
# wenn der wert kein float ist, gebe zurück dass der wert kein float ist und den entsprechenden datentyp

def checkIfValueIsFloat(zahl):
   # zahl = input("Gebe mir eine Zahl") << Macht 0 Sinn
    if type(zahl) == float:
        print("Wert ist ein float")
    else:
        print("Wert ist kein float " + str(type(zahl)))
