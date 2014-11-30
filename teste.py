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


	for x in range(len(lista)):

if e != lista[x]:
				nome = e.nome + str(lista[x].nome)
				contrario = str(lista[x].nome) + e.nome
				estado = Estado(nome)
				verify = verificaExistencia(teste, nome, contrario)
				#verifycontrario = verificaExistencia(lista, contrario)
				afnd_uniao = []

				if len(e.zero) > 1:
					for e2 in e.zero:
						afnd_uniao.append(e2)

				if len(lista[x].zero) > 1:
					for e2 in lista[x].zero:
						afnd_uniao.append(e2)

				if len(e.um) > 1:
					for e2 in e.um:
						afnd_uniao.append(e2)

				if len(lista[x].um) > 1:
					for e2 in lista[x].um:
						afnd_uniao.append(e2)

				if len(afnd_uniao) > 0:
					estado.afnd(afnd_uniao)
				if not verify:
					teste.append(estado)


				#nome = e + estados[x]
				#contrario = estados[x] + e
				#if (nome not in teste) and (contrario not in teste):
				#	teste.append(nome)