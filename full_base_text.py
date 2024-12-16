import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка данных
df = pd.read_csv('marketing_campaign.csv', sep='\t')

# Предварительный просмотр данных
print("\nПервые строки данных:\n")
print(df.head())
print("\nОбщая информация о данных:\n")
print(df.info())

# Проверка на наличие дубликатов
duplicates = df.duplicated().sum()
if duplicates > 0:
    print(f"\nНайдено дубликатов: {duplicates}, удаляем их...")
    df = df.drop_duplicates()
else:
    print("\nДубликатов не найдено.")

# Проверка на пропуски
print("\nКоличество пропусков в данных:\n")
missing_values = df.isnull().sum()
print(missing_values[missing_values > 0])

# Заполнение пропусков (пример: замена на медианные значения для числовых столбцов)
num_cols = df.select_dtypes(include=[np.number]).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].median())

# Проверка изменений
print("\nПропуски после заполнения:\n")
print(df.isnull().sum().sum())

# Изменение типа данных (пример для столбца 'Dt_Customer')
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], format='%d-%m-%Y')

print("\nОбновленная информация о данных:\n")
print(df.info())

# Статистическое описание данных
print("\nОсновная статистика:\n")
print(df.describe())
