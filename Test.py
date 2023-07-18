#test de github, código em python. Manipulação de lista composta.

lista = []
dell = []
cont = maior = menor = 0
while True:
    lista.append(str(input('Nome: ').title()))
    lista.append(int(input('Peso: ')))
    if len(dell) == 0:
        maior = menor = lista[1]
    else:
        if maior < lista[1]:
            maior = lista[1]
        if menor > lista[1]:
            menor = lista[1]
    dell.append(lista[:])
    lista.clear()
    cont += 1
    c = str(input('Quer Continuar? [S/N] ')).upper().strip()
    while c not in 'NnSs': 
        print('Opção invalida')        
        c = str(input('Quer Continuar? [S/N] ')).upper().strip()
    if c in 'Nn':
        break
print(f'Ao todo, você cadastrou {cont} pessoas.')
print(f'o Menor peso foi "{menor}"" de', end=' ')
for p in dell:
    if p[1] == menor:
        print(f'{p[0]}', end = '... ')
print()
print(f'O Maior peso foi "{maior}" de', end=' ')
for p1 in dell:    
    if p1[1] == maior:
        print(f'{p1[0]}', end = '... ')