import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('marketing_campaign.csv', sep='\t')

# 1.1 Разделение по образованию
education_groups = df.groupby('Education')[numeric_cols].mean()
print("Средние показатели по группам образования:")
print(education_groups[['Income', 'Total_Spending', 'MntFruits', 'MntWines']])

# Визуализация можно убрать hue='Total_Spending' для точных значений, но будут ошибки
plt.figure(figsize=(12, 6))
sns.barplot(x='Education', y='Total_Spending', data=df, palette="viridis", legend=False, hue='Total_Spending')
plt.title("Общие траты по уровню образования")
plt.xlabel("Образование")
plt.ylabel("Средние траты")
plt.xticks(rotation=45)
plt.show()

# 1.2 Разделение по уровню заработка
income_bins = pd.qcut(df['Income'], q=4, labels=["Low", "Medium", "High", "Very High"])
df['Income_Group'] = income_bins

income_groups = df.groupby('Income_Group', observed=False)[numeric_cols].mean()
print("\nСредние показатели по группам дохода:")
print(income_groups[['Total_Spending', 'MntFruits', 'MntMeatProducts', 'MntGoldProds']])

# Визуализация можно убрать hue='Total_Spending' для точных значений, но будут ошибки
plt.figure(figsize=(10, 6))
sns.barplot(x='Income_Group', y='Total_Spending', data=df, palette="coolwarm", legend=False, hue='Total_Spending')
plt.title("Общие траты по уровню дохода")
plt.xlabel("Группа дохода")
plt.ylabel("Средние траты")
plt.show()

# 1.3 Разделение по семейному статусу
marital_groups = df.groupby('Marital_Status', observed=False)[numeric_cols].mean()
print("\nСредние показатели по семейному статусу:")
print(marital_groups[['Total_Spending', 'MntWines', 'MntFruits', 'Complain']])

# Визуализация можно убрать hue='Total_Spending' для точных значений, но будут ошибки
plt.figure(figsize=(12, 6))
sns.barplot(x='Marital_Status', y='Total_Spending', data=df, palette="magma", legend=False, hue='Total_Spending')
plt.title("Общие траты по семейному статусу")
plt.xlabel("Семейный статус")
plt.ylabel("Средние траты")
plt.xticks(rotation=45)
plt.show()