from functools import reduce
lista = [100, 248.90, 88, 124.90]

def desconto(preco):
    return preco * (1 - 0.1)

#1 - Dada uma lista com n valores, aplicar a função de desconto usando map()
result = map(lambda x: desconto(x),lista)
result = list(result)
print(result)

result = map(desconto,lista)
result = list(result)
print(result)


#2 - Retornar os valores maiores que 100, usando filter()
result = filter(lambda x: x>100,lista)
result = list(result)
print(result)

#3 - Somar todos os valores da lista usando reduce()
result = reduce(lambda x, y: x+y, lista, 0)
print(result)