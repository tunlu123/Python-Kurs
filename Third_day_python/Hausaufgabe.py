# Erstellt eine Liste mit Städtenamen
staedte = ["Berlin", "München", "Hamburg", "Köln", "Frankfurt", "Stuttgart", "Düsseldorf", "Dortmund", "Essen", "Leipzig"]

# Sortiert diese Liste
staedte.sort()

# Checkt mit contains ob 2 Städte enthalten sind
stadt1 = "Berlin"
stadt2 = "München"

if stadt1 in staedte and stadt2 in staedte:
    print(f"Die Städte {stadt1} und {stadt2} sind in der Liste enthalten.")
else:
    print(f"Die Städte {stadt1} und {stadt2} sind nicht in der Liste enthalten.")

# Gibt diese Städte ins Terminal aus
print("Die sortierte Liste der Städte:")
for stadt in staedte:
    print(stadt)

# Macht ein Tupel mit Vornamen
vornamen = ("Max", "Anna", "Lukas", "Sophia", "Leon")

# Macht ein Tupel mit Nachnamen
nachnamen = ("Müller", "Schmidt", "Schneider", "Fischer", "Weber")

# Verbindet Vor- und Nachname für die Email mit einem Punkt (join Methode)
emails = []
for vorname, nachname in zip(vornamen, nachnamen):
    email = ".".join([vorname.lower(), nachname.lower()]) + "@skyered.de"
    emails.append(email)

# Checkt mit contains ob die Emails bestimmte Namen enthalten
name1 = "max.müller"
name2 = "anna.schmidt"

if name1 in emails and name2 in emails:
    print(f"Die Emails {name1} und {name2} sind in der Liste enthalten.")
else:
    print(f"Die Emails {name1} und {name2} sind nicht in der Liste enthalten.")

# Gibt die Emails ins Terminal aus
print("\nDie Emails:")
for email in emails:
    print(email)