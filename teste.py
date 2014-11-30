# -*- coding: utf-8 -*-
#! /bin/env python
import os

estados = ['q0', 'q1', 'q2', 'q3', 'q4']
teste = []
estadofinal = ""
for e in estados:	
	#x = 0	
	for x in range(len(estados)):
		if e != estados[x]:
			nome = e + estados[x]
			contrario = estados[x] + e			
			if (nome not in teste) and (contrario not in teste):
				teste.append(nome)
	estadofinal = estadofinal + e


teste = estados + teste
teste.append(estadofinal)
print '-----'
print  teste
	