# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 22:05:50 2021

@author: WarleY
"""  

print('=== Desafio 28 ===')
# 28 - Faça um algoritmo que faco o computador pensar em um numero inteiro
# ente 0 e 5 e pera para o usuario tentar descobir o numero escolhido. O programa
# devera esvrever na tela se o usuario venceu ou nao

import random

sorteado = random.randrange(0,5)

palpite = int(input('Digite um numero entre 0 e 5: '))

if palpite == sorteado:
    print('Cagão')
else:
    print('Nao foi dessa vez')
    print('O numero certo era {}'.format(sorteado))
print('\n')

print('=== Desafio 29 ===')
# 29 - Faça um algoritmo que leia a velocidade do carro, se ele 
# ultrapassar 80km/h mostra uma mensagem dizendo que ele foi mutado, 
# a multa vai custar 7 por cada km a cima do limite

velocidade = int(input('Digite a velocidade do carro: '))

if velocidade == 80:
    print('parabens voce nao tem multa!!!')
else:
    excedeu = velocidade - 80
    multa = excedeu * 7
    print('Você excedeu {}Km/h, sua muta e de R${},00'.format(excedeu,multa))
print('\n')

print('=== Desafio 30 ===')
# 30 - Faça um algoritmo que leia um numero interio e diga se ele e par ou impar

numero = int(input('Digite o valor de um numero interio: '))

if numero%2 == 0:
    print('Par')
else:
    print('Impar')
print('\n')

print('=== Desafio 31 ===')
# 31 - Faça um algoritmo que pergunte a distancia de uma viagem em km. 
# calculo o preço da passargem cobrada, 0,50 centavos por km ate viagem
# a 200km e 0,45 centavos para viagem a cima de 200

viagem = float(input('Digite a distancia da viagem: '))
if viagem == 200:
    preco = 200*0.5
    print('O preço da passagem é R${}'.format(preco))
else:
    preco = viagem *0.45
    print('O preço da passagem é R${}'.format(preco))
print('\n')

print('=== Desafio 31 ===')
# 32 - Faça um algoritmo que leia se o ano e bissexto
ano = int(input('Digite um ano qualquer para saber se e bissexto: '))

if ano%4 == 0:
    print('Ano bissexto')
else:
    print('Esse ano nao e bissexto')
print('\n')
 

print('=== Desafio 33 ===')
# 33 - Faça um algoritmo que leia 3 numero e mostre qual e maior e qual e menor

num1 = int(input('Digite o primeiro numero : '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))

menor = num1

if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

maior = num1

if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
    
print ('Maior {} Menor {}'.format(maior,menor))
print('\n')


print('=== Desafio 34 ===')

# 34 - Faça um algoritmo que pergunta o salario do funcionario e calculo o
# valor do seu aumento. para salarios a cima de 2500 
# calcule 10% para inferiores calcule 15%

salario = float(input('Digite o salario do Funcionario: '))

aumentoDez = (10*salario)/100
totalDez = salario + aumentoDez
aumentoQuinze = (15*salario)/100
totalQuinze = salario + aumentoQuinze

if salario >= 2500:
    print('O Salario atual e R${} teve um aumento de 10% que equivale a R${} seu salario novo e de R${}'
          .format(salario, aumentoDez, totalDez ))
else:
    print('O Salario atual e R${} teve um aumento de 10% que equivale a R${} seu salario novo e de R${}'
          .format(salario, aumentoQuinze, totalQuinze ))
print('\n')


print('=== Desafio 35 ===')

r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: ')) 
r3 = float(input('Digite o valor da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar um triangulo')
else:
    print('Os seguimentos nao podem formar um triangulo')

    # 35 - Faça um algoritimo que leia o comprimento de tres retas e diga ao 
    # usuario se elas podem ou nao formar um triangulo



























































