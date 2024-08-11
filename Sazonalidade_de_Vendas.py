from faker import Faker
import pandas as pd
import random
fake = Faker()

# Definir Parâmetros
Num_records = 1000
products = ['Camisa', 'Calça', 'Sapato', 'Bolsa', 'Relogio']
locations = ['Loja A', 'Loja B', 'Loja C', 'Loja D']

# Gerando dados fictícios
data = {
"Data da Venda": [fake.date_this_year() for _ in range(Num_records)],
"Produto": [random.choice(products) for _ in range(Num_records)],
"Quantidade": [random.randint(1, 10) for _ in range(Num_records)],
"Preço Unitário": [round(random.uniform(10.0, 100.0), 2) for _ in range(Num_records)],
"Localização": [random.choice(locations) for _ in range(Num_records)],
}
df_vendas = pd.DataFrame(data)

# Criar uma coluna com os meses para facilitar a analise
df_vendas['Mes'] = pd.to_datetime(df_vendas['Data da Venda']).dt.strftime('%B')

# Agrupa as vendas por mes e produto
vendas_mensais = df_vendas.groupby(['Produto', 'Mes'])['Quantidade'].sum().unstack().fillna(0)

# Identificar o melhor e o pior mês para cada produto
melhor_mes = vendas_mensais.idxmax(axis=1)
pior_mes = vendas_mensais.idxmin(axis=1)

# Extrair as quantidades correspondentes
def get_quantidade(data, produto, mes):
    return data.loc[produto, mes]

# Aplicar a função para obter as quantidades
quantidade_melhor_mes = [get_quantidade(vendas_mensais, prod, melhor_mes[prod]) for prod in vendas_mensais.index]
quantidade_pior_mes = [get_quantidade(vendas_mensais, prod, pior_mes[prod]) for prod in vendas_mensais.index]

# Criar um DataFrame final com as informações
resultados_df = pd.DataFrame({
    'Produto': vendas_mensais.index,
    'Melhor_Mês': melhor_mes.values,
    'Qntd_Melhor_Mês': quantidade_melhor_mes,
    'Pior_Mês': pior_mes.values,
    'Qntd_Pior_Mês': quantidade_pior_mes
})

print(resultados_df)

# Exportar a planilha csv
resultados_df.to_csv('Sazonalidade.csv', sep=',', index=False)
