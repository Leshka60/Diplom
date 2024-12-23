import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import plotly.express as px
import math


#Линейный график
# Загрузка данных из CSV файла
file_path = 'https://raw.githubusercontent.com/Leshka60/-Homework_in_Urban/main/Diploma%20project/vendor-ww-monthly.csv'
data = pd.read_csv(file_path)

# Преобразуем столбец 'Date' в формат datetime
data['Date'] = pd.to_datetime(data['Date'])

# Создаем график
fig = go.Figure()

# Добавляем линии для каждого производителя
fig.add_trace(go.Scatter(x=data['Date'], y=data['Apple'], mode='lines+markers', name='Apple'))
fig.add_trace(go.Scatter(x=data['Date'], y=data['Samsung'], mode='lines+markers', name='Samsung'))
fig.add_trace(go.Scatter(x=data['Date'], y=data['Xiaomi'], mode='lines+markers', name='Xiaomi'))
fig.add_trace(go.Scatter(x=data['Date'], y=data['Other'], mode='lines+markers', name='Other'))

# Настройка заголовка и меток осей
fig.update_layout(
    title='Доля производителей смартфонов с июня 2024 по ноябрь 2024',
    xaxis_title='Дата',
    yaxis_title='Доля (%)',
    legend_title='Производители',
    xaxis=dict(tickformat='%Y-%m-%d'),
    template='plotly_white'
)

# Отображение графика
fig.show()


#Столбчатая диаграмма
# Загрузка данных из CSV файла
file_path = 'https://raw.githubusercontent.com/Leshka60/-Homework_in_Urban/main/Diploma%20project/vendor-ww-monthly.csv'
data = pd.read_csv(file_path)

# Преобразование столбца 'Date' в формат datetime
data['Date'] = pd.to_datetime(data['Date'])

# Установка 'Date' в качестве индекса
data.set_index('Date', inplace=True)

# Группировка данных по месяцу и суммирование значений
monthly_data = data.resample('ME').sum().reset_index()

# Преобразование данных в длинный формат для Plotly
monthly_data_melted = monthly_data.melt(id_vars='Date', var_name='Vendor', value_name='Sales')

# Построение столбчатой диаграммы
fig = px.bar(monthly_data_melted, x='Date', y='Sales', color='Vendor',
             title='Доля производителей смартфонов с июня 2024 по ноябрь 2024',
             labels={'Sales': 'Доля (%)', 'Date': 'Месяц', 'Vendor': 'Производитель'},
             text='Sales')

# Настройка отображения значений на столбцах
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')

# Отображение графика
fig.show()


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


# Пузырьковая диаграмма
# Загружаем данные, определяем текст при наведении курсора и размер пузырька
data = px.data.gapminder()
df_2007 = data[data['year']==2007]
df_2007 = df_2007.sort_values(['continent', 'country'])
hover_text = []
bubble_size = []
for index, row in df_2007.iterrows():
    hover_text.append(('Country: {country}<br>'+
                      'Life Expectancy: {lifeExp}<br>'+
                      'GDP per capita: {gdp}<br>'+
                      'Population: {pop}<br>'+
                      'Year: {year}').format(country=row['country'],
                                            lifeExp=row['lifeExp'],
                                            gdp=row['gdpPercap'],
                                            pop=row['pop'],
                                            year=row['year']))
    bubble_size.append(math.sqrt(row['pop']))
df_2007['text'] = hover_text
df_2007['size'] = bubble_size
sizeref = 2.*max(df_2007['size'])/(100**2)
# Dictionary with dataframes for each continent
continent_names = ['Africa', 'Americas', 'Asia', 'Europe', 'Oceania']
continent_data = {continent:df_2007.query("continent == '%s'" %continent)
                              for continent in continent_names}
# Создание фигуры
fig = go.Figure()
for continent_name, continent in continent_data.items():
    fig.add_trace(go.Scatter(
        x=continent['gdpPercap'], y=continent['lifeExp'],
        name=continent_name, text=continent['text'],
        marker_size=continent['size'],
        ))
# Настройка внешнего вида и компоновки маркера
fig.update_traces(mode='markers', marker=dict(sizemode='area',
                                              sizeref=sizeref, line_width=2))
fig.update_layout(
    title='Life Expectancy v. Per Capita GDP, 2007',
    xaxis=dict(
        title='GDP per capita (2000 dollars)',
        gridcolor='white',
        type='log',
        gridwidth=2,
    ),
    yaxis=dict(
        title='Life Expectancy (years)',
        gridcolor='white',
        gridwidth=2,
    ),
    paper_bgcolor='rgb(243, 243, 243)',
    plot_bgcolor='rgb(243, 243, 243)',
)
fig.show()


# 3D график

# Пример данных
df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 11, 12, 13, 14],
    'z': [5, 6, 7, 8, 9],
    'category': ['A', 'B', 'A', 'B', 'A']
})

# Создание 3D графика
fig = px.scatter_3d(df, x='x', y='y', z='z', color='category',
                     title='3D Рассеянный график',
                     labels={'x': 'Ось X', 'y': 'Ось Y', 'z': 'Ось Z'})

# Отображение графика
fig.show()
