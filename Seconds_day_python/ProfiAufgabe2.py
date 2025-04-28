# Bibliothek importieren
import math
import random

# Funktion zur Berechnung der Quadratzahlen
def quadratzahlen(liste):
    ergebnis = []
    for zahl in liste:
        ergebnis.append(zahl ** 2)
    return ergebnis

# Funktion zur Verarbeitung eines Wörterbuchs
def bearbeite_daten(daten):
    for key, value in daten.items():
        if value > 10:
            print(f"Der Wert {value} ist größer als 10.")
        else:
            print(f"Der Wert {value} ist kleiner oder gleich 10.")

# Hauptprogramm
werte = [5, 10, 15, 20]
ergebnisse = quadratzahlen(werte)
print("Quadratzahlen:", ergebnisse)

# Wörterbuch mit Daten
daten = {"A": 5, "B": 15, "C": 25}
bearbeite_daten(daten)

# Zusatz: Implementiere eine Funktion, die prüft, ob eine Eingabezahl eine Primzahl ist.
def ist_primzahl(zahl):
    if zahl < 2:
        return False
    for i in range(2, zahl // 2):
        if zahl % i == 0:
            return False
    return True

# Test der Primzahlfunktion
zahl = 19
if ist_primzahl(zahl):
    print(f"{zahl} ist eine Primzahl.")
else:
    print(f"{zahl} ist keine Primzahl.")
