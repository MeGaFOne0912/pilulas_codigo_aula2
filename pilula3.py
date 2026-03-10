import datetime
data_compra = input ('digite data da compra (dd/mm/aaaa):')
meses = int(input('Prazo da garantia: '))
data_inicial = datetime.datetime.strptime(data_compra,'%d/%m/%Y')
data_final = data_inicial + datetime.timedelta(days = meses * 30)
print(f'Garantia valida até {data_final.strftime('%d/%m/%Y')}')
print(f'Dia da semana: {data_final.strftime('%A')}')