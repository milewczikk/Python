#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

cen = int(input("Wprowadz podstawową cenę samochodu: "))

podat = (cen*0.2)
oplrej = (cen*0.1)
prowdil = 100
dost = 250

total = cen + podat + oplrej + prowdil + dost

print("\n\nPodatek wynosi: ", podat)
print("\nOpłata rejestracyjna wynosi: ", oplrej)

print("\nFaktyczna cena samochodu wynosi: ", total)
