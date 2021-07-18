# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 23:58:56 2021

@author: WarleY
"""
print(':='*12)
print('Desafio 36')
print(':='*12)
# 36 - Faça um algoritmo para aprovar um empresitmo bancario
# para a compra de uma casa. O algoritmo vai perguntar o valor da casa,
# o salario do comprador e em quantos anos ele vai pagar.
# Calculo o valor de cada prestação mensal sabendo que ela nao pode exceder
# 30% do salario ou entao o emprestimo e negado

casa = float(input('Qual o valor da casa?  '))
salario = float(input('Qual o seu salario? '))
anos = float(input('Quantos anos pretende pagar a casa? '))

meses = anos * 12
parcela = (30*salario)/100
valor = casa/meses

if valor > parcela:
    print('Emprestimo negao')
    print('O valor maximo do seu emprestimo e de R${}, para essa simulação o emprestimo e de R${:.2f}'.
          format(parcela, valor))
else:
    print('Emprestimo aprovado')
print('\n')

print(':='*12)
print('Desafio 37')
print(':='*12)
# 37 - Faça um algoritimo que leia um numero interio qualquer e peça para o usuario
# escolher qual sera a base de conversação, 1 binario, 2 octal,3 hexadecimal

numero = int(input('Digite um numero: '))
print (''' Escolha uma opção 
      [ 1 ] Converter para BINARIO
      [ 2 ] Converter para OCTAL
      [ 3 ] Converter para HEXADECIMAL''')

opcao = int(input('Escolha uma opção a cima: '))

if opcao == 1:
    print('{} Convertido para BINARIO e {}'.format(numero,bin(numero)))
elif opcao == 2:
    print('{} Convertido para OCTAL e {}'.format(numero, oct(numero)))
else:
    print('{} Convertido para HEXADECIMAL e {} '.format(numero,hex(numero)))
print('\n')

print(':='*12)
print('Desafio 38')
print(':='*12)
# 38 - Faça um algoritmo que leia dois numeros interios e compraos mostrando
# na tela a mesnsagem, o primeiro valor e maior o segundo valor e menor nao
# existe valor maior os dos sao iguais

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))

if num1 > num2:
    print('O numero um e maior que o numero dois')
elif num1 < num2:
    print('O numero dois e maior que o numero um')
else:
    print('Os numero sao do mesmo valor')
print('\n')

print(':='*12)
print('Desafio 39')
print(':='*12)
# 39 - Faça um algoritmo que leia o ano de nascimento de um jovem e informe,
# de acordo com a idade, se ele ainda vai se alisart no exercito, se e a hora
# de se alistar, se ja passou do tempo do alistamento, o algoritmo tmb devera
# mostar quanto tempo que falta ou passou do prazo

ano = int(input('Digite seu ano de nascimento: '))
idadeMin = 18
idadeMax = 45

calculo = 2021 - ano

if calculo < 18:
    print('Voce tem {} anos, NÃO esta na hora de se alistar'.format(calculo))
    calculo = 18 - calculo 
    print('Ainda falta {} anos para poder se alistar'.format(calculo))
    
elif calculo <= 45:
    print('Voce tem {} anos, esta na hora de voce se alistar'.format(calculo))
    
elif calculo > 45:
    print('Não precisa mais se alistar, voce tem {} anos'.format(calculo))
    calculo =  calculo - 45
    print('Ja passou {} anos do alistamento obrigatorio'.format(calculo))

else:
    print('Idade invalida')
print('\n')

print(':='*12)
print('Desafio 40')
print(':='*12)
# 40 - Faça um algoritmo que leia duas notas de cada aluno e calcule sua media, 
# mostrando a mensagem no final, de acordo com a media, 5 reprovado, 5 a 6,9 
# recuperação, >7 aprovado

nota = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota+nota2)/2

if media <= 5:
    print('Somando suas notas sua medio foi {}, infelimente voce esta REPROVADO'.format(media))
elif media < 7:
    print('Sua media foi {}, voce esta de RECUPERAÇÂO'.format(media))
else:
    print('Sua media foi {}, PARABENS VOCE PASSOU'.format(media))
print('\n')

print(':='*12)
print('Desafio 41')
print(':='*12)
# 41 - Faça um algoritmo que leia o ano de nacimento de um atleta e mostra 
# sua categoria de acordo com a idade, 9 anos mirim, 14 anos infantil, 19 junior,
# 20 senior. >20 master
idade = int(input('Digite o ano de nascimento: '))
categoria = 2021 - idade

if categoria <= 9:
    print('Voce tem {} anos, sua categoria e a Mirim'.format(categoria))
elif categoria <= 14:
    print('Voce tem {} anos, sua categoria e a Infantil'.format(categoria))
elif categoria <= 19:
    print('Voce tem {} anos, sua categoria e a Junior'.format(categoria))
elif categoria == 20:
    print('Voce tem {} anos, sua categoria e a Senior'.format(categoria))
else:
    print('Voce tem {} anos, sua categoria e a Master'.format(categoria))
print('\n')

print(':='*12)
print('Desafio 43')
print(':='*12)
# 43 - Faça um algoritmo que calcule o IMC e mostre a mensagem, 18.5
# abaixo do peso, 18,5 a 25 peso ideal, 25 a 30 sobrepeso, 30 a 40 
# obesidade, >40 obsidade morbida
altura = float(input('Qual a sual altra (m): '))
peso = float(input('Qual seu peso (kg): '))

imc = peso / (altura**2)

if imc <= 18.5:
    print('Seu IMC e de {:.2f}'.fomat(imc))
    print('Voce esta a baixo do peso ideal')
elif imc <= 25:
    print('Seu IMC e de {:.2f}'.format(imc))
    print('Parabens voce esta no peso ideal')
elif imc <=40:
    print('Seu IMC e de {:.2f}'.format(imc))
    print('Cuidado voce esta com Sobrepeso')
else:
    print('Seu IMC e de {:.2f}'.format(imc))
    print('Procure uma ajuda, voce esta muuuuuuito gordo')
print('\n')

print(':='*12)
print('Desafio 44')
print(':='*12)
# 44 - Faça um algoritmo que calcule o valor a ser pago por um produto
# considerando o seu preço normal e condição de pagamento. 
# A vista dinheiro ou cheque 10% de desconto, a vista no cartao 5% 
# de desconto, em ate 2x no cartao preço normal, 3x ou mais no cartao 20 % de juros 
preco = float(input('Preço das compras: R$'))
print(''' FORMA DE PAGAMENTO 
      [ 1 ] a vista com dinheiro ou cheque
      [ 2 ] a vista Cartão
      [ 3 ] 2x no Cartao
      [ 4 ] 3x ou mais no Cartao ''')
opcao = int(input('Qual a forma de Pagamento: '))
print('\n')
if opcao == 1:
    valor = (10*preco)/100
    total = preco - valor
    
    print('Sua compra e de R${}.00 vai custar R${} no final'.format(preco,total))
    
elif opcao == 2:
    valor = (5*preco)/100
    total = preco - valor
    print('Sua compra de R${}.00 vai custar R${} no final'.format(preco,total))
    
elif opcao == 3:
    print('Sua compra nao tem desconto, valor total R${}'.format(preco))
    
elif opcao == 4:
    parcelas = int(input('quantas parcelas: '))  
    valor = (20*preco)/100
    total = preco + valor
    totalParcela = total/parcelas
    
    print('Sua comprar sera  parcelada em {}x de R${} COM JUROS'.format(parcelas,totalParcela))
    print('Sua compra  de R$ {}vai custar R${} no final'.format(preco,total))
    
print('\n')

print(':='*12)
print('Desafio 44')
print(':='*12)
# 45 - Faça um algoritmo que faça o computador jogar jokenpo com voce

import random 
from time import sleep

itens = ['Pedra', 'Papel', 'Tesoura']
ia = random.randint(0,2)

print('''SUAS OPÇÔES
      [ 0 ] Pedra
      [ 1 ] Papel
      [ 2 ] Tesoura
      ''')
      
jogador = int(input('Qual a sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!')

print('-='*12)
print('O computador escolher {}'.format(itens[ia]))
print('O Jogador escolheu {}'.format(itens[jogador]))
print('-='*14)

if jogador == 0 and ia == 0:
    print('Os dois escolheram PEDRA. EMPATE')
elif jogador == 1 and ia == 0:
    print('O Jogador ganhou com PEDRA!!!')
elif jogador == 2 and ia == 0:
    print('O Computador vencel com PEDRA')
elif jogador == 1 and ia == 1:
    print('Empate, os dois jogaram PAPEL')
elif jogador == 1 and ia == 0:
    print('O computador vencel com PAPEL')
elif jogador == 2 and ia == 1:
    print('O Jogador ganhou com TESOURA')
elif jogador == 2 and ia == 2:
    print('Empate, os dois jogaram TESOURA')
elif jogador == 1 and ia == 2:
    print('O Computador Venceu com TESOURA')
   

























