# int: 1 2 3 -5 -7 789

# float: 3.1 7.4 8.89 0.45 -8.74

# bool: True False

# str: 'olá' "olá" '''olá''' """olá"""

idade = 22
peso = 135.2
altura = 180
nome = 'Lucas Almeida'
concat = f'O {nome} tem {idade} anos de idade, pesa {peso}KG e tem {altura} de altura'

print(concat)

texto = '''Olá mundo
escrito em
várias linhas'''

print(texto)

n1 = 22
n2 = 8.4
cidade = "Barcelona"
isTrue = True

print(type(n1))
print(type(n2))
print(type(cidade))
print(type(isTrue))

print('\n')


def primeira_funcao(p1, p2):
    return p1 + p1


resultado = primeira_funcao(5, 12)
print(resultado)


# Sempre utilizar return nas funções e métodos
def primeira_funcao_print(n1, n2):
    print(n1 + n2)


resultado2 = primeira_funcao_print(5, 12)
print(resultado2)

