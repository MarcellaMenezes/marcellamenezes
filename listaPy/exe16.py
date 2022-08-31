valor_emprestimo = float(input('Informe o valor do empréstimo: '))
taxa             = int(input('Informe o valor da taxa: '))
qtd_meses        = int(input('Informe a quantidade de meses para pagamento: '))

valor_final = valor_emprestimo + (valor_emprestimo * (taxa/100) * qtd_meses)

print('O valor final do empréstimo será: ', valor_final)
