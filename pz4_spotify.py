import pandas as pd
import matplotlib.pyplot as plt

# Завантаження даних
file_path = 'spotify_2023.csv'
data = pd.read_csv(file_path, encoding='ISO-8859-1')

# Перетворюємо стовпець 'streams' у числовий формат
data['streams'] = pd.to_numeric(data['streams'], errors='coerce')

# Групування за артистами
artist_streams = data.groupby("artist(s)_name")["streams"].sum().sort_values(ascending=False)

# Беремо Топ-15 артистів
top_artists = artist_streams.head(15)

# Побудова графіка
plt.figure(figsize=(12, 6))
top_artists.sort_values().plot(kind="barh", color="purple", alpha=0.7)

# Підписи
plt.xlabel("Загальна кількість прослуховувань (млрд)", fontsize=12)
plt.ylabel("Артисти", fontsize=12)
plt.title("Топ-15 артистів за кількістю прослуховувань на Spotify", fontsize=14)

# Відображення чисел на графіку
for index, value in enumerate(top_artists.sort_values()):
    plt.text(value, index, f"{value/1e9:.1f} млрд", va='center', fontsize=10, color="black")

plt.grid(axis="x", linestyle="--", alpha=0.5)
plt.show()
