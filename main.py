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

# Exportar a planilha csv
df_vendas.to_csv('dados_vendas.csv', sep=',', index=False)
