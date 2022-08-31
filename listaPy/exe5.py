# 5) Resolva estes problemas em Python, guardando os valores e seus resultados em
# variáveis diferentes.

# a. Calcule a área de um quadrado cujo lado seja 2 cm.
lado = 2
print(f'Área = {lado**2}')

# b. Uma mala custa R$120,00. Esta recebeu 5% de desconto. Quanto você irá pagar por ela.
print(f'Valor da mala com desconto = {120 - 120*(5/100)}')

# c. Um carro está viajando a uma velocidade média de 100 Km/h, o trecho de viagem será 200 Km. Quantas horas irá demorar a viagem.
# v = ds/dt => dt = ds/v
print(f'O carro demorará {200/100} horas')

# d. João tem 2 pirulitos, Maria 3 pirulitos e Sofia 1 pirulito. Calcule o total de pirulitos e sua média.
totalPirulitos = 2+3+1
print('A média de pirulitos por pessoa é = '+str(totalPirulitos/3))

# e. Davi tem 13 anos e sua irmã tem 7 anos. Guarde na variável eh_mais_velho a verificação se a idade de Davi é maior que a idade de sua irmã.
Davi = 13
Irma = 7
eh_mais_velho = Davi > Irma
print(eh_mais_velho)