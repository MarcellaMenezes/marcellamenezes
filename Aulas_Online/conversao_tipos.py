
v = ['Banana', ['Tomate', 'Maçã'], ['Goiaba', 'Pêra']]
#for i in v:
#    if type(i) == list:
#        a = 'morango'  
#        sublista = i.append(a)
#        #sublista = i
#        #sublista.append(a)
#        print(sublista)

v = ['Banana', ['Tomate', 'Maçã'], ['Goiaba', 'Pêra']]
sublista = []
variavel_fruta = 'morango'
for i in v:
    # esse for está acessando todos os itens da lista v
    # supondo que naS sublistaS você quer colocar morango, você terá que criar um outro for ou acessar a sublista pelo index dela
    
    # aqui eu verifico se o tipo que tenho dentro da minha lista principal é um tipo lista, então vou saber que é uma nova lista, sendo sublista
    if type(i) == list:
        # usando extend, na minha variavel que foi declarada como lista vazia fora do for, eu vou extender essa lista com minhas sublistas
        sublista.extend(i)
        # logo mais vou adicionar o morango a minha nova lista
        sublista.append(variavel_fruta)
        
        # Dessa forma voce cria uma nova lista, agrupando as duas sublistas          
print(sublista)


# se voce quiser pegar apenas a primeira sublista
sublista = []
variavel_fruta = 'morango'
for i in v:
    if type(i) == list:
        sublista.extend(i)
        sublista.append(variavel_fruta)
        # com ajuda do break eu vou parar o for no primeiro loop, quando ele encontrar a primeira sublista
        break
    
print(sublista)

# ou se vc tem definido o index de onde vai pegar
sublista=v[1]
sublista.append('morango')
print(sublista)

# usando lambda
sublista = []
sublista = filter(lambda sub: type(sub)== list, v)
vetorsub = list(sublista)
print(vetorsub)

