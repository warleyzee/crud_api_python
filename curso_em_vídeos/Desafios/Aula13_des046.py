# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 20:07:12 2021

@author: WarleY

print('-='*14)
print('DESAFIO 46')
print('-='*14)
# 46 - Faça um algoritmo que mostra na tela uma contavem regressiva para 
# o estouro de fogos de artificio. indo de 10 ate 0 com pausa de 1 segunto entre elas

from time import sleep

for x in range(10,0,-1):
    print(x)
    sleep(1)
print('BOOM, Feliz ano novo')
print('\n')

print('-='*14)
print('DESAFIO 46')
print('-='*14)
# 47 - Crie um algoritimo que mostra na tela todos os numero pares 1 a 50

for x in range (0,50,2):
    print(x, end=' ')
print('Finish')
print('\n')

print('-='*14)
print('DESAFIO 48')
print('-='*14)
# 48 - Faça um algoritimo que calcule a soma entre todos os numero pares
# que sao multiplos de 3 entre 1 e 500
soma = 0
cont = 0
for x in range(1, 501, 2):
    if x % 3 == 0:
        cont = cont + 1
        soma = soma + x
print('A soma de todos os {} valores sao {}'.format(cont, soma))

print('-='*14)
print('DESAFIO 50')
print('-='*14)   
# 50 - faça um algoritmo que leia seis numero interio e mostre a somoa apenas
# daqueles que foram par.
soma = 0
for x in range (0,6):
   numero = int(input(('Digite um numero: ')))
   if numero %2 == 0:
      soma = soma + numero

print('A soma dos valores pares sao {}'.format(soma))
print('\n')
"""
print('-='*14)
print('DESAFIO 51')
print('10 TERMOS DE UMA PA')
print('-='*14) 
# 51 - Fala um algoritmo que leia o primeio termo e a razao de um PA. No final
# mostre os 10 primeiros termos dessa progressao 

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10 - 1) * razao

for x in range (termo, decimo + razao, razao):
   print('{}'.format(x), end='-> ')
print('Finish')
print('\n')
# """
# print('-='*14)
# print('DESAFIO 52')
# print('-='*14) 
# # 52 - Faça um programa que leia um numero interio e diga se ele e ou nao um numero primo

# numero = int(input('Digite um numero: '))
# cont = 0

# for x in range(1,numero+1):
#     if  numero % x == 0:
#       cont += 1
#       print('\033[32m', end='')
#     else:
#       print('\033[31m', end='')
#     print('{}'.format(x), end=' ')
    
# print('\n') 

# if cont == 2:   
#     print('O número {} foi dividido {}x, por isso não é primo'.format(numero, cont))
# else:
#     print('O número {} e Primo'.format(numero))
# print('\n')

# print('-='*14)
# print('DESAFIO 53')
# print('-='*14) 
# # 53 - Faça um algoritmo que leia uma frase qualquer e diga se ela e palindromo desconsiderando os espaços 
# frase = input('Digite uma frase: ').strip().upper()
# frase = frase.split()
# junto = ''.join(frase)
# inverso = ''

# for letra in range(len(junto) -1, -1 ,-1):
#     inverso += junto[letra]
# if inverso == junto:
#     print('Essa Frase e um Palindromo: ')
# else:
#     print('Essa frase nao e um Palindromo')
# print('\n')

# print('-='*14)
# print('DESAFIO 54')
# print('-='*14) 
# # 54 - Faça um algoritmo que leia o ano de nascimento de sete pessoas. 
# # No final mostre a quantas pessoas nao atingiram a maioridade e quantas sao de maior

# maior = 0
# menor = 0
# for x in range(1,8):
#     data = int(input('Diga a data de Nascimento da {}° pessoa: '.format(x)))
#     if data >= 2003:
#         menor += 1
#     else:
#         maior += 1
# print('Temos {} pessoas de MENOR e {} pessoas de MAIOR'.format(menor, maior))
# print('\n')

# print('-='*14)
# print('DESAFIO 55')
# print('-='*14) 
# # 55 - Faça uum algoritmo que leia o peso de cinco pessoas. No final mostre qual foi o maior e qual o menor
# maior = 0
# menor = 0 

# for x in range(1,6):
#     peso = float(input('Digite o pero da {}° pessoa: '.format(x)))
#     if peso > maior:
#         maior = peso
#     else:
#         menor = peso
# print('O maior peso é {} e o menor peso é {}'.format(maior, menor))

# print('-='*14)
# print('DESAFIO 56')
# print('-='*14) 
# # 56 - Faça um algoritmo que leia o nome a idade e o sexo de 4 pessoas, 
# # no final mostre. A media de didade do grupo, qual e o nome do homem mais
# # velho quantas mulher tem menos de 20 anos

# media = 0 
# nomeHomem = ''
# mulher = 0
# idadeHomem = 0
# idadeMaior = 0

# for x in range (1,5):
#      nome = input('Digite seu nome: ')
#      idade = int(input('Digite sua idade: '))
#      print(Qual seu sexo:
#           [ M ] Masculino
#           [ F ] Feminino)
#      sexo = input('Esolha uma opção: ')
#      print('-'*14)
    
#      media = media + idade
    
#      if sexo == 'f' and idade <20:
#          mulher +=1
#      if sexo == 'm' and idade > idadeHomem:
#          nomeHomem = nome
#          idadeMaior = idade
#      else:
#         nomeHomem == ''
         
# media = media/4

# print('A media de idade do grupo e de {} anos'.format(media))
# if nomeHomem == '':
#     print('Nenhum homem foi cadastrado')
# else:
#     print('O homem mais velho tem {} anos e se chama {}'.format(idadeMaior, nomeHomem))
# print('Ao todo sao {} mulheres'.format(mulher))

