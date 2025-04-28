# 📦 Klasse Programm speichert Name & Version
class Programm:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def __repr__(self):
        return f"{self.name} (Version {self.version})"
