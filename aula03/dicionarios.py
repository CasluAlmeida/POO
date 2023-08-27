cores = ('Azul', 'Verde', 'Vermelho', 'Amarelo')
print(type(cores))

print(cores)

tupla_s = ('valor',)

print(type(tupla_s))

# range(fim)  inicio = 0 e passo = 1
# range(inicio, fim)  passo = 1
# range(inicio, fim, passo)

list(range(8))

print(range)

interiros = [1, 25, 17, 58, 18, 51]

var = 17 in interiros
var_1 = 32 not in interiros

print(var)
print(var_1)

a, b, c, d, e, f = interiros

print(a, b, c, d, e, f)

print(*interiros)


def teste_desempacote(a, b, c, d, e, f):
    print(f'{a=} {b=} {c=}')
    print(f'{d=} {e=} {f=}')


teste_desempacote(interiros[0], interiros[1], interiros[2], interiros[3], interiros[4], interiros[5])

teste_desempacote(*interiros)

