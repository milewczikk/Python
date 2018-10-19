import random
slowa=("python", "gdansk", "dlaczego", "gdynia", "wsb")
word=random.choice(slowa)
poprawnie = word
iloscliter=len(word)
b=5
print(
"""
	Witaj w grze 'Losowe slowa'!
	Masz na poczatek 5 prob na sprawdzenie,
	czy dana litera wystepuje w wylosowanym slowie.
	Nastepnie po 5 probach musisz odgadnac slowo.
	(Aby zakonczyc zgadywanie, nacisnij klawisz Enter
	 bez podawania odpowiedzi.)
"""
)
while b>0:
	litera = input("\nTwoja litera: ")
	if litera in poprawnie and litera !="":
		print("TAK")
		b = b-1
	else:
		print("NIE")
		b = b-1
zgaduj = input("\nTwoja odpowiedz: ")
while zgaduj != poprawnie and zgaduj !="":
	print("Niestety, to nie to slowo.")
	zgaduj = input("\nTwoja odpowiedz: ")
if zgaduj == poprawnie and zgaduj !="":
	print("\nZgadza sie!")
print("Dziekuje za udzial w grze")
