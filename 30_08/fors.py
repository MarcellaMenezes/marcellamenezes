
lista = ['Banana', 5, 'Tomate', 'Maçã', 7,'Goiaba', 'Pêra']

#For ser enumerate
for elemento in lista:
    print(elemento)

#For com enumerate
for index, elemento in enumerate(lista):
    print(f'lista[{index}] = {elemento}')

#For com range    
for indice in range(len(lista)):
    print(f'lista[{index}] = {lista[indice]}')