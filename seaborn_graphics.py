import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#Линейный график
# Загрузка данных из CSV файла
file_path = 'https://raw.githubusercontent.com/Leshka60/-Homework_in_Urban/main/Diploma%20project/vendor-ww-monthly.csv'
data = pd.read_csv(file_path)

# Преобразуем столбец 'Date' в формат datetime
data['Date'] = pd.to_datetime(data['Date'])

# Устанавливаем 'Date' как индекс
data.set_index('Date', inplace=True)

# Сброс индекса для использования в Seaborn
data_reset = data.reset_index()

# Построение линейного графика с использованием Seaborn
plt.figure(figsize=(12, 6))
sns.lineplot(data=data_reset, x='Date', y='Apple', label='Apple', marker='o')
sns.lineplot(data=data_reset, x='Date', y='Samsung', label='Samsung', marker='o')
sns.lineplot(data=data_reset, x='Date', y='Xiaomi', label='Xiaomi', marker='o')
sns.lineplot(data=data_reset, x='Date', y='Other', label='Other', marker='o')

# Добавление заголовка и меток осей
plt.title('Доля производителей с июня 2024 по ноябрь 2024')
plt.xlabel('Дата')
plt.ylabel('Доля (%)')
plt.xticks(rotation=45)
plt.legend()
plt.grid()

# Отображение графика
plt.tight_layout()
plt.show()


#Многорядная столбчатая диаграмма
# Загрузка данных из CSV файла
file_path = 'https://raw.githubusercontent.com/Leshka60/-Homework_in_Urban/main/Diploma%20project/vendor-ww-monthly.csv'
data = pd.read_csv(file_path)

# Преобразование столбца 'Date' в формат datetime
data['Date'] = pd.to_datetime(data['Date'])

# Установка 'Date' в качестве индекса
data.set_index('Date', inplace=True)

# Группировка данных по месяцу и суммирование значений
monthly_data = data.resample('ME').sum().reset_index()

# Настройка стиля Seaborn
sns.set(style="darkgrid")

sns.set_palette("husl")

# Преобразование данных в длинный формат для Seaborn
monthly_data_melted = monthly_data.melt(id_vars='Date', var_name='Vendor', value_name='Sales')

# Построение столбчатой диаграммы
plt.figure(figsize=(12, 6))
sns.barplot(data=monthly_data_melted, x='Date', y='Sales', hue='Vendor')

# Настройка заголовка и меток осей
plt.title('Доля производителей смартфонов с июня 2024 по ноябрь 2024')
plt.xlabel('Месяц')
plt.ylabel('Доля (%)')
plt.xticks(rotation=45)
plt.legend(title='Производители')

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

# Настройка стиля Seaborn
sns.set(style="whitegrid")

# Построение круговой диаграммы
plt.figure(figsize=(10, 7))
plt.pie(vendor_sales, labels=vendor_sales.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
plt.title('Доля продаж по производителям')
plt.axis('equal')  # Чтобы круговая диаграмма выглядела как круг

# Отображение графика
plt.show()


# Коробчатые графики

# Пример данных
tips = sns.load_dataset("tips")

# Создание коробчатого графика
sns.boxplot(x="day", y="total_bill", data=tips)
plt.title("Коробчатый график расходов по дням")
plt.show()


# Скрипичные графики

# Пример данных
tips = sns.load_dataset("tips")

# Создание скрипичного графика
sns.violinplot(x="day", y="total_bill", data=tips)
plt.title("Скрипичный график расходов по дням")
plt.show()


# Парные графики

# Пример данных
iris = sns.load_dataset("iris")

# Создание парного графика
sns.pairplot(iris, hue="species")
plt.title("Парные графики для набора данных Iris")
plt.show()
