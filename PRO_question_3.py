import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Пример вашего DataFrame
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

# 1. Анализ коэффициентов корреляции между расходами
correlation_matrix = df[numeric_cols].corr()

# Визуализация корреляционной матрицы
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', vmin=-1, vmax=1)
plt.title("Корреляция между категориями расходов")
plt.tight_layout()
plt.show()

# 2. Распределение Total_Spending по группам
plt.figure(figsize=(10, 6))
sns.boxplot(x='Spending_Group', y='Total_Spending', data=df, palette='Set2')
plt.title("Распределение Total_Spending по группам")
plt.xlabel("Группа концентраций")
plt.ylabel("Общие расходы")
plt.xticks([0, 1], ['Низкие расходы', 'Высокие расходы'], rotation=0)
plt.tight_layout()
plt.show()

# 3. Анализ дохода по группам
plt.figure(figsize=(10, 6))
sns.boxplot(x='Spending_Group', y='Income', data=df, palette='Set1')
plt.title("Распределение доходов по группам расходов")
plt.xlabel("Группа расходов")
plt.ylabel("Доход")
plt.xticks([0, 1], ['Низкие расходы', 'Высокие расходы'], rotation=0)
plt.tight_layout()
plt.show()

# 4. Анализ среднего уровня трат по категориям
category_means = df[numeric_cols].mean()

plt.figure(figsize=(10, 6))
category_means.plot(kind='bar', color='skyblue')
plt.title("Средний уровень трат по категориям")
plt.xlabel("Категории")
plt.ylabel("Среднее значение расходов")
plt.tight_layout()
plt.show()

# Вывод коэффициентов корреляции
print("Коэффициенты корреляции между категориями расходов:")
print(correlation_matrix)
