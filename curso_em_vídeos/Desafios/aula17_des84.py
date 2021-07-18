print('-='*14)
print('Desafio 84')
print('-='*14)
# 68 - Faça um programa que leia o nome e peso de varias pessoas 
# guarde tudo em uma lista. No final mostre:
# Quantas pessoas foram cadastradas, uma lista das pessoas mais pesadas, 
# uma lista com as pessoas mais leves

print( " CADASTRO DE PESSOAS: ")
pessoa = list()
cadastro = list() 
menor = 0
maior = 0
opcao = input("Deseja cadastrar um paciente? [S/N] ")

if opcao not in 'Ss':
    print("Cadastro Finalizado!")
    
else:
    
    while True:
        pessoa.append(input("Nome do paciente: "))
        pessoa.append(float(input("Digite seu peso: ")))
        
        if len(cadastro) == 0:
           menor = maior = pessoa[1]
        else:
             if (pessoa[1] >= maior):
                 maior = pessoa[1]
             if (pessoa[1]<= menor):
                menor = pessoa[1]
        cadastro.append(pessoa[:])
        pessoa.clear()

        res = str(input("Deseja cadastrar um paciente? [S/N]"))
        if res in 'Nn':
            break
        
    print('-='*30)
    print(f' A quantidade de pessoas cadastradas foram de {len(cadastro)}.')
    print(f' O maior peso foi de {maior}Kg. Peso de ', end='')
    for p in cadastro:
        if p[1] == maior:
            print (f'[{p[0]}]', end='')
    print()
    print(f' O menor peso foi de {menor}Kg', end='')
    for p in cadastro:
        if p[1] == menor:
            print(f'[{p[0]}]', end='')

       

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    