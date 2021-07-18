# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 20:39:50 2021

@author: WarleY
"""

print(' Desafio 06')
num1 = int(input("Digite um numero: "))

print('O numero digitado foi {}, \n seu sucessor é  {}  \n e seu antecessor é {}'
      .format(num1, num1+1, num1-1))

print('\n')
print('Desafio 07')

num1 = int(input('Digite um numero: '))
print('o numero digitado foi {}, \n O dobro dele é {}, \n O triplor é{}, E sua raiz quadrada é {}'
      .format(num1,num1*2, num1*3,num1**1/2))

print('\n')
print('Desafio 08')

num2 = int(input('Digite alguma metragem:'))
print('O valor em cm de {} é {}cm \n E em quilometragem é {}Km '
      .format(num2, num2*1000, num2/1000))

print('\n')
print('Desafio 09')

num3 = int(input("Digite um valor a ser mutiplicado: "))
mult = 0
for x in range(11):
    
    print('{} * {} = {}'.format(mult+x, num3, num3*x))

print('\n')
print('Desafio 10')

valor = float(input('Quanto voce tem na carteira: '))
dolar = float(input('Insira o valor do dolar: '))

print('Voce pode comprar {} dolare com essa valor'.format(valor//dolar))


print('\n')
print('Desafio 11')

largura = int(input('Digite a largura da parede: '))
altura = int(input('Digite a altura da parede: '))
diametro = largura * altura

print('O diametro da parede é de {}, sera necessarias {}L de tinta'.
      format(diametro, (diametro/2)))

print('\n')
print('Desafio 12')

produto = input('Qual Produto voce deseja: ')
valorProduto = float(input('Qual o valor do Produto: '))
desconto = 5.0
calcDesconto = (desconto/100)*valorProduto
    
print('{} tem o desconto de  R${}, sai pelo valor de R$ {}'
      .format(produto, calcDesconto, valorProduto-calcDesconto))


print('\n')
print('Desafio 13')

nome = input('Qual o nome do funcionario: ')
salario = float(input('Qual o salario do {}: '.format(nome)))
aumento = (salario/100)*15

print('{} ganhao 15% de aumento e seu salrio agora é R${}'
      .format(nome, salario+aumento))

























