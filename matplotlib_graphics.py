import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm


#Линейный график
# Загрузка данных из CSV файла
file_path = 'https://raw.githubusercontent.com/Leshka60/-Homework_in_Urban/main/Diploma%20project/vendor-ww-monthly.csv'
data = pd.read_csv(file_path)

# Преобразуем столбец 'Date' в формат datetime
data['Date'] = pd.to_datetime(data['Date'])

# Устанавливаем 'Date' как индекс
data.set_index('Date', inplace=True)

# Построение графика
plt.figure(figsize=(12, 6))

# Строим линии для каждой операционной системы
plt.plot(data.index, data['Apple'], label='Apple', marker='o')
plt.plot(data.index, data['Samsung'], label='Samsung', marker='o')
plt.plot(data.index, data['Xiaomi'], label='Xiaomi', marker='o')
plt.plot(data.index, data['Other'], label='Other', marker='o')

# Добавление заголовка и меток осей
plt.title('Доля производителей смартфонов с июня 2024 по ноябрь 2024')
plt.xlabel('Дата')
plt.ylabel('Доля (%)')
plt.xticks(rotation=45)
plt.legend()
plt.grid()

# Отображение графика
plt.tight_layout()
plt.show()


#Многорядная столбчатая диаграмма
# Загрузка данных из CSV
file_path = 'https://raw.githubusercontent.com/Leshka60/-Homework_in_Urban/main/Diploma%20project/vendor-ww-monthly.csv'
df = pd.read_csv(file_path)

# Установка индекса по дате
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

plt.figure(figsize=(12,6))

# Настройка параметров для многорядной столбчатой диаграммы
bar_width = 0.2
x = np.arange(len(df))  # Позиции по оси x для месяцев

# Построение столбцов для каждой марки
plt.bar(x - bar_width, df['Apple'], width=bar_width, label='Apple')
plt.bar(x, df['Samsung'], width=bar_width, label='Samsung')
plt.bar(x + bar_width, df['Xiaomi'], width=bar_width, label='Xiaomi')
plt.bar(x + 2 * bar_width, df['Other'], width=bar_width, label='Other')

# Настройка графика
plt.xlabel('Месяц')
plt.ylabel('Доля (%)')
plt.title('Доля производителей смартфонов с июня 2024 по ноябрь 2024')
plt.xticks(x, df.index.strftime('%Y-%m'), rotation=45)  # Форматирование меток по оси x
plt.legend()  # Отображение легенды

# Отображение графика
plt.tight_layout()
plt.show()


#Круговая диаграмма
# Загрузка данных из CSV файла
file_path = 'https://raw.githubusercontent.com/Leshka60/-Homework_in_Urban/main/Diploma%20project/vendor-ww-monthly.csv'
data = pd.read_csv(file_path)

# Преобразование столбца 'Date' в формат datetime
data['Date'] = pd.to_datetime(data['Date'])

# Установка 'Date' в качестве индекса
data.set_index('Date', inplace=True)

# Группировка данных по месяцу и суммирование значений
monthly_data = data.resample('ME').sum().reset_index()

# Преобразование данных в длинный формат для анализа
monthly_data_melted = monthly_data.melt(id_vars='Date', var_name='Vendor', value_name='Sales')

# Суммирование продаж по производителям
vendor_sales = monthly_data_melted.groupby('Vendor')['Sales'].sum()

# Построение круговой диаграммы
plt.figure(figsize=(10, 7))
plt.pie(vendor_sales, labels=vendor_sales.index, autopct='%1.1f%%', startangle=140)
plt.title('Доля продаж по производителям')
plt.axis('equal')  # Чтобы круговая диаграмма выглядела как круг

# Отображение графика
plt.show()


# Тепловая карта
data = np.random.rand(10, 10)

plt.imshow(data, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title('Тепловая карта')
plt.show()


# Диаграмма рассеяния
x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, color='purple')
plt.title('Диаграмма рассеяния')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()


# 3D график
x = np.arange(-2, 5, 0.85)
xlen = len(x)
y = np.arange(-5, 2, 0.25)
ylen = len(y)
x, y = np.meshgrid(x, y)
r = np.sqrt(x ** 2 + y ** 2)
z = np.sin(r * 1.3)

ax = plt.figure(figsize=(8, 6))
ax = ax.add_subplot(1, 1, 1, projection='3d')
ax.plot_surface(x, y, z, cmap=cm.coolwarm, edgecolor='black', linewidth=0.23, antialiased=True)

plt.show()
