import os


class programm:
    """Die Klasse Programm ist eine Datenstruktur mit einer Definition. Diese Klasse wird automatisch ebenfalls zu einem Datentyp"""
    def __init__(self, name, version):
        """Def __init__ wird auch als Constructor bezeichnet"""
        self.name = name
        self.version = version

    def installProgramm(self):
        """In der For Schleife greifen wir auf das OS Modul zu, in diesem Modul OS greifen wir auf die Methode system() zu.
         Der Methode System übergeben wir als Parameter einen string, welcher mit generischen string literals befüllt wird. """
        os.system(f"choco upgrade {self.name}  --version={self.version} --y")
