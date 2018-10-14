import random
slowa=("python", "gdansk", "dlaczego", "gdynia", "wsb")
word=random.choice(slowa)
poprawnie = word
pomie=""
while word:
	position = random.randrange(len(word))
	pomie += word[position]
	word = word[:position] + word[(position + 1):]
#print (pomie)

print(
"""
	Witaj w grze 'Wymieszane litery'!
	Uporzadkuj litery, aby odtworzyc praidlowe slowo.
	(Aby zakonczyc zgadywanie, nacisnij klawisz Enter
	 bez podawania odpowiedzi.)
"""
)
print("Zgadnij, jakie to slowo: ", pomie)
zgaduj = input("\nTwoja odpowiedz: ")
a=1
while zgaduj != poprawnie and zgaduj !="":
	print("Niestety, to nie to slowo.")
	print("podpowiedz: ", poprawnie[position:a], "\n")
	a+=1
	zgaduj = input("Twoja odpowiedz: ")
if zgaduj==poprawnie:
	print("\nZgadza sie! Zgadles za" , a, "razem!")
print("Dziekuje za udzial w grze")
