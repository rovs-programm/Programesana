#Kalkulators Danila Poimanovs

#Tas ir krāsu mainas modulis
from colorama import init
from colorama import Fore, Back, Style

init()

#Šīs ir komandas krāsu mainai
print(Fore.WHITE)
print(Back.RED)

#Tas ir programmas sākums, prasa turpmākas darbības
what = input("Ko mēs darām? (+, -, *, /): ")

print(Back.CYAN)

#Vērtība, no kuras tiek veidota aprēķina formula
a = float(input("Vadīt pirmo skaitli: "))
b = float(input("Vadīt otro skaitli: "))

print(Back.RED)

#Aprēķinu formulas
if what == "+":
	c = a + b
	print("Rezultāts: " + str(c))

elif what == "-":
	c = a - b
	print("Rezultāts: " + str(c))

elif what == "*":
	c = a * b
	print("Rezultāts: " + str(c))

elif what == "/":
	c = a / b
	print("Rezultāts: " + str(c))

else:
	print("Atlasīta nederīga darbība!")

input()
