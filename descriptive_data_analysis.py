import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка данных
df = pd.read_csv('marketing_campaign.csv', sep='\t')

# Анализ распределения числовых переменных
num_cols = df.select_dtypes(include=[np.number]).columns
for col in num_cols:
    plt.figure(figsize=(10, 5))
    sns.histplot(df[col], kde=True, bins=30, color='blue')
    plt.title(f"Распределение {col}")
    plt.xlabel(col)
    plt.ylabel("Частота")
    plt.show()

# Анализ категориальных переменных с визуализацией
cat_cols = df.select_dtypes(include=['object']).columns
for col in cat_cols:
    plt.figure(figsize=(10, 5))
    sns.countplot(data=df, x=col, hue=col, order=df[col].value_counts().index, palette="viridis", legend=False)
    plt.title(f"Распределение значений для {col}")
    plt.xlabel(col)
    plt.ylabel("Частота")
    plt.xticks(rotation=45)  # Поворот подписей для удобства чтения
    plt.show()


# Попытка преобразовать столбец 'Dt_Customer' в datetime с обработкой ошибок
try:
    df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], format='%d-%m-%Y', errors='coerce')
except Exception as e:
    print(f"Ошибка преобразования Dt_Customer: {e}")

# Проверка на наличие некорректных значений после преобразования
if df['Dt_Customer'].isnull().sum() > 0:
    print("\nОбнаружены некорректные значения в Dt_Customer, удаляем их...")
    df = df.dropna(subset=['Dt_Customer'])

# Анализ даты после успешного преобразования
df['Customer_Since_Years'] = 2024 - df['Dt_Customer'].dt.year
plt.figure(figsize=(10, 5))
sns.histplot(df['Customer_Since_Years'], bins=20, color='green')
plt.title("Распределение времени с момента регистрации клиентов")
plt.xlabel("Лет с момента регистрации")
plt.ylabel("Частота")
plt.show()

# Выводы
print("\nПредварительный анализ показывает следующее:")
print("1. Есть распределения с выбросами, которые стоит проанализировать отдельно.")
print("2. Категориальные переменные (например, 'Education', 'Marital_Status') имеют разнообразие значений, их стоит изучить в контексте покупок.")
print("3. Есть перекосы в некоторых числовых данных, например, доходы и суммы трат.")

