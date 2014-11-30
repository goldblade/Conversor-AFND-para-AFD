# -*- coding: utf-8 -*-
#! /bin/env python
import os
import time
import itertools as it
from itertools import product, permutations, combinations, combinations_with_replacement
#from colorama import Fore, Back, Style, init
#http://www.htmlstaff.org/ver.php?id=26987

#init(autoreset=True)

def cls():
    os.system(['clear','cls'][os.name == 'nt'])

class Estado:

	def __init__(self, nome):		
		self.nome = nome
		self.zero = []
		self.um = []
		self.anfd_uniao = []
		
	def alfa_zero(self, Estado):		
		self.zero.append(Estado)
	
	def alfa_zero_lista(self, listaDeEstados):
		self.zero = listaDeEstados
	
	def alfa_um(self, Estado):
		self.um.append(Estado)

	def alfa_um_lista(self, listaDeEstados):		
		self.um = listaDeEstados

	def inicial(self, status):
		self.inicial = status		

	def final(self, status):
		self.final = status

	def afnd(self, listaDeEstados):
		self.afnd_uniao = listaDeEstados	

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
afd = []
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

def DesenhaEstado(estado):	
	#print "%3s"  % (nome) + "%3s" % ('|')
	''' monta a string com os estados para o caracter 0 '''
	zero = '{'
	i = 0
	for ez in estado.zero:
		if i == 0:
			zero = zero + ez.nome
		else:
			zero = zero + ',' + ez.nome
		i = i + 1
	zero = zero + '}'
	um = '{'
	''' monta a string com os estados para o caracter 1 '''
	i = 0
	for eu in estado.um:
		if i == 0:
			um = um + eu.nome
		else:
			um = um + ',' + eu.nome
		i = i + 1
	um = um + '}'	
	nome_estado = estado.nome
	if estado.inicial is True:
		nome_estado = '->' + estado.nome
	if estado.final is True:
		nome_estado = '*' + estado.nome
	print "%s|%s|%s" % (str(nome_estado).rjust(6), str(zero).rjust(6), str(um).rjust(6))
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


''' 
TESTE DE MESA PARA ALGORITMO DE CONVERSAO 

comeco pelo o estado inicial, processo os estados que tem em 0 e depois em 1

se tiver mais de um estado em 0 ou 1, a uniao desses estados vira um novo estado, verifica-se se o estado ja existe na 
lista de de afd se nao existir adciona ele

eliminar estados sem alcance a partir do estado inicial
'''

'''

- procura estado inicial na lista de afn
- verifica se tem estados vazio na lista de um e zero, se encontrar vazio tem que eliminar o estado e achar o inicial de acordo com o apontamento da transicao
- verificar se para o caracter zero tenho mais de 1 estado possivel, caso nao tenha, verificar se o estado já existe na lista de afd




'''
def criaEstado(listaDeEstados):
	lista_zero = []
	lista_um = []	
	nome = ""
	afnd_uniao = []
	final = False
	i = 0
	for estado in listaDeEstados:				
		if i == 0:			
			nome = nome + estado.nome
		else:			
			nome = nome + "" + estado.nome						
		afnd_uniao.append(estado)
		i = i + 1		
		'''		
		for j in range(0, len(estado.zero)):			
			if estado.zero[j] not in lista_zero:
				lista_zero.append(estado.zero[j])
		for j in range(0, len(estado.um)):			
			if estado.um[j] not in lista_um:
				lista_um.append(estado.um[j])
		'''

		'''
		if len(estado.zero) > 0:
			for i in range(0, len(estado.zero)):
				zero.append(estado.zero[i])
		if len(estado.um) > 0:
			for j in range(0, len(estado.um)):
				print j
				um.append(estado.um[j])
		afnd_uniao.append(estado)'''

	estadoNovo = Estado(nome)
	#set(lista_zero)
	#set(lista_um)		
	#estadoNovo.alfa_zero_lista(lista_zero)	
	#estadoNovo.alfa_um_lista(lista_um)
	#estado.final(True)	
	estadoNovo.afnd(afnd_uniao)	
	for e in estadoNovo.afnd_uniao:		
		if e.final is True:
			estadoNovo.final(True)					
	return estadoNovo

'''
def estadoExiste(transicao, estado):
	if

	for referencia in listaDeEstados:
		zero.append(transicao[referencia].zero)
		um.append(transicao[referencia].um)
	
	for estado in transicao:
		if(estado.zero == zero and estado.um == um):
			return True
	
	return False


[0]q0 - 0[1, 2] / 1[]
[1]q1
[2]q2
'''

def juntaEstado(lista):	
	temp = lista
	for e in lista:				
		try:
			#print e.nome + ' tem estados unidos ' + str(e.afnd_uniao)
			''' processar alfa zero '''
			''' processar alfa um '''			
			for e2 in e.afnd_uniao:
				for e2_z in e2.zero:
					e.alfa_zero(e2_z)				
				for e2_u in e2.um:
					e.alfa_um(e2_u)
				#e.alfa_zero(e2)
				#e.alfa_um(e2)			
				pass
		except Exception, e:
			pass		
	return temp

def verificaExistencia(lista, nome, nomecontrario):
	for x in lista:		
		if nome == x.nome:
			return True
		if nomecontrario == x.nome:
			return True
	return False


listaglobal = []
def combinaRecurEstado(qtd, lista):
	global listaglobal
	if qtd <= 1:
		#print lista + listaglobal
		#for l in lista:
		#	listaglobal.append(l)
		listaglobal = estados + listaglobal
	else:
		for i in combinations(lista, qtd):
			e = Estado(i)
			listaglobal.append(e)
			#print i
		combinaRecurEstado(qtd-1, lista)


'''
def criarEstados():
	for j in listaglobal:
		print j.nome

	teste = list(j.nome)
		for x in range(0, len(teste)):
			print teste[x]
		print teste[1]'''



def combinaEstados():
	lista = listaglobal
	#print lista[1].nome

	for e in lista:
		''' detectar tupla '''
		#print type(e.nome)
		if type(e.nome) is tuple:
			''' separar nomes e procurar referencia para zero e um nos estados afn '''
			nomeseparado = list(e.nome)
			#print len(nomeseparado)
			for i in range(len(nomeseparado)):
				for es in estados:
					if es.nome == nomeseparado[i]:
						if len(es.zero) > 0:
							for ezero in es.zero:
								if ezero not in e.zero:
									e.alfa_zero(ezero)
						if len(es.um) > 0:
							for ezum in es.um:
								if ezum not in e.um:
									e.alfa_um(ezum)
						#print 'achou a bagaca: ' + e.nome
						#print nomeseparado[i]





	#teste = juntaEstado(teste)
	for t in lista:
		DesenhaEstado(t)

	#for s in xrange(len(lista)+1):
	#	teste = combinations_with_replacement(lista, s)
	#return list(teste)
	#for x in list(teste):
	#	for j in x:
	#		print j.nome



def Converter():	
	transicao = estados

	for estado in transicao:				
		if len(estado.zero) > 1:	
			novoEstado = criaEstado(estado.zero)							
			if novoEstado is not False:					
				teste = novoEstado in transicao				
				if teste:
					#print 'ja existe o estado'
					pass
				else:
					#print 'nao tem o estado'
					estado.alfa_zero_lista([novoEstado])
					transicao.append(novoEstado)					
					
					
					
		if len(estado.um) > 1:
			novoEstado = criaEstado(estado.um)
			if novoEstado is not False:								
				teste = novoEstado in transicao				
				if teste:
					pass
					#print 'ja existe o estado para um'
				else:
					#print 'nao tem o estado'
					estado.alfa_um_lista([novoEstado])
					transicao.append(novoEstado)					
					

	teste = juntaEstado(transicao)

	#print teste
	for estado in teste:
		DesenhaEstado(estado)


	

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
				DesenhaEstado(e)			
		else:
			print 'Nenhum estado cadastrado'
		raw_input('Pressione enter para continuar....')
		cls()
	elif opcao == 5:
		estado0 = Estado("q0")
		estado1 = Estado("q1")
		estado2 = Estado("q2")
		estado3 = Estado("q3")
		estado0.inicial(True)
		estado0.alfa_zero_lista([estado0])
		estado0.alfa_um_lista([estado0, estado1])
		estado1.alfa_zero_lista([])
		estado1.alfa_um_lista([estado2])
		estado2.alfa_zero_lista([estado2])
		estado2.alfa_um_lista([estado2])
		estado2.final(True)
		estado3.alfa_zero([estado1])
		estado3.alfa_um([estado2])
		estados.append(estado0)
		estados.append(estado1)
		estados.append(estado2)
		#estados.append(estado3)
		''' Converter para AFD '''
		cls()		
		#print list(combinations(estados, len(estados)))
		listanome = []
		for e in estados:
			listanome.append(e.nome)
		#print listanome
		#limpando = list(product(listanome, listanome))	
		
		'''
		listafull = []
		for i in combinations(listanome, 2):
			listafull.append(i)
			print i
		for i in combinations(listanome, 3):
			listafull.append(i)
			print i	
		for i in combinations(listanome, 4):
			listafull.append(i)
			print i	
		#limpando = listanome + limpando		
		listafull = listanome + listafull
		print listafull
		'''
		combinaRecurEstado(len(estados), listanome)
		#criarEstados()
		combinaEstados()
		#Converter()
	elif opcao == 6:
		print 'Saindo do programa....'
		break
	else:		
		print 'Opção não disponível'
	#pass
