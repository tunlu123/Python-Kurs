vorNamen = ["Max", "Tom", "Sina"];
nachNamen = ["Mustermann", "Müller", "Sniff"]

domain = "@skyered.de"

i = 0
for _ in vorNamen:
    name = ".".join([vorNamen[i], nachNamen[i]])
    name += domain
    print(name)
    i +=1
 