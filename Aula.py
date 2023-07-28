#Lista com notas de aluno (Sem dicionários)

from time import sleep
lista = [] 
copia = [] 
b = ''

#Aqui lerá os nomes e acrescentará na lista "copia", e perguntará se quer continuar

while True: 	
    nome = str(input('\033[30mQual o primeiro nome? \033[m')).title().split()[0]
    nota1 = int(input('\033[30mQual a primeira nota? \033[m'))
    nota2 = int(input('\033[30mQual a segunda nota? \033[m'))
    nota3 = int(input('\033[30mQual a terceira nota? \033[m'))
    nota4 = int(input('\033[30mQual a quarta nota? \033[m')) 	
    lista.append(nome)
    lista.append(nota1)
    lista.append(nota2)
    lista.append(nota3)
    lista.append(nota4)
    copia.append(lista[:])
    lista.clear() 
    b = str(input('\033[36mQuer continuar?\033[m \033[32m[S/N]\033[m ')).upper().strip()[0]	
    if b in 'Nn': 		
        break 	
    else: 		
        while b not in 'Ss':
            print('\033[31mOpção inválida\033[m') 
            b = str(input('Quer continuar? [S/N] ')).upper().strip()[0] 

#Aqui fará um print de todos os elementos da lista com suas respectivas médias e enumerando cada um.

print('\033[32m=-\033[m'*15)
for c, v in enumerate(copia): 	
    print(f'{c+1}° Aluno: \033[30m{v[0]}\033[m. Média \033[30m{(v[1] + v[2] + v[3] + v[4]) / 4:.2f}\033[m')  
print('\033[32m=-\033[m'*15)

#Se quiser escolher ver as notas dos alunos, digitará a posição dele.

while True:
    info = int(input(f'''\033[30mVocê deseja ver as notas de algum aluno? 
Se sim digite a POSIÇÃO dele, se não digite\033[m \033[31m999\033[m: '''))
    if info == 999: 		
            break
    elif info > len(copia) or info < 1:
        print(f'\033[31mOpção inválida digite de 1 a {len(copia)}\033[m')
    else: 
        info = info - 1 	
        print(f'As notas de {copia[info][0]}, foram: \033[32m{copia[info][1]} , {copia[info][2]} , {copia[info][3]} e {copia[info][4]}\033[m')
        sleep(1) 	
    


