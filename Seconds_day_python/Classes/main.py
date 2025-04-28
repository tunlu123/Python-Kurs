class student:
    
    def __init__(self, name, age, interessen):
        self.name = name
        self.age = age
        self.interessen = interessen

Muhammed = student("Muhammed", 26, ["Kochen", "Fußball spielen"])
Arthur = student("Arthur", 24, ["Programmieren", "Computer zocke"])
Hassibulah = student("Hassibulah", 29, ["Bahn fahren", "Basteln"])

teacherStudends = {"Emre" : {}, "Stephan" : {Muhammed, Arthur, Hassibulah}}

for actualStudent in teacherStudends["Stephan"]:
    print(actualStudent.name)
    print(actualStudent.interessen)
    print(actualStudent.age)

