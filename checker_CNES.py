#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import requests
import random
from tqdm import tqdm
from random import randint
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

#FOR PRA GERAR CNES
print('Gerando lista de CNES...\n \n')
for i in tqdm(range(9999999)):
    cnes.append('%0.7d' %i)
#RANDOM NA LISTA DE CNES
print('\n \nSeparando os CNES aleatoriamente...')
random.shuffle(cnes)
#FOR VALIDA CNES
for item in cnes:
	NUMERO_CNES = NUMERO_CNES-1
	print "\n \nCNES RESTANTES: %i" %NUMERO_CNES
	print("\n \nTESTANDO CNES: %s") %item 
	payload = {'Vcodigo': item} 
	valida_cnes = requests.get(url_valida_cnes, params=payload, headers=headers)
	consulta_estabelecimento = '\n'.join(busca_estabelecimento(valida_cnes.content))
	if consulta_estabelecimento == "":
	 print "\n \nCNES INVALIDO!\n"
	else:
	 print "\n \nCNES VALIDO!\n"
