# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 14:31:35 2021

@author: WarleY


print('==== Desafio 22 ===')
# 22 - Crie um algorimo que leia o nome completa da pessoa e mostre 
# O nome com todas letras misculas, minusculas, total de letras sem espaço, 
# quantas letras tem o primeiro nome

nome = input('Escreva seu nome completo: ')
primeiro = nome.split()
print('Seu nome todo maiusculo fica: {} '.format(nome.upper()))
print('Seu nome minusculo fica: {} '.format(nome.lower()))
print('Seu primeiro nome tem {} letras'.format(len(primeiro[0])))

print('\n')

print('==== Desafio 23 ===')
# 23 - Faça um algoritimo que leia qualquer numero entre o e 999 e mostre na tela ]
# cada um dos digitos. Ex1834 = unidade 4 desena 3 centena 9 milhar 1

numero = int(input('Digite um numero entre 0 e 999: '))
unidade = numero % 10
numero = (numero - unidade) / 10
dezena = numero % 10
numero = (numero - dezena)/10
centena = numero

dezena = int(dezena)
centena = int(numero)

print('centena {} '.format(centena))
print('Dezena {}'.format(dezena))
print('Unidade {} '.format(unidade))
print('\n')


print('==== Desafio 24 ===')
# 24 - Crie um algoritmo que leai o nome de uma cidade e diga se ela começa com o nome Santo

nomecidade = input('Digite o nome da sua cidade: ')

if nomecidade[:5] == 'Santo':
    print('Cidade Santa')
else:
    print('Cidade nao Santa')
print('\n')

print('=== Desafio 25 ===')
# Crie um algoritmo que leia o nome da pessoa e diga se ela tem silva no nome

nome = input('Digite seu nome: ')

if 'Silva' in nome:
    print('Pobre')
else:
    print('Talvez nao')
print('\n')

print('=== Desafio 26 ===')
# 26 - Faça um algoritmo que leia uma frase pelo teclado e mostre: quantas vezes aparece
# a letra A em qual posição ela aparece primeiro, em que posição ela aparece a ultima vez

frase = input('Digite uma frase: ').upper().strip()
letra = frase.count('A') 

print('A letra -A- aparece {}x'.format(letra))
print('A letra -A- apareceu a primeira vez na posição {}'.format(frase.find('A')+1))
print('A ultima letra -A- aparece na posição {}'.format(frase.rfind('A')+1))
print('\n')
"""

print('=== Desafio 27 ===')
# 27 - Faça um algoritmo que leia o nome completo de uma pessoa, mostre depois o primeiro 
# e o ultimo nome, 

nome = input('Digite seu nome compelo: ').strip()
primeiro = nome.split()

print('Seu primeiro nome é: {}'.format(primeiro[0]))
print('Seu ultimo nome é: {} '.format(primeiro[len()-1]))





















  