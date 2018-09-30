#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

import random
liczba = random.randint(1,50)
for i in range(6):
	odp = input("Jaka liczba od 1 do 50 wylosowano: ")
	if liczba == int(odp):
		print("Dobrze ")
	else:
		print("Nie dobrze")
