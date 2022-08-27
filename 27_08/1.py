# ------------ Tipos --------------------
nome = 'Marcella'
idade = 23.10
destra = True

print('Nome = '+str(type(nome)) + '\nIdade = '+str(type(idade)) + '\nDestra = '+ str(type(destra)))
print('Nome = '+nome + '\nIdade = '+str(idade) + '\nDestra = '+ str(destra))

# ------------ Comentários ------------
'''
oi
'''
# ------------ Operadores ------------
print('\nOperadores')

print (1 + 2)   # soma
print (1 - 2)   # subtração
print (1 / 2)   # divisão
print (1 // 2)  # Divisão Inteira
print (1 % 2)   # Resto da Divisão
print (27 ** (1/3))  # Exponenciação

# ------------ Condicionais ------------ <=, >=, ==, !=
print('\nCondicionais')

if  1 == '1':
    print ('São iguais')
else:
    print ('Não são iguais')  
    
if 1 == int('1'):
    print ('São iguais')
else:
    print ('Não são iguais')  
    
 # Operador de atribuição *=, /=, +=, -=
print('\nOperador de atribuição')

a = 3
a **= 4
print (a) 

a /= 9
print (a) 

a %= 4
print (a)

# ----- Operadores Lógicos
lista = [1, 2, 3, 4] 
if 7 not in lista:
    print('não tem na lista')

print (7 == 7 or 6 == 5)
print (7 == 7 and 6 == 5)
print (not (7 == 7 and 6 == 5))