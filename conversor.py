# -*- coding: utf-8 -*-
#! /bin/env python
import os
import time

def cls():
    os.system(['clear','cls'][os.name == 'nt'])

class Estado:

	def __init__(self, nome):		
		self.nome = nome
	
	def alfa_zero(self, Estado):
		self.proximo_estado = Estado

	def alfa_um(self, Estado):
		self.proximo_estado = Estado

	def inicial(self, status):
		self.inicial = status

	def final(self, status):
		self.final = status

def Opcoes():
	print '-------------- MENU --------------'	
	print '1 - Inserir Estados'
	print '2 - Exibir Estados'
	print '5 - Sair'
	print ''
	try:
		opcao = int(raw_input('Escolha uma opção: '))		
		return opcao
		pass
	except Exception, e:
		print u'Opção Inválida'

estados = []
inicial = False

def NovoEstado():
	cls()
	print "-------------- NOVO ESTADO --------------"

	try:
		nome = raw_input('Entre com o Nome do Estado: ')
		estado = Estado(nome)		
		pass
	except Exception, e:
		print u'Ocorreu um problema, tente novamente'

	global inicial

	if not inicial:

		while True:

			try:
				repeat = raw_input('Deseja que este estado seja o estado Inicial? Escolha S para sim, N para não: ')
			except Exception, e:
				print u'Ocorreu um problema, tente novamente'

			if (repeat == 'S') or (repeat == 's'):
				estado.inicial(True)
				inicial = True
				break
			elif (repeat == 'N') or (repeat == 'n'):				
				break				
			else:
				print u'Escolha inválida, tente novamente...'
				time.sleep(1)

	while True:

		try:
			repeat = raw_input('Deseja que este estado seja o estado Final? Escolha S para sim, N para não: ')
		except Exception, e:
			print u'Ocorreu um problema, tente novamente'

		if (repeat == 'S') or (repeat == 's'):
			estado.final(True)			
			break
		elif (repeat == 'N') or (repeat == 'n'):				
			break				
		else:
			print u'Escolha inválida, tente novamente...'
			time.sleep(1)								

	estados.append(estado)

	cls()
	print 'Estado ' + nome + ' Inserido com sucesso!'
	try:
		repeat = raw_input('Deseja inserir um novo estado? Escolha S para sim, N para não: ')
	except Exception, e:
		print u'Ocorreu um problema, tente novamente'	
	if (repeat == 'S') or (repeat == 's'):
		NovoEstado()
	elif (repeat == 'N') or (repeat == 'n'):
		print 'Voltando ao menu...'	
		time.sleep(1)
		cls()
	else:
		print 'Escolha invalida, retornando ao menu...'
		time.sleep(1)
		cls()

#nome = raw_input('Entre com o Nome: ')
#idade = int(raw_input('Entre com a idade: '))
while True:
	opcao = Opcoes()
	if opcao == 1:
		NovoEstado()
		pass
	elif opcao == 2:
		print estados
	elif opcao == 5:
		print 'Saindo do programa....'
		break
	else:		
		print 'Opção não disponível'
	#pass
