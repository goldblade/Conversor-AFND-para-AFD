# -*- coding: utf-8 -*-
#! /bin/env python
import os
import time
#from colorama import Fore, Back, Style, init

#init(autoreset=True)

def cls():
    os.system(['clear','cls'][os.name == 'nt'])

class Estado:

	def __init__(self, nome):		
		self.nome = nome
		self.zero = []
		self.um = []
	
	def alfa_zero(self, Estado):		
		self.zero.append(Estado)

	def alfa_um(self, Estado):
		self.um.append(Estado)

	def inicial(self, status):
		self.inicial = status		

	def final(self, status):
		self.final = status

def Opcoes():
	print '-------------- MENU --------------'	
	print '1 - Inserir Estados'
	print '2 - Inserir Transições'
	print '3 - Apagar'
	print '4 - Exibir Automato'
	print '5 - Converter para AFD'
	print '6 - Sair'
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

def DesenhaEstado(nome):	
	#print "%3s"  % (nome) + "%3s" % ('|')
	print "%s|%s" % (str(nome).rjust(6), nome)
	#print '{0} | {1}'.format(nome, nome)
	#print "%3d\n%3d" % (50, 150)
	
def EscolheEstado(origem, caracter):
	cls()
	print "-------------- Escolha o Estado --------------"
	
	i = 0
	for e in estados:
		print str(i) + ' - ' + e.nome
		i = i + 1
	print ''
	
	x = 0
	estado = None
	while True:		
		
		if origem == 'inserirTransicao':
			try:
				escolha = int(raw_input('Digite o número do estado que deseja inserir transições: '))	
			except Exception, e:
				print 'Ouve um erro na escolha, tente novamente'
				time.sleep(1)
				InserirTransicao()
				
		if origem == 'estadoDestino':
			#perguntar se deseja inserir transicao para o caracter 0 ou 1
			try:
				escolha = int(raw_input('Para o caracter %d escolha o estado de destino da transição: ' % (caracter)))
			except Exception, e:
				print 'Ouve um erro na escolha, tente novamente'
				time.sleep(1)
				InserirTransicao()			
				
		try:
			estado = estados[escolha]				
		except Exception, e:
			print u'Escolha inválida, tente novamente...'
			x = x + 1
			if x == 3:
				print u'Limite de tentativas inválidas excedida, retornando ao menu inicial...'
				time.sleep(1)
				cls()				
				break
			time.sleep(1)
		
		if estado is not None:
			break
	
	return estado

def InserirTransicao():
	#seleciona estado
	estado = EscolheEstado('inserirTransicao', None)
    #se tem estado pedir para escolher o estado de destino de acordo com o alfabeto
	if estado is not None:
		#escolhe estado de destino para o alfabeto
		print 'Estado foi escolhido: ' + estado.nome
		for x in range(0,2):
			try:
				repeat = raw_input('Deseja inserir transição para o caracter %d? Escolha S para sim, N para não: ' % (x))
			except Exception, e:
				print u'Ocorreu um problema, tente novamente pq tem exption?'
				x = x - 1
			
					
			if (repeat == 'S') or (repeat == 's'):
				
				estado_destino = EscolheEstado('estadoDestino', x)
				if estado_destino is not None:
					if x == 0:
						print estado
						print estado_destino
						estado.alfa_zero(estado_destino)
					if x == 1:
						print estado
						print estado_destino
						estado.alfa_um(estado_destino)
					print 'Transições inseridas com sucesso!'
				
		raw_input('Pressione enter para continuar....')
	
cls()
while True:
	opcao = Opcoes()
	if opcao == 1:
		NovoEstado()
		pass
	elif opcao == 2:
		''' Transicoes '''
		cls()
		if len(estados) > 0:
			InserirTransicao()
		else:
			print 'Por favor, cadastre os estados primeiro...'
			time.sleep(1)
	elif opcao == 3:
		print ''' Apagar algo '''		
	elif opcao == 4:
		'''Exibir automato'''
		cls()
		if len(estados) > 0:
			print '         AFND          '
			print ''
			print '      |   0   |   1   |'
			print '-----------------------'
			for e in estados:
				DesenhaEstado(e.nome)			
		else:
			print 'Nenhum estado cadastrado'
		raw_input('Pressione enter para continuar....')
		cls()
	elif opcao == 5:
		''' Converter para AFD '''
		print 'convertendo....'
	elif opcao == 6:
		print 'Saindo do programa....'
		break
	else:		
		print 'Opção não disponível'
	#pass
