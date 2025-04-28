import os
from programmCollection import programms

# 📦 Funktion zur Installation eines Programms mit Versionsauswahl
def installSoftware(keyListe):
    for key in keyListe:
        if key in programms:
            programm = programms[key]
            print(f"⚙️ Installiere {programm.name} (Version {programm.version})...")
            
            # Nutzt Chocolatey für die Installation (Windows) oder APT (Linux)
            os.system(f"choco upgrade {programm.name} --version={programm.version} -y")

            print(f"✅ {programm.name} (Version {programm.version}) wurde erfolgreich installiert!")
        else:
            print(f"❌ Programm {key} nicht gefunden.")
