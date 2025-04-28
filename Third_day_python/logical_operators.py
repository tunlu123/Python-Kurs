import cpuinfo

x = 3
y = 25

s = 23

def printMessage(line):
    print(f"Do something: Line: {line}")

#if x < y or x == s:
#    printMessage(11)

#if x < y and x == s:
#     printMessage(14)

#if (x < y) != (x == s):
#     printMessage(17)

#if (x < y) == (x == s):
#     printMessage(20)

#if type(x) is int:
#    printMessage(23)

#if type(x) is not str:
#     printMessage(26)


cities = ["Prag", "Berlin", "Paris", "Brüssel", "Amsterdam", "Ankara", "Warschau", "Pekin", "Tokyo"]

if cities.__contains__("Tokyo") and cities.__contains__("Paris"):
    print("Found cities")

if cities.__contains__("Brüssel") or cities.__contains__("Ankara"):
    print("Found 1 city")

# 2 x input
# check if input int
# if input int then addition
# print sum in terminal

number = input("Please give me number 1 ")
number2 = input("Please give me number 2 ")

if type(number) is int and type(number2) is int:
    sum = number2 + number
    print(sum)

age = 6
permission = True

if age >= 12 or permission:
    printMessage(53)


cpus = cpuinfo.get_cpu_info()["count"]

minimumCpu = 4
optimumCpu = 8

# if cpus minimum and optimum cpu reached
# if cpus minimum cpu -> print("You have minimum cpu count")
# if cpus optimum cpu -> print("You have optimum cpu count")

if cpus >= minimumCpu and cpus >= optimumCpu:
    print(f"You have {cpus} cpu count and reached the optimum requirement")

    if cpus >= optimumCpu:
        print("You have optimum cpu")
    else:
        print("You reached minimum requirement")

if cpus < minimumCpu:
    print("You have less then minimum cpu")

