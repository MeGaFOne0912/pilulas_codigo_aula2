import math
#entradas leituras
assinantes = int(input('Digite a Qtd de assinantes: '))
mensalidade = float(input('Digite o Valor da Mensalidade: '))
taxa = float(input('Digite a Taxa de Crescimento mensal(%):'))
meses = int(input('Digite a qtd de meses da projeção: '))
#processamento
assinantes_finais = assinantes * math.pow((1 + taxa/100), meses)
receita_final = assinantes * mensalidade 
#saida
print (f'Assinantes Estimados: {assinantes_finais:.0f}')
print(f'Receita Estimada: R${receita_final:.2f}')