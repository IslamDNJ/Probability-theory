import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Задание 2
# Выгрузка данных из файла
data = pd.read_csv('marketing_campaign.csv', sep='\t')

df = pd.DataFrame(data)

# Создать новую колонку Total_Spending
df['Total_Spending'] = df['MntWines'] + df['MntFruits'] + df['MntMeatProducts'] + df['MntGoldProds']

# Вычислить медиану Total_Spending
median_spending = df['Total_Spending'].median()

# Создать колонку Spending_Group
df['Spending_Group'] = np.where(df['Total_Spending'] > median_spending, 1, 0)

# Указать только числовые колонки
numeric_cols = ['Income', 'MntWines', 'MntFruits', 'MntMeatProducts', 'MntGoldProds']

# Убедиться, что все столбцы числовые
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Удалить строки с NaN в числовых колонках
df = df.dropna(subset=numeric_cols)

# Группировать и вычислять средние значения
group_means = df.groupby('Spending_Group')[numeric_cols].mean()

print("Средние значения по группам (Spending_Group):")
print(group_means)

# Визуализация
plt.figure(figsize=(10, 6))
group_means.plot(kind='bar', color=['skyblue', 'salmon'])
plt.title("Средние значения по группам расходов (Spending_Group)")
plt.xlabel("Группа расходов")
plt.ylabel("Средние значения")
plt.xticks([0, 1], ['Низкие расходы', 'Высокие расходы'], rotation=0)
plt.legend(title='Категории', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
