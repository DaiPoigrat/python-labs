import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('task19.csv', delimiter=';', encoding='windows-1251')

grouped = data.groupby('Пункт назначения')['Расход бензина'].sum()

plt.figure(figsize=(8, 8))
plt.pie(grouped, labels=grouped.index, autopct='%1.1f%%', startangle=140)
plt.title('Распределение расхода бензина по населенным пунктам отправления')
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(data['Масса груза'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Масса груза (кг)')
plt.ylabel('Частота')
plt.title('Распределение массы перевезенного груза')
plt.grid(True)
plt.show()

plt.scatter(data['Пункт отправления'], data['Пункт назначения'], c='blue')
plt.title('График зависимости пункта назначения от пункта отправления')
plt.xlabel('Пункт отправления')
plt.ylabel('Пункт назначения')
plt.tight_layout()

plt.show()
