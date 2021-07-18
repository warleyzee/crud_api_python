# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 13:16:21 2021

@author: WarleY
"""

frase = 'Aprendendo Python de Forma Urgente'
#Fatiando strings
print('Imprima a frase: {}'.format(frase))
print('Imprima a letra na posição 4: {} '.format(frase[4]))
print('Imprima as letras na posição 3 : 10: {} '.format(frase[3:10]))
print('Imprima a frase da posição 0 : 10: '.format(frase[:10]))
print('Impreima a frase comecando da posição 10 ate o fim: '.format(frase[10:]))
print('Imprima a frase da posição 2:15 pulando de 2em2: {} '.format(frase[2:15:2]))

print('Qual o tamanho da frase: {} caracteres'.format(len(frase)))

frase2 = '     tirando os espaço em branco   '
print('Qual o tamanho total da frase {} caracteres'.format(len(frase2)))
print('Tirando os espaços agora {} caracteres'.format(len(frase2.strip())))
print('antiga {} nova {} '.format(frase2, frase2.replace("branco", "preto")))

frase3 = 'Aprendendo a dividir uma frase'
dividido = frase3.split()
print(dividido)
print('Acessando os letras dividas {}'.format(dividido[2][5]))