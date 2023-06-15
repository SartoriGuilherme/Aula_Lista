pessoas = ['João', 'Pedro', 'Carlos', 'Guilherme', 'Rafaela']

print(pessoas)

print('-------')

print(pessoas[0])

print('-------')

# len: comando para ver a quantidade de itens na lista
print(len(pessoas))

print('-------')

# Cria um range do tamanho da lista e usa a variável i como índice (posição) de cada elemento da lista
for i in range(len(pessoas)):
    print(pessoas[i])

print('---------Usar de preferência o código de baixo (ambas fazem a mesma função)---------')

# Percorre a lista de pessoas, atribuindo à variável p cada elemento na lista
for p in pessoas:
    print(p)

print('-------')

# Percorre a lista, obtendo para cada elemento, o valor na lista e a sua posição
for (i, p) in enumerate(pessoas):
    print(f'Nome: {p} na posição {i}')
