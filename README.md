Дипломная работа по курсу "Python-разработчик" на тему: "Сравнение различных библиотек для визуализации данных: Matplotlib, Seaborn и Plotly."

**Python** сегодня является одним из самых популярных языков программирования в мире, особенно в области анализа данных. \
Из-за этого разработчики создают все больше и больше библиотек для работы с данными и их визуализации. В 2023 году \
лучшие библиотеки Python для визуализации данных остаются прежними - **Matplotlib**, **Seaborn** и **Plotly**.

- **Matplotlib** (https://matplotlib.org/) - это наиболее распространенная и стандартная библиотека в Python для создания\
статических графиков. Она предоставляет практически безграничный спектр возможностей для создания и визуализации \
различных типов графиков, включая линейные, столбчатые, круговые, точечные, гистограммы, графики распределений и т.д. \
Отвечая на вопрос: "Можно ли что-то сделать на Matplotlib?", ответ практически всегда - Да.\

Пример кода
```
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

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
```

- **Seaborn** (https://seaborn.pydata.org/) - это библиотека, основанная на Matplotlib, но с более высоким уровнем \
абстракции и упрощенным интерфейсом. Она предоставляет множество функций для создания красивых графиков, включая \
гистограммы, ящики с усами, тепловые карты, рассеяния и многое другое. Также эта библиотека, в отличии от Matplotlib, \
позволяет строить более эстетически приятные для восприятия диаграммы, как говорится, "из коробки".\
Пример кода
```
import seaborn as sns
import matplotlib.pyplot as plt

# Пример данных
iris = sns.load_dataset("iris")

# Создание парного графика
sns.pairplot(iris, hue="species")
plt.title("Парные графики для набора данных Iris")
plt.show()
```

- **Plotly** (https://plotly.com/) - это библиотека для создания интерактивных графиков. Она предоставляет возможность \
создавать графики с помощью веб-интерфейса и делиться ими с другими пользователями. Plotly подходит для создания \
красивых и интерактивных графиков, но требует более высокого уровня компетенции.\
Пример кода
```
import plotly.express as px
import pandas as pd

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
```

В целом, выбор библиотеки Python для визуализации данных зависит от конкретных потребностей и уровня опыта разработчика.\
Matplotlib и Seaborn являются хорошими выборами для начинающих пользователей, а Plotly дополнительно предоставляет \
возможности для создания более продвинутых и интерактивных графиков.
