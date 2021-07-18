# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 19:57:54 2021

@author: WarleY
"""

txt = input('Digite algo: ')
print("Esse é o o tipo primito ", type(txt))
print('É um numero ',txt.isalnum())
print('E uma palavra',txt.isalpha())
print('É um numero decimal ',txt.isdecimal())
print('É um titulo ', txt.istitle())
print('Possui espaço',txt.isspace())
print('Não sei o que é isso ',txt.isidentifier())