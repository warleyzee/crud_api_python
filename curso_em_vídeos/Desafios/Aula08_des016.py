# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 19:22:32 2021

@author: WarleY

"""

import math
# Crie um programa que lea um numero real pelo tecladoe mostra na tela a sua 
# porção inteira. EX: 6.127 deve retornar o valor 6

print ('DESAFIO 016')

num = float(input('Digite um numero float: '))
print('O numero {} tem o valor interio de: {}'.format(num,math.floor(num)))

print ('DESAFIO 017')
# Faca um algoritmo que leia o comprimeto do Cateto oposto e adjancente de um triangulo
# e calculo a hipotenusa

import math

oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Compirmento do cateto adjacente: '))
hipotenusa = float(math.hypot(oposto, adjacente))

print('A hipotenusa e: {:.2f}'.format(hipotenusa))

print ('DESAFIO 018')
# Faça um algoritmo que leia um angulo e mostro na tela os valores de 
# seno, cosseno e tangente
import math

angulo = float(input('Digite um angulo: '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O valor de {}° é equivalente a {:.2f} seno'.format(angulo, seno))
print('O valor de {}° é equivalente a {:.2f} cosseno'.format(angulo, cosseno))
print('O valor de {}° é equivalente a {:.2f} tangente'.format(angulo, tangente))


print ('DESAFIO 019')
#Um professor quer sortear um dos seus quadros alunos para apagar o quadro.
# Faça um algortmo leia o nome do aluno e escreva o nome escolhido 

import random

alunos = []

for x in range(4):
    nome = input('Digite o nome do aluno: ')
    alunos.append(nome)
    
print('O aluno escolhido foi: {}'.format(random.choice(alunos)))

print ('DESAFIO 020')
# Um professor quer sortear a ordem de apresentação de trabalho dos alunos
# Faça um Algoritmo que lea o nome dos quatro alunos e mostra na ordem sorteada 

import random

alunos = []

for x in range(4):
    nome = input('Digite o nome do aluno: ')
    alunos.append(nome)
    
random.shuffle(alunos)
    
print('O aluno escolhido foi: {}'.format(alunos))


print ('DESAFIO 021')
# Faça um algoritmo que repoduza um audio em MP3

# instalar o modulo pygame pelo console <pip install pygame==2.0.0.dev6>

import pygame

pygame.mixer.init()

pygame.init()                 # essa inicialização nos meus testes, não foi necessária

pygame.mixer.music.load('teste.mp3')

pygame.mixer.music.play()

pygame.mixer.music.set_volume(1)

x = input('digite algo para encerrar ...')


























