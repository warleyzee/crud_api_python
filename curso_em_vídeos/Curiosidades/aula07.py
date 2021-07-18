# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 20:06:20 2021

@author: WarleY
"""

nome = input('digite seu nome: ')

idade = int(input('Digite sua idade: '))
mes = int(input('Digite o mes: '))
ano1 = 2020
ano2 = 2021

print('prazer {:=^20}!'.format(nome))

if mes >= 3:
   print('Voce nasceu no ano de {}'.format(ano1-idade))
else: print('Voce nasceu no ano de {}'.format(ano2-idade))


