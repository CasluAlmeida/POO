lista = {'Nome': 'Lucas',
         'Idade': 21,
         'Altura': 1.80}

print(lista)

lista['Endereco'] = 'Avenida das Rosas'

print(lista)

lista.pop('Endereco')

print(lista)

notas = {'Lucas': 7.0,
         'Jorge': 8.0,
         'Matheus': 5.0,
         'Marcos': 9.0}

print(notas.items())

for nome, nota in notas.items():
    print(f'{nome} teve a nota {nota}')
