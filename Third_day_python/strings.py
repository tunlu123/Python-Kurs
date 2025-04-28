string = "Ich bin ein Teststring"

vorname = "Stephan"
nachname = "Löcher"
domain = "skyered.de"

sliced = string[5:-5]
length = len(string)

#email = vorname + "." + nachname + "@" + domain

email = f"{vorname}.{nachname}@{domain}"

#email = str.join([vorname,".",nachname,"@",domain])

base = "etc"
var = "var"
filepath = "file.txt"

complete = "/".join([base,var,filepath])

print(f"Line 22: {complete}")

print(f"Line 24: {email}")

print((f"Line 26: " + string.lower()))
print((f"Line 27: " + string.upper()))

print(f"Line 29: " + str(email.find("skyered.de")))
print(f"Line 30: " + email.replace("ö", "oe"))

print(f"Line 32: " +  str(string.__contains__("Teststring")))
