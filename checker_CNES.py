#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import requests
import os
import time
import random
from tqdm import tqdm
from random import randint
import fileinput
_output_ = open(raw_input("\nDIGITE O NOME DO ARQUIVO DE SAIDA COM OS CNES:\nEXEMPLO \"ARQUIVO.txt\"\n\n"), 'w')
cnes = []
#REGER PRA FILTRAR ESTABELECIMENTOS NO CONTENT DO REQUEST
def busca_estabelecimento(content):
    estabelecimentos = []
    for line in content.split('>'):
        index = line.find('href="Exibe_Ficha_Estabelecimento.asp')
        if index != -1:
            href_start = line.find('href="Exibe_Ficha_Estabelecimento.asp', index) + 6
            href_end = line.find('</a>', href_start)
            estabelecimentos.append(line[href_start:href_end])
    return estabelecimentos
#CONTAGEM DE CNES
NUMERO_CNES = 10000000
#PARAMETROS PRA CONSULTA DE CNES
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
url_valida_cnes = "http://cnes2.datasus.gov.br/Lista_Es_Nome.asp"
validos_ = 0
#FOR PRA GERAR CNES
print('Gerando lista de CNES...\n \n')
for i in tqdm(range(9999999)):
    cnes.append('%0.7d' %i)
#RANDOM NA LISTA DE CNES
print('\n \nSeparando os CNES aleatoriamente...')
random.shuffle(cnes)
#FOR VALIDA CNES
for item in cnes:
	os.system('cls')
	NUMERO_CNES = NUMERO_CNES-1
	print "\n \nCNES RESTANTES: %i" %NUMERO_CNES
	print("\n \nTESTANDO CNES:  %s") %item 
	payload = {'Vcodigo': item} 
	try:
	 valida_cnes = requests.get(url_valida_cnes, params=payload, headers=headers)
	except:
	 os.system('cls')
	 print "ERRO AO CONECTAR...\n"
	 print "RECONECTANDO...\n"
	 for i in tqdm(range(120)):
		os.system('cls')
		print "RECONECTANDO EM 120 SEGUNDOS...\n AGUARDE..."
		time.sleep(1)
	 valida_cnes = requests.get(url_valida_cnes, params=payload, headers=headers)
	consulta_estabelecimento = '\n'.join(busca_estabelecimento(valida_cnes.content))
	if consulta_estabelecimento == "":
	 print "\n \nCNES INVALIDO!	[ - ]\n"
	 print "\n %i VALIDOS\n" %validos_
	 time.sleep(0.8)
	else:
	 validos_ = validos_+1
	 print "\n \nCNES VALIDO!	[ + ]\n"
	 print "\n %i VALIDOS\n" %validos_
	 time.sleep(3)
	_output_.write(item)
	_output_.write("\n")
