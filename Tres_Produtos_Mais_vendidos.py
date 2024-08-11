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

# Somando a quantidade vendida por produto
total_vendido_por_produto = df_vendas.groupby('Produto', as_index=False)['Quantidade'].sum()

# Ordena do produto mais vendido para o menos vendido
produtos_mais_vendidos_ordenados = total_vendido_por_produto.sort_values(by='Quantidade',ascending=False)

#Seleciona os tres produtos mais vendidos
tres_mais_vendidos = produtos_mais_vendidos_ordenados.head(3)

print(tres_mais_vendidos)

# Exportar a planilha csv
tres_mais_vendidos.to_csv('tres_produtos_mais_vendidos.csv', sep=',', index=False)