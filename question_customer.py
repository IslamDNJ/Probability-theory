import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('marketing_campaign.csv', sep='\t')

# Задание 1
# Средние траты на каждый тип товара
avg_spending_per_category = df[['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']].mean()
print("Средние траты на каждый тип товара:\n")
print(avg_spending_per_category)

# Визуализация
plt.figure(figsize=(10, 6))
avg_spending_per_category.sort_values().plot(kind='bar', color='skyblue')
plt.title("Средние траты на каждый тип товара")
plt.ylabel("Средние траты")
plt.xlabel("Категории товаров")
plt.xticks(rotation=45)
plt.show()

# Товар с наибольшими тратами
max_category = avg_spending_per_category.idxmax()
print(f"\nАкцент следует сделать на товаре: {max_category}")

# Задание 2
# Расчет среднего возраста
current_year = 2024
df['Age'] = current_year - df['Year_Birth']
mean_age = df['Age'].mean()
print(f"Средний возраст покупателя: {mean_age:.1f} лет")

# Корреляция между возрастом и тратами
age_corr = df[['Age', 'MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']].corr()
print("\nКорреляция возраста с категориями трат:")
print(age_corr['Age'])

# Визуализация зависимости
plt.figure(figsize=(10, 6))
sns.heatmap(age_corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Корреляция возраста с категориями трат")
plt.show()

# Задание 3
# Суммарные траты и количество детей + иждивенцев
df['Total_Children'] = df['Kidhome'] + df['Teenhome']
df['Total_Spending'] = df[['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']].sum(axis=1)

# Средние траты по количеству детей
avg_spending_children = df.groupby('Total_Children')['Total_Spending'].mean()
print("\nСредние траты в зависимости от количества детей и иждивенцев:")
print(avg_spending_children)

# Визуализация
plt.figure(figsize=(8, 5))
avg_spending_children.plot(kind='bar', color='orange')
plt.title("Средние траты в зависимости от количества детей и иждивенцев")
plt.xlabel("Количество детей и иждивенцев")
plt.ylabel("Средние траты")
plt.show()

# Задание 4
# Средние траты по категориям товаров для каждого уровня образования
education_spending = df.groupby('Education')[['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']].mean()

print("Средние траты в зависимости от уровня образования:")
print(education_spending)

# Визуализация
education_spending.plot(kind='bar', figsize=(12, 6))
plt.title("Средние траты по категориям товаров в зависимости от образования")
plt.ylabel("Средние траты")
plt.xlabel("Образование")
plt.xticks(rotation=45)
plt.legend(title="Категории товаров")
plt.show()

# Задание 5
# Средние траты на золото по семейному положению
marital_gold_spending = df.groupby('Marital_Status')['MntGoldProds'].mean()

print("\nСредние траты на покупку золота в зависимости от семейного положения:")
print(marital_gold_spending)

# Визуализация
plt.figure(figsize=(8, 5))
marital_gold_spending.sort_values().plot(kind='bar', color='gold')
plt.title("Средние траты на золото по семейному положению")
plt.ylabel("Средние траты на золото")
plt.xlabel("Семейное положение")
plt.xticks(rotation=45)
plt.show()

# Задание 6
# Анализ зависимостей
df['Discount_Rate'] = df['NumDealsPurchases'] / df['NumWebPurchases']
discount_relation = df[['NumWebPurchases', 'NumDealsPurchases']].corr()

print("\nКорреляция между покупками на сайте и покупками со скидкой:")
print(discount_relation)

# Визуализация
sns.scatterplot(data=df, x='NumWebPurchases', y='NumDealsPurchases', color='purple')
plt.title("Зависимость покупок на сайте и покупок со скидкой")
plt.xlabel("Количество покупок на сайте")
plt.ylabel("Количество покупок со скидкой")
plt.show()

# Задание 7
# Жалобы и траты
complaint_spending = df.groupby('Complain')['Total_Spending'].mean()

print("\nСредние траты клиентов в зависимости от жалоб:")
print(complaint_spending)

# Визуализация
plt.figure(figsize=(6, 4))
sns.barplot(x=complaint_spending.index, y=complaint_spending.values, palette="coolwarm", hue=complaint_spending.index, dodge=False)
plt.legend([], [], frameon=False)
plt.title("Связь между жалобами и средними тратами")
plt.xlabel("Жалоба (0 - Нет, 1 - Да)")
plt.ylabel("Средние траты")
plt.show()

# Задание 8
# Анализ предложений
df['Accepted_Last'] = df['AcceptedCmp5'] == 1
accepted_last_spending = df.groupby('Accepted_Last')['Total_Spending'].mean()

print("\nСредние траты в зависимости от принятия предложения в последней компании:")
print(accepted_last_spending)

# Визуализация
sns.barplot(x=accepted_last_spending.index, y=accepted_last_spending.values, palette="magma", hue=accepted_last_spending.index, dodge=False)
plt.legend([], [], frameon=False)
plt.title("Траты клиентов в зависимости от принятия предложения в последней компании")
plt.xlabel("Приняли предложение в последней компании (True/False)")
plt.ylabel("Средние траты")
plt.show()