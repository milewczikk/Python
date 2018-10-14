a = int(input("podaj liczbe poczatkowa: "))
b = int(input("podaj liczbe koncowa: "))
c = int(input("podaj wielkosc odstepu: "))

if a>b:
	for i in range(b,a,c):
		print (i)

elif b>a:
	for j in range(a,b,c):
		print (j)

