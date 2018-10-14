import random
slowa=("python")
#, "gdansk", "dlaczego", "gdynia", "wsb"
word=random.choice(slowa)
poprawnie = word
pomie=""
while word:
	position = len(word)
	pomie += word[position]
	word = word[:position] + word[(position + 1):]
print (pomie)
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
litera = input("\nTwoja litera: ")
a=1
b=5
while b>0:
	if litera == poprawnie[position:] and zgaduj !="":
		print("TAK")
		b-=1
		litera = input("\nTwoja litera: ")
	elif litera != poprawnie[position] and zgaduj !="":
		print("NIE")
		b-=1
		litera = input("\nTwoja litera: ")
zgaduj = input("\nTwoja odpowiedz: ")
while zgaduj != poprawnie and zgaduj !="":
	print("Niestety, to nie to slowo.")
	print("podpowiedz: ", poprawnie[position:a], "\n")
	a+=1
	zgaduj = input("Twoja odpowiedz: ")
if zgaduj==poprawnie:
	print("\nZgadza sie! Zgadles za" , a, "razem!")
print("Dziekuje za udzial w grze")
