#!/usr/bin/env python3

# Dies ist ein einzeiliger Kommentar

"""
Dies ist ein Multline Comment
Diesen Kommentag kann ich über mehrere Zeilen schreiben
"""

'''
Auch dies ist ein Mulit line comment
Auch dies geht über mehrere Zeilen!
'''

# Variabeln und grundlegende Datentypen
x = 2  #(integer)
y = 3.5 #(float)
name = "Stephan" # (string)
isCoder = True #(boolean)

minCpuCount = 4
maxCpuCount = 8

# if statements


if x > 2:
    print("x is bigger")

if x == 2:
    print("x is equal to 2")
elif x < 2:
    print("is is smaler then 2")
else: 
    print("x is bigger then 2")

#Import sollte immer am Anfang des scripts stehen
import os
import cpuinfo
import erweiterte_grundlagen

cpuCount = os.cpu_count()

# String concatination mit str() (Umwandlung des Int in ein String)
print("You have: " + str(os.cpu_count()) + " cores.")

# String literal mit format print (das f in der klammer und direkt angegebener Variabel)
print(f'You have: {cpuCount} cores.')

cpuinfo = cpuinfo.get_cpu_info()

# If, else, elseif mit greater euqals, lower equals und mit wörtern is und is not

if cpuinfo["count"] >= maxCpuCount:
    print("Your CPU is big")
elif cpuinfo["count"] <= minCpuCount:
    print("Your cpu is small")
else:
    print("Your CPU is okay :D")

if cpuinfo["count"] is maxCpuCount:
    print("Your Cpu ist great")

if cpuinfo["count"] is not maxCpuCount:
    print("Your Cpu ist bad")

# Erweiterte Datentypen

names = ["Stephan", "Muhammed", "Cihat", "Matthias"] # Datentyp: Listen

print(names.sort(reverse=True))

ages = (2, 5, 8, 14, 263) # Datentyp: Tupel

marken = {"Ford", "BMW", "VW", "Opel"} # Datentyp: Set

dictionary = { "autoMarken": marken, "alter": ages, "namen": names } # Dictionary (Key:Value)
#newDictionary = {"Namen" : []}

#newDictionary["Namen"].ad

print(names[2])
print(ages[1])
print(marken)

print(marken.__contains__("BMW"))

print(dictionary["namen"])

print(dictionary.__len__())

# For Schleife

for name in names:
    print(name)

for key in dictionary:
    for value in dictionary[key]:
        print(value)

# Slicen von String

stringToSlice = "Hello World!"

print(stringToSlice[1:4])
filename = "Log-2025-01-19.txt"
print(filename[4:14])

dates = ["2025-01-17","2025-01-18","2025-01-19","2025-01-20","2025-01-21","2025-01-22"]

print(dates.__contains__(filename[4:14]))

# While Schleife

i = 0

while i < 5:
    print(i)
    i+=1

# Nutzung eines importierten Scripts

erweiterte_grundlagen.addition(2,3)


json = { "Name": "Cihat", 
        "Age": 24, 
        "Hobbies" : ["Cooking", "talking", "learning"] 
        }

json2 = { "Name": "Talha", 
         "Age": 27, 
         "Hobbies" : ["playing", "music", "cars"] 
         }

Students = {"Studend" : { "Cihat": json, "Talha": json2 } }

Students["Studend"]

#for studend in Students["Studend"]:
#    for value in Students["Studend"][studend]:
#        for field in Students["Studend"][studend][value]:
#            print(field)

print(Students["Studend"]["Cihat"]["Age"])
