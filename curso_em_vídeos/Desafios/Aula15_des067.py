# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 11:48:58 2021

@author: WarleY

print('-='*14)
print('Desafio 66')
print('-='*14)
# 66 - Cria um algoritmo que leia varios numeros interios. O programa so vai
# parar quando o usuario digigar o valor 999. No final mostre quantos numeros
# foram digitados e qual foi a soma entre eles
num = 0
cont = 0
soma = 0
while True:
    num = int(input('Digite um valor [999 - para parar]: '))
    if num ==999:
        break
    soma += num
    cont += 1
print(f'A soma dos {cont} valores são {soma}')
print('/n')

print('-='*14)
print('Desafio 67')
print('-='*14)
# 67 - Faça um algoritmo que mostre a tabuada de varios numeros,
# um de cada vez. apra cada valor digitado pelo usuario. O programa
# sera interrompido quando o numero soliciado for negativo

num = 0 
numero = 1

while True:
    numero = int(input('Quer ver a tabuado de qual valor: '))
    if numero < 0:
        break
    print('-'*14)
    for i in range (1,10+1):
        multi = numero * i
        print(f'{numero} x {i} = {multi}')
    print('-'*14)
print('fim')
print('/n')
"""
print('-='*14)
print('Desafio 68')
print('-='*14)
# 68 - Faça um algoritmo que jogue par ou impar com o computador. 
# O jogo sera interrompido quando o jogador perder, mostarndo o total
# de vitorias consecutivas que ele conquistou no final do jogo
import random

print('=-'*14)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*14)
pontoAi = 0
pontoPlayer = 0
while True:
    if pontoAi ==1:
        print('VOCE PERDEU')
        print('-'*18)
        print(f'GAME OVER! Você venceu {pontoPlayer} vezes ')
        break
    computer = random.randrange(0,10)
    valor = int(input('Diga um valor: '))
    jogo = input('Par ou Impor: [P/I]: ').upper().strip()
    soma = valor+computer
    
    if jogo == 'P' and soma % 2 == 0:
        pontoPlayer +=1
    elif jogo == 'I' and soma % 2 != 0:
        pontoPlayer +=1
    else:
        pontoAi +=1
    print('-'*18)
    print(f'Voce jogou {valor} e o computador jogou {computer}. Total de {soma}')
    print('='*18)














# 69 - Faça um algoritmo que leia a idade e o sexo de varias pessoas, A cada pessoa cadastrada o programa devera perguntar so o usuario qeur ou nao continuar. Quantas pessoas tem mais de 18 anos, quantos homens foram cadastrado e quantas mulheres tem menos de 20 anos
#
# 70 - Faça um algoritmo que leia o nome e o preço de varios produtos, o algoritmo devera perguntar se o usuario vai conitunar e no final mostrar. Qual e o total gasto, quantos produtos custaram maid de 1000, qual e o nome do produto mais barato
#
# 71 - Faça um algoritmo que simule o funcionamento de um caixa, no inicio ele perguntar ao usuario qual sera o valor a ser sacado e o programa vai informar quantas cedulas de cada valor seram entregue. Considerando apenas notas de 50,20,10,1 
#
# 72 - 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
