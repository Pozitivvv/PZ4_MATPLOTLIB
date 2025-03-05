import pandas as pd
import matplotlib.pyplot as plt

# Завантаження даних з правильным разделителем
data = pd.read_csv("titanic3.csv", sep=';')

# Преобразование столбца 'age' в числовой формат, заменяя запятые на точки
data['age'] = data['age'].str.replace(',', '.').astype(float)

# Побудова гістограми
fig = plt.figure(figsize=(10, 6))
axes = fig.add_axes([0, 0, 1, 1])

bins = 20  # Кількість стовпців у гістограмі

# Построение гистограмм и сохранение данных о столбцах
male_hist, male_bins, male_patches = axes.hist(data[data["sex"] == "male"]["age"].dropna(), bins=bins, alpha=0.6, label="Чоловіки", color="blue")
female_hist, female_bins, female_patches = axes.hist(data[data["sex"] == "female"]["age"].dropna(), bins=bins, alpha=0.6, label="Жінки", color="red")

# Добавление надписей на столбцы для мужчин
for count, x, patch in zip(male_hist, male_bins[:-1], male_patches):
    if count > 0:  # Добавляем надпись только если есть данные
        axes.text(x + (male_bins[1] - male_bins[0]) / 2, count + 5, int(count), 
                  ha='center', va='bottom', fontsize=10, color='blue')

# Добавление надписей на столбцы для женщин
for count, x, patch in zip(female_hist, female_bins[:-1], female_patches):
    if count > 0:  # Добавляем надпись только если есть данные
        axes.text(x + (female_bins[1] - female_bins[0]) / 2, count + 5, int(count), 
                  ha='center', va='bottom', fontsize=10, color='red')

# Добавление легенды и подписей
axes.legend()
axes.set_xlabel("Вік", fontsize=14)
axes.set_ylabel("Кількість", fontsize=14)
axes.set_title("Розподіл віку по статі", fontsize=16)

# Добавление координат на оси
max_age = int(data["age"].max()) + 10  # Максимальный возраст с запасом
axes.set_xticks(range(0, max_age, 10))  # Метки возраста каждые 10 лет снизу
axes.set_yticks(range(0, int(axes.get_ylim()[1]) + 50, 50))  # Метки по оси Y каждые 50 человек

# Улучшение видимости меток возраста
axes.tick_params(axis='x', labelsize=12, rotation=45)  # Увеличение шрифта и поворот меток

# Отображение графика
plt.show()