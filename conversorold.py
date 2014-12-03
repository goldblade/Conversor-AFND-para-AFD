# -*- coding: utf-8 -*-
# ! /bin/env python
import os
import time
import itertools as it
from itertools import product, permutations, combinations, combinations_with_replacement

def cls():
    os.system(['clear', 'cls'][os.name == 'nt'])

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
	i = 0
	for eu in estado.um:
		if i == 0:
			um = um + eu.nome
		else:
			um = um + ',' + eu.nome
		i = i + 1
	um = um + '}'
	nome_estado = estado.nome
	if estado.inicial is True and estado.final is True:
		nome_estado = '->*' + str(nome_estado)
	else:
		if estado.inicial is True:
			nome_estado = '->' + str(estado.nome)
		if estado.final is True:
			nome_estado = '*' + str(estado.nome)
	print "%s|%s|%s" % (str(nome_estado).rjust(20), str(zero).rjust(20), str(um).rjust(20))

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
	estado = EscolheEstado('inserirTransicao', None)
	if estado is not None:
		print 'Estado foi escolhido: ' + estado.nome
		for x in range(0, 2):
			try:
				repeat = raw_input(
					'Deseja inserir transição para o caracter %d? Escolha S para sim, N para não: ' % (x))
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

	estadoNovo = Estado(nome)
	estadoNovo.afnd(afnd_uniao)
	for e in estadoNovo.afnd_uniao:
		if e.final is True:
			estadoNovo.final(True)
	return estadoNovo

def juntaEstado(lista):
	temp = lista
	for e in lista:
		try:
			for e2 in e.afnd_uniao:
				for e2_z in e2.zero:
					e.alfa_zero(e2_z)
				for e2_u in e2.um:
					e.alfa_um(e2_u)
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
	if qtd > len(lista) :
		listaglobal = estados + listaglobal
	else:
		for i in combinations(lista, qtd):
			e = Estado(i)
			listaglobal.append(e)
		combinaRecurEstado(qtd + 1, lista)

def combinaEstados():
	lista = listaglobal
	for e in lista:
		if type(e.nome) is tuple:
			nomeseparado = list(e.nome)
			for i in range(len(nomeseparado)):
				for es in estados:
					listaafnd = []
					if es.nome == nomeseparado[i]:
						listaafnd.append(es)
						if es.final is True:
							e.final(True)
						if len(es.zero) > 0:
							for ezero in es.zero:
								if ezero not in e.zero:
									e.alfa_zero(ezero)
						if len(es.um) > 0:
							for ezum in es.um:
								if ezum not in e.um:
									e.alfa_um(ezum)
					e.afnd(listaafnd)

	for idx in range(0, len(lista)):
		if lista[idx].inicial is True and idx != 0:
			estado = lista.pop(idx)
			lista.insert(0, estado)

	idx = 0
	removeu = False
	while idx < len(lista):
		if (len(lista[idx].zero) == 0) or (len(lista[idx].um) == 0):
			if lista[idx].inicial is True:
				lista[idx+1].inicial(True)
			lista.remove(lista[idx])
			removeu = True
		idx = idx + 1
		if removeu:
			idx = idx - 1
			removeu = False

	listaRemover = []
	for e in lista:
		if e.inicial is not True:
			for ref in lista:
				if e != ref:
					if len(ref.um) > 1:
						lista_um = []
						for o in ref.um:
							lista_um.append(o.nome)
						tupla_um = tuple(lista_um)
						if tupla_um == e.nome:
							listaRemover.append(e)
					else:
						if len(ref.um) > 0:
							if e.nome == ref.um[0].nome:
								listaRemover.append(e)
					if len(e.zero) > 1:
						lista_zero = []
						for o in ref.zero:
							lista_zero.append(o.nome)
						tupla_zero = tuple(lista_zero)
						if tupla_zero == e.nome:
							listaRemover.append(e)
					else:
						if len(ref.zero) > 0:
							if e.nome == ref.zero[0].nome:
								listaRemover.append(e)

	if len(listaRemover) > 0:
		for r in listaRemover:
			try:
				lista.remove(r)
			except Exception, e:
				pass

	'''removeu = False
	i = 0
	while i < len(lista):
		temReferencia = False
		if lista[i].inicial is not True:
			for j in range(0, i):
				if i != j:
					if len(lista[j].um) > 1:
						lista_um = []
						for o in lista[j].um:
							lista_um.append(o.nome)
						tupla_um = tuple(lista_um)
						if tupla_um == lista[i].nome:
							temReferencia = True
					else:
						if len(lista[j].um) > 0:5
							if lista[i].nome == lista[j].um[0].nome:
								temReferencia = True
					if len(lista[j].zero) > 1:
						lista_dois = []
						for o in lista[j].zero:
							lista_dois.append(o.nome)
						tupla_zero = tuple(lista_dois)
						if tupla_zero == lista[i].nome:
							temReferencia = True
					else:
						if len(lista[j].zero) > 0:
							if lista[i].nome == lista[j].zero[0].nome:
								temReferencia = True
			if not temReferencia:
				lista.remove(lista[i])
				removeu = True
		i = i + 1
		if removeu:
			i = i - 1
			removeu = False'''



	for t in lista:
		DesenhaEstado(t)

def Converter():
	transicao = estados

	for estado in transicao:
		if len(estado.zero) > 1:
			novoEstado = criaEstado(estado.zero)
			if novoEstado is not False:
				teste = novoEstado in transicao
				if teste:
					pass
				else:
					estado.alfa_zero_lista([novoEstado])
					transicao.append(novoEstado)

		if len(estado.um) > 1:
			novoEstado = criaEstado(estado.um)
			if novoEstado is not False:
				teste = novoEstado in transicao
				if teste:
					pass
				else:
					estado.alfa_um_lista([novoEstado])
					transicao.append(novoEstado)

	juntaEstadoTransicao = juntaEstado(transicao)

	for estado in juntaEstadoTransicao:
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
			print "%s|%s|%s" % (str("").rjust(20), str("0").rjust(20), str("1").rjust(20))
			print '--------------------------------------------------------------'
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
		estado0.alfa_zero_lista([estado0, estado1])
		estado0.alfa_um_lista([estado0])
		estado1.alfa_zero_lista([estado2])
		estado1.alfa_um_lista([])
		estado2.alfa_zero_lista([estado2])
		estado2.alfa_um_lista([estado2])
		estado2.final(True)
		estado3.alfa_zero([estado1])
		estado3.alfa_um([estado2])
		estados.append(estado0)
		estados.append(estado1)
		estados.append(estado2)
		#estados.append(estado3)

		cls()

		listanome = []
		for e in estados:
			listanome.append(e.nome)
		combinaRecurEstado(2, listanome)

		print '         AFND          '
		print ''
		print "%s|%s|%s" % (str("").rjust(20), str("0").rjust(20), str("1").rjust(20))
		print '--------------------------------------------------------------'
		combinaEstados()

	elif opcao == 6:
		print 'Saindo do programa....'
		break
	else:
		print 'Opção não disponível'