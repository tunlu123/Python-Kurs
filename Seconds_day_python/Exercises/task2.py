zahl1 = input("Gebe die erste Zahl ein ")
zahl2 = input("Gebe die zweite Zahl ein ")

# Größe in Bytes berechnen (UTF-8-Kodierung)
zahl1InBits = len(zahl1.encode('utf-8'))
zahl2InBits = len(zahl2.encode('utf-8'))

# Größe in Bits berechnen
größe_in_bits_zahl1 = zahl1InBits * 8
größe_in_bits_zahl2 = zahl2InBits * 8

print(f"Die erste Zahl ist {größe_in_bits_zahl1} bytes groß")
print(f"Die erste Zahl ist {größe_in_bits_zahl2} bytes groß")

print(int(zahl1) + int(zahl2))

gesamtGrößeInBit = (64 * 8) + (64 * 8) + größe_in_bits_zahl1 + größe_in_bits_zahl2 

print(f"Der Gesamtspeicherbedarf ist {gesamtGrößeInBit} bytes")
