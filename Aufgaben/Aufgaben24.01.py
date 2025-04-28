# Erstelle 8 Variabeln mit je einem anderen Datentyp
# Benenne die Datentypen der Variabeln
# Nehme einen Input entgegen und speichere sie in die Variabel ab
# Checke den Typ und gebe den Typ der Inputvariabel in der console aus
# Schreibe eine Methode
# Nehme in der Methode 2 parameter entgegen.
# Schreibe eine beliebige funktionierende Logik mit folgendem Inhalt:
# - es muss ein if statement drin sein
# - es muss eine for loop enthalten sein
# - es muss sein logischer operator enthalten sein
# führe die Methode aus


f = 20 # integer
x = 20.5 # float
m = "monday" # string
t = (1,2,3)  # tupel
l = [1,2,3] # list
d = {"türkei": "Ankara", "Deutschland" : "Berlin"} # dictionary
b = True # boolean
s = {1,2,3} # set


#zahl = input("Geben Sie eine Zahl ein: ")

#print(type(zahl))

#if type(zahl) == int and type(zahl) == float and zahl >= 5 and zahl <= 10:
#    print("True")

dryFood = ["DryMeat", "Corny", "Cookies", "knoppers"]

def bestellungsChecker(einkaufsliste, lebensmittel = dryFood):
    if type(einkaufsliste) == list or type(einkaufsliste) == tuple or type(einkaufsliste) == set:
        for essen in einkaufsliste:
            if essen == lebensmittel:
                print("Line 37: true")
                continue
            
            
            print(f"Line 40: {essen} is not {lebensmittel}")





bestellung = ["wasser", "salz", "ei", "mehl", "tee"]
bestellungsChecker(bestellung, "wasser")
bestellungsChecker(dryFood, "Corny")



#for zahl2 in range(20):
#    if zahl2 == 10:
#        print("Continue")
        
    
#    print(zahl2)



vac = ["Asta Zenica", "Sputnik", "Moderna", "Aspirin", "Ibuprophene", "Comirnaty"]
headacheMedicine = ["Aspirin", "Ibuprophene"]

#for medicine in vac:
#    if headacheMedicine.__contains__(medicine):
 #       print(f"{medicine} is a headache medicine and not efficient against corona")
#        continue
    
#    print(f"{medicine} is efficent against corona")


#i = 0
#while i <= (vac.__len__() - 1) :
#    if headacheMedicine.__contains__(vac[i]):
#        print(f"{vac[i]} is a headache medicine and not efficient against corona")
#        continue
#        i+=1
    
#    print(f"{vac[i]} is efficent against corona")
#    i+=1
