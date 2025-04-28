# Ein und Ausgabe

import math

#name = input("Wie heißt du? ")
# print("Hallo " + name)

#print(f"Hallo {name}")

#value = input("Wie alt bist du? ")
# print(type(value))

# value2 = input("nenne mit eine Zahl ")
# value3 = input("nenne mir eine weitere Zahl ")

def addition(number, number2):
    return int(number) + int(number2)

# print(addition(value2, value3))
# print(addition(9,19))
# print(addition("29", 10))

def subtraktion(number, *args):
    oldNumber = number

    for value in args:
      oldNumber = oldNumber + value

#    print(oldNumber)



# subtraktion(2,2,1,6,5,4,8)
# subtraktion(2,2,1,2)
    
int() # Umwandlung in Integer
float() # Umwandlung in float
str() # Umwandlung in string

fl = 2.6 

print(math.ceil(fl)) # Mathe Klasse IMMER hoch runden

print(math.floor(fl)) # Mathe Klasse IMMER runter runden

print(round(fl)) # Richtig runden Methode
 
print(math.pi) # Festgelegte Pi wert

print(int(fl)) # Von Float direk auf Int umgewandelt mit Nachkommastellenverlust

print(float(2))

print(type(str(35)))
if type("35") == int:
  print("35 ist integer")
else:
  #print("35 ist not a integer, it is a: " + str(type("35")))
  convertedNumber = int("35")



#print(35 + "35")
