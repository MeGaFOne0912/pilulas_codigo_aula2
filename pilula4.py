import statistics as st
lote1 = float(input('Produção Lote 1: '))
lote2 = float(input('Produção Lote 2: '))
lote3 = float(input('Produção Lote 3: '))
media = st.mean((lote1, lote2, lote3))
desvio= st.stdev((lote1, lote2, lote3))
print(f'Media{media:.2f}')
print(f'Desvio padrão{desvio:2f}')