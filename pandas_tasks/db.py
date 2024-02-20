import pandas as pd
import matplotlib.pyplot as plt

agents = pd.read_csv('travel_agents.csv', sep=';')
travels = pd.read_csv('travels.csv', sep=';')
sales = pd.read_csv('sale_of_tour_packages.csv', sep=';')

regional_cities = [
    'Москва', 'Санкт-Петербург', 'Екатеринбург', 'Новосибирск', 'Красноярск', 'Ростов-на-Дону', 'Краснодар',
    'Владивосток', 'Казань', 'Иркутск', 'Нижний Новгород', 'Челябинск', 'Уфа', 'Самара', 'Омск', 'Волгоград', 'Пермь',
    'Красноярск', 'Воронеж', 'Саратов'
]
regional_sales = sales[sales['ID тура'].isin(travels[travels['Город'].isin(regional_cities)]['ID тура'])]
total_people_regional = regional_sales['Количество проданных путёвок'].sum()

print(f'{total_people_regional = }')

operator_horizon = 'Горизонт'
horizon_sales = sales[
    sales['ID туроператора'] == agents[agents['Название'] == operator_horizon]['ID туроператора'].values[0]
    ]

city_sales = horizon_sales.merge(travels, on='ID тура')
city_total_sales = city_sales.groupby('Город')['Стоимость, на 1 чел'].sum()

plt.figure(figsize=(10, 8))
plt.pie(city_total_sales, labels=city_total_sales.index, autopct='%1.1f%%', startangle=140)
plt.title('Общая стоимость путевок и стоимость по городам (туроператор "Горизонт")')
plt.show()

operator_dream = 'Мечта'
dream_sales = sales[
    sales['ID туроператора'] == agents[agents['Название'] == operator_dream]['ID туроператора'].values[0]]

daily_sales_dream = dream_sales.groupby('Дата')['Количество проданных путёвок'].sum()

daily_sales_dream.plot(kind='bar', figsize=(12, 6))
plt.grid(True)
plt.title('Количество проданных путевок туроператором "Мечта" по дням')
plt.xlabel('Дата')
plt.ylabel('Количество продаж')
plt.show()
