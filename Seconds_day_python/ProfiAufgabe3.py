# Produkte im Lager als Liste von Dictionaries
produkte = []

# Funktion, um ein Produkt hinzuzufügen
def produkt_hinzufuegen(produkt_name, menge, preis):
    neues_produkt = {"name": produkt_name, "menge": menge, "preis": preis}
    produkte.append(neues_produkt)

# Funktion, um ein Produkt zu entfernen
def produkt_entfernen(produkt_name):
    for produkt in produkte:
        if produkt["name"] == produkt_name:
            produkte.remove(produkt)
            return True
    return False

# Funktion, um den Lagerbestand anzuzeigen
def bestand_anzeigen():
    for produkt in produkte:
        print(f"Produkt: {produkt['name']}, Menge: {produkt['menge']}, Preis: {produkt['preis']}")

# Funktion, um eine Bestellung zu erstellen
def bestellung_erstellen(artikel_liste):
    gesamtpreis = 0
    for artikel in artikel_liste:
        name, menge = artikel
        for produkt in produkte:
            if produkt["name"] == name:
                if produkt["menge"] >= menge:
                    gesamtpreis += menge * produkt["preis"]
                    produkt["menge"] -= menge
                else:
                    print(f"Nicht genug Bestand für {name}. Verfügbar: {produkt['menge']}")
    return gesamtpreis

# Hauptprogramm
# Produkte hinzufügen
produkt_hinzufuegen("Laptop", 10, 1200)
produkt_hinzufuegen("Maus", 50, 25)
produkt_hinzufuegen("Tastatur", 20, 45)

# Lagerbestand anzeigen
print("Lagerbestand:")
bestand_anzeigen()

# Bestellung erstellen
artikel_liste = [("Laptop", 2), ("Maus", 5), ("Tastatur", 1)]
gesamtpreis = bestellung_erstellen(artikel_liste)
print(f"Gesamtpreis der Bestellung: {gesamtpreis}")

# Aktualisierten Lagerbestand anzeigen
print("\nAktualisierter Lagerbestand: ")
bestand_anzeigen()

dictionary = {"Key": "Value"}

print( f"Hallo welt {dictionary['Key']}")
