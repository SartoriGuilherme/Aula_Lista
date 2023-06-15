pessoas = []

for i in range(5):
    nome = input(f'Informe o nome da pessoas {i}: ')
    pessoas.append(nome)
    print(f'Tamanho atual da lista: {len(pessoas)}')

# Obtém posição de um item na lista
pos_maria = pessoas.index('Maria')
print(f'Maria está na posição {pos_maria}')
