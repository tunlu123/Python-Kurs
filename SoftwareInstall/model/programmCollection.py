from model import programm

programms = {"git" : programm.programm("git", "2.47.1"), 
            "7zip" : programm.programm("7zip", "24.9.0"),  
            "apache2" : programm.programm("apache-httpd", "2.4.55")
            }
"""Die Variabel programms ist vom Datentyp Dictionary. Als Key wird der String (name des Programms) verwendet und als Value erstellen
wir ein neues Object 'Klasse' vom Typ programm. Wir übergeben dem Constructor den Namen des Programms als string sowie die Versionsnummer 
als String """
