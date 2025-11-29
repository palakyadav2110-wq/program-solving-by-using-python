
# WEATHER DATA VISUALIZER 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# ===============================================================
# SECTION 1 — LOAD WEATHER DATA (Task 1)
# ===============================================================

# Replace this with your real CSV path
csv_path = "weather_data.csv"   # Example: "Delhi_Weather.csv"

df = pd.read_csv(csv_path)

print("\n======= HEAD =======")
print(df.head())

print("\n======= INFO =======")
print(df.info())

print("\n======= DESCRIBE =======")
print(df.describe())

# ===============================================================
# SECTION 2 — CLEANING & PROCESSING (Task 2)
# ===============================================================

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Keep only useful columns (change if needed)
df = df[['date', 'temperature', 'humidity', 'rainfall']]

# Handle missing values
df['temperature'] = df['temperature'].interpolate().bfill().ffill()
df['humidity'] = df['humidity'].interpolate().bfill().ffill()
df['rainfall'] = df['rainfall'].fillna(0)

# Save cleaned CSV
os.makedirs("outputs", exist_ok=True)
df.to_csv("outputs/cleaned_weather.csv", index=False)

# ===============================================================
# SECTION 3 — STATISTICAL ANALYSIS (Task 3)
# ===============================================================

df = df.set_index('date')

# Daily stats
daily_stats = df.agg(['mean', 'min', 'max', 'std'])
print("\n======= DAILY STATS =======")
print(daily_stats)

# Monthly stats
monthly_stats = df.resample('M').agg(['mean', 'min', 'max', 'std'])
monthly_stats.to_csv("outputs/monthly_stats.csv")

# Yearly stats
yearly_stats = df.resample('Y').agg(['mean', 'min', 'max', 'std'])
yearly_stats.to_csv("outputs/yearly_stats.csv")

# ===============================================================
# SECTION 4 — VISUALIZATION WITH MATPLOTLIB (Task 4)
# ===============================================================

print("\nGenerating charts...")

# 1 — Daily temperature line chart
plt.figure(figsize=(10,4))
plt.plot(df.index, df['temperature'])
plt.title("Daily Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.savefig("outputs/daily_temperature.png")
plt.close()

# 2 — Monthly rainfall bar chart
monthly_rain = df['rainfall'].resample('M').sum()

plt.figure(figsize=(10,4))
plt.bar(monthly_rain.index.strftime("%Y-%m"), monthly_rain.values)
plt.title("Monthly Rainfall Total")
plt.xticks(rotation=45)
plt.ylabel("Rainfall (mm)")
plt.tight_layout()
plt.savefig("outputs/monthly_rainfall.png")
plt.close()

# 3 — Humidity vs Temperature scatter plot
plt.figure(figsize=(6,6))
plt.scatter(df['temperature'], df['humidity'], alpha=0.5)
plt.title("Humidity vs Temperature")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.tight_layout()
plt.savefig("outputs/humidity_vs_temperature.png")
plt.close()

# 4 — Combined plot
monthly_temp = df['temperature'].resample('M').mean()

fig, ax1 = plt.subplots(figsize=(10,4))
ax1.plot(df.index, df['temperature'], label="Daily Temp", color="blue")
ax1.set_ylabel("Temperature (°C)")

ax2 = ax1.twinx()
ax2.bar(monthly_rain.index, monthly_rain.values, color="orange", alpha=0.3, label="Monthly Rainfall")
ax2.set_ylabel("Rainfall (mm)")

plt.title("Temperature (Daily) + Rainfall (Monthly)")
plt.tight_layout()
plt.savefig("outputs/combined_plot.png")
plt.close()

# ===============================================================
# SECTION 5 — GROUPING & AGGREGATION (Task 5)
# ===============================================================

# Add month column
df['month'] = df.index.month

grouped_month = df.groupby('month').agg({
    'temperature': ['mean', 'min', 'max'],
    'rainfall': ['sum', 'mean'],
    'humidity': ['mean']
})

grouped_month.to_csv("outputs/grouped_by_month.csv")

# ===============================================================
# SECTION 6 — EXPORT & STORYTELLING (Task 6)
# ===============================================================

with open("outputs/report.txt", "w") as report:
    report.write("WEATHER DATA ANALYSIS REPORT\n")
    report.write("=============================\n\n")
    report.write("This report summarizes trends in temperature, rainfall, and humidity.\n")
    report.write("• Cleaned data saved as cleaned_weather.csv\n")
    report.write("• Monthly and yearly summaries generated\n")
    report.write("• All charts saved as PNG files\n\n")
    report.write("MAIN INSIGHTS:\n")
    report.write("- Temperature shows seasonal trends.\n")
    report.write("- Rainfall varies strongly by month.\n")
    report.write("- Humidity has a visible correlation with temperature.\n")

print("\nAll tasks completed! Check the 'outputs/' folder.")
