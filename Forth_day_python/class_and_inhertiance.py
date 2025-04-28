class Human:
    def __init__(self, age, name, legs):
        self.name = name
        self.age = age
        self.legs = legs

    def walk(self, distance):
        print(f"I walked {distance}m")
    
class Student(Human):
    def __init__(self, topics, interrests, age, name, legs):
        self.topics = topics
        self.interrests = interrests
        super().__init__(age, name, legs)

    def walk(self, distance):
        return super().walk(distance)

    

x = Student(["c#", "python", "Ansible"], ["Web-Developement", "Dev-Ops"], 46, "Mathias", True,)

x.walk(23)
print(x.interrests)
print(x.age)


class Tier:
    def sprich(self):
        print("Das Tier macht ein Geräusch")
 
# Abgeleitete Klasse 1
class Hund(Tier):
    def sprich(self):
        print("Der Hund bellt: Wuff Wuff!")
 
# Abgeleitete Klasse 2
class Katze(Tier):
    def sprich(self):
        print("Die Katze miaut: Miau Miau!")
 
# Hauptprogramm
tier = Tier()
tier.sprich()  # Gibt aus: Das Tier macht ein Geräusch
 
hund = Hund()
hund.sprich()  # Gibt aus: Der Hund bellt: Wuff Wuff!
 
katze = Katze()
katze.sprich()  # Gibt aus: Die Katze miaut: Miau Miau!
