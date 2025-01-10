import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Przygotowanie danych
file_path = '/Users/macbook/Desktop/Strava_db.Activities3.xlsx'
data = pd.read_excel(file_path)

# Zmiana start_date na format datetime, aby łatwiej manipulować danymi 
data['start_date'] = pd.to_datetime(data['start_date'], errors='coerce')
data['month'] = data['start_date'].dt.to_period('M')  

###Obliczenie maksymalnego tętna
def max_hr(age):
    return 220 - age

### Obliczenia maksymalnego tętna 
wiek = 25
wynik = max_hr(wiek)
print(f"Maksymalne tętno dla osoby w wieku {wiek} lat to: {wynik} bpm")


###  Klasyfikowanie aktywności do stref tętna (HR Zones)
def classify_hr_zone(hr):
    if hr < 0.50 * wynik:
        return 'Odpoczynku'
    elif 0.50 * wynik <= hr < 0.60 * wynik:
        return 'Regeneracyjna'
    elif 0.60 * wynik <= hr < 0.70 * wynik:
        return 'Wytrzymałość podstawowa'
    elif 0.70 * wynik <= hr < 0.80 * wynik:
        return 'Tlenowa'
    elif 0.80 * wynik <= hr < 0.90 * wynik:
        return 'Beztlenowa'
    elif 0.90 * wynik <= hr <= wynik:
        return 'Maksymalna'
    else:
        return 'Outside Zones'

data['HR_zone'] = np.where(
    data['average_heartrate'].notna(), 
    data['average_heartrate'].apply(classify_hr_zone), 
    'No Data')

### Obliczenie TSS 
def calculate_tss(row):
    if pd.notna(row['average_heartrate']) and row['average_heartrate'] > 0:
        intensity_factor = row['average_heartrate'] / 195
        tss = row['moving_time'] / 60 * (intensity_factor ** 2)
        return tss
    return 0

data['TSS'] = data.apply(calculate_tss, axis=1)


### Rozkład stref tętna 
hr_zone_distribution = data['HR_zone'].value_counts(normalize=True) * 100
hr_zone_counts = data['HR_zone'].value_counts()  # Liczba aktywności w każdej strefie
total_activities = hr_zone_counts.sum()  # Całkowita liczba aktywności

print("Rozkład stref tętna (HR Zone Distribution):")
for zone, percent in hr_zone_distribution.items():
    count = hr_zone_counts[zone]
    print(f"{zone}: {percent:.2f}% ({count} aktywności)")

print(f"Całkowita liczba aktywności: {total_activities}")

### Trendy dla miesięcznego TSS i HR 
monthly_trends = data.groupby('month').agg(
    average_hr=('average_heartrate', 'mean'),
    max_hr=('max_heartrate', 'mean'),
    total_tss=('TSS', 'sum')
).reset_index()

print("Trendy miesięczne:")
print(monthly_trends)


### Wizualizacja rozkładu tętna
plt.figure(figsize=(10, 6))
hr_zone_distribution.plot(kind='bar', color='skyblue', alpha=0.8)
plt.title('Rozkład stref tętna')
plt.ylabel('Procenty')
plt.xlabel('Strefy tętna')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


### Wizualizacja miesięczny TSS 
# Wielkość wykresu
plt.figure(figsize=(10, 6))

# Wykres liniowy dla danych miesięcznych
plt.plot(monthly_trends['month'].astype(str), 
         monthly_trends['total_tss'], 
         marker='o', 
         linestyle='-', 
         label='TSS')

plt.title('Miesięczny Training Stress Score (TSS)')
plt.ylabel('TSS')
plt.xlabel('Month')
plt.xticks(rotation=45)

# Wartości danych nad punktami na wykresie
for idx, (month, tss) in enumerate(zip(monthly_trends['month'], monthly_trends['total_tss'])):
    plt.text(idx, tss + 20, f'{tss:.0f}', ha='center')

plt.legend()
plt.tight_layout()
plt.show()


### Wizualizacja 
plt.figure(figsize=(12, 6))
plt.plot(monthly_trends['month'].astype(str), monthly_trends['total_tss'], marker='o', label='TSS', color='blue')
plt.plot(monthly_trends['month'].astype(str), monthly_trends['average_hr'], marker='o', label='Średnie tętno', color='green')
plt.plot(monthly_trends['month'].astype(str), monthly_trends['max_hr'], marker='x', label='Maksymalne tętno', color='red', linestyle='--')

plt.title('Trendy - TSS i tętno')
plt.ylabel('Values')
plt.xlabel('Month')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

