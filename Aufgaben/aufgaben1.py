# Erstellen von 8 Variablen mit unterschiedlichen Datentypen
int_var = 10                   # Integer
float_var = 10.5               # Float
string_var = "Hallo Welt"      # String
bool_var = True                # Boolean
list_var = [1, 2, 3, 4, 5]     # Liste
dict_var = {"key": "value"}    # Dictionary
tuple_var = (1, 2, 3)          # Tuple
set_var = {1, 2, 3}            # Set

# Eingabe vom Benutzer entgegennehmen
user_input = input("Bitte geben Sie etwas ein: ")

# Typ der Eingabe speichern
input_type = type(user_input)

# Typ der Inputvariablen in der Konsole ausgeben
print(f"Der Typ der Eingabe ist: {input_type}")

# Methode definieren
def example_function(param1, param2):
    # Beispielhafte Logik
    if param1 > param2:
        print(f"{param1} ist größer als {param2}.")
    else:
        print(f"{param1} ist nicht größer als {param2}.")

    # For-Schleife mit logischem Operator
    for i in range(5):
        if i % 2 == 0:  # logischer Operator: modulo
            print(f"{i} ist gerade.")

# Methode aufrufen mit zwei Parametern
example_function(10, 5)