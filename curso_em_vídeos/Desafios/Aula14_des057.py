# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 10:36:19 2021

@author: WarleY

print('-='*14)
print('DESAFIO 57')
print('-='*14)
# 57 - Faça um algoritmo que lia o sexo de uma pessoa, mas so aceita os valores M e F,
# caso esteja errado peça a digitação nomante ate ter o valor cerreto
sexo = input('Informe seu sexo [M/F]: ').strip().upper()[0]

while sexo not in 'MmFf':
    sexo = input('Dados INVALIDOS. Informe seu sexo [M/F]: ')
print('Sexo cadastro {}, cadastro finalizado!!!'.format(sexo))
print('\n')

print('-='*14)
print('DESAFIO 58')
print('-='*14)
# 58 - Melhore o jogo do Desafio 28. Agora o desafio e fazer um algoritmo  que
# o jogador vai tentar adivinhar ate acertar, mostrando os palpites no final,
# quando foram necessarios para acerta
import random 

chance = 1
sorteado = random.randrange(1,3)
print(
      SOU SEU COMPUTADOR...
      Acabei de pensar em um numero entre 0 e 10
      será que voce e capaz de adivinhar:)
num = int(input('Adivinhe o numero se for capaz: '))

while num != sorteado:
    if num == sorteado:
        chance +=1
        print('fim')
    elif num > sorteado:
        chance +=1
        num = int(input('MENOS... Digite outro número: '))
    else:
        chance =+1
        num = int(input('MAIS... Digite outro número: '))
print('fim')
print(chance)
print('\n')

print('-='*14)
print('DESAFIO 59')
print('-='*14) 
# 59 - Faça um algoritmo que leia dois valores e mostre um menu na
# tela: 1=Somar 2=Multiplicar 3=Maior 4=Novos Numeros 5=Sair
from time import sleep

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite o segundo valor: '))
conta = 0

print('+-*/'*14)
print('\n')
print( CALCULADORA
      
      [ 1 ] Somar
      [ 2 ] Subtrair
      [ 3 ] Multiplicar 
      [ 4 ] Dividir
      [ 5 ] Escolher outros valores 
      [ 6 ] Sair)
print('\n')
print('+-*/'*14)

opcao = int(input('Escolha uma opção: '))

while opcao != 6:
    if opcao == 1:
        conta = num1 + num2
        print('O resultado da soma são {}'.format(conta))
        opcao = int(input('Escolha uma opcao: '))
    elif opcao == 2:
        conta = num1 - num2
        print('A subtração dos dois valores são {}'.format(conta))
        opcao = int(input('Escolha uma opção: '))
    elif opcao == 3:
        conta = num1 * num2
        print('A multiplicação dos valores sao {}'.format(conta))
        opcao = int(input('Digite uma opção: '))
    elif opcao == 4:
        conta = num1 / num2
        print('A divisão dos valores sao {}'.format(conta))
        opcai = int(input('Escolha outra opção: '))
    elif opcao == 5:
        num1 = int(input('Digite um novo numero: '))
        num2 = int(input('Digite outro segundo numero: '))
        opcao = int(input('Escolhar uma opção'))
    elif opcao == 6:
        print('Fim dos calculos')
    else:
        print('Opção invalida')
        opcao = int(input('Digite outra opção: '))
print('Finalizando... ')
sleep(1)
print('Fim do programa')
print('\n')

print('-='*14)
print('DESAFIO 60')
print('-='*14)
# 60 - Faça um algoritmo que leia um numero e mostre seu fatorial
num = int(input('Digite um numero para calcular seu fatoria: '))
teste = num
fat = 1
print('Calculando {}!'.format(teste),'{}'.format(teste), end=' ')
while num >= 2:
    fat = fat*num
    num -= 1
    print('x {}'.format(num), end='  ')
print('= {}'.format(fat))
print('\n')

print('-='*14)
print('DESAFIO 61')
print('-='*14)
# 61 - Refaça o desafio 51, lendo o primeiro termo e a razao de uma PA,
# mostrando os 10 primeiro termos da progressao
termo = int(input('Termo: '))
razao = int(input('Razão: '))
decimo = 10
gamb = termo

while decimo != 1:
        gamb += razao
        print('{}'.format(gamb), end='-> ' ) 
        decimo -=1
    
print('Finish')
print('\n')

print('-='*14)
print('DESAFIO 62')
print('-='*14)
# 62 - Melhore o desafio 61, perguntando para o usuario se ele quer mostrar mais alguns termos.
# O programa encerrar quando ele disser que quer mostrar 0 termos
termo = int(input('Digite um termo: '))
razao = int(input('Razao: '))
gamb = termo
cont =1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print('{}'.format(gamb), end='-> ')
        gamb +=razao
        cont +=1
    print('Pausa')
    mais = int(input('Quantos termos voce quer mostrar a mais: '))
print('Fim')
print('\n')

print('-='*14)
print('DESAFIO 63')
print('-='*14)
# 63 - Faça um algoritmo que leia n numero e mostra na tela os n primeiro elementos de uma sequencia de fibonacci

termo = int(input('Quantos termos vc quer mostrar: '))
t1 = 0
t2 = 1
print('~'*30)
print('{} -> {}'.format(t1,t2), end='')
cont = 3

while cont <= termo:
    t3 = t1+t2
    print('-> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')
print('\n')

print('-='*14)
print('DESAFIO 64')
print('-='*14)
# 64 - Faça um algoritmo que leia varios numero interios.
# O programa so vai para quano o usuario digitar o valor 999,
# e e a condição de parada. No final mostre quantos numeros foram
# digitados e qual foi a soma deles. Desconsiderando o flag

num = 0
soma = 0
while num != 999:
       if num != 999:
        num = int(input('Digite um numero [999 para parar]: '))
        n = num
        soma = soma + n
print(soma-999)
print('\n')
"""
print('-='*14)
print('DESAFIO 65')
print('-='*14)
# 65 - Faça um algoritmo que leia varios numero. No final da execução,
# mostre a media entre todos os valores e qual foi o mairo e o menor valor lido.
# O programa dever perguntar ao usuario se ele deseja continuar.

stop = 'S'
soma = 0
media = 0
cont = 0
maior = 0
menor = 0

while stop == 'S':
    num = int(input('Digite um valor: '))
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    cont +=1
    soma += num
            
    stop = input('Deseja continuar [N/S]: ').upper()
media = soma/cont
print(maior)
print(menor)
print(media)
print('fim')






























 