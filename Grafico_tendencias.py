import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from faker import Faker
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

# Adicionar coluna com o nome do mês da venda
df_vendas['Mês'] = df_vendas['Data da Venda'].dt.strftime('%B')

# Mapeamento dos meses para português
meses_map = {
    'January': 'Janeiro', 'February': 'Fevereiro', 'March': 'Março',
    'April': 'Abril', 'May': 'Maio', 'June': 'Junho', 'July': 'Julho',
    'August': 'Agosto', 'September': 'Setembro', 'October': 'Outubro',
    'November': 'Novembro', 'December': 'Dezembro'
}
df_vendas['Mês'] = df_vendas['Mês'].map(meses_map).fillna(df_vendas['Mês'])

# Agrupar as vendas por produto e mês
vendas_mensais = df_vendas.groupby(['Produto', 'Mês'])['Quantidade'].sum().unstack().fillna(0)

# Agrupar vendas totais por mês
vendas_totais_mensais = df_vendas.groupby('Mês')['Quantidade'].sum()
vendas_totais_mensais = vendas_totais_mensais.reindex(list(meses_map.values()))

# Criar gráficos
plt.figure(figsize=(14, 6))

# Gráfico de Tendências de Vendas por Produto ao Longo do Ano
plt.subplot(1, 2, 1)
sns.lineplot(data=vendas_mensais.T, palette='tab10')
plt.title('Tendência de Vendas por Produto ao Longo do Ano')
plt.xlabel('Mês')
plt.ylabel('Quantidade Vendida')
plt.xticks(rotation=45)
plt.legend(title='Produto')

# Gráfico de Totais de Vendas Mensais
plt.subplot(1, 2, 2)
sns.barplot(x=vendas_totais_mensais.index, y=vendas_totais_mensais.values, palette='viridis')
plt.title('Totais de Vendas Mensais')
plt.xlabel('Mês')
plt.ylabel('Quantidade Total Vendida')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
