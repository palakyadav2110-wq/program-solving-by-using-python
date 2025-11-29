# tracker.py
# Name: [__PALAK_]
# Date: 2025-10-09
# Title: Daily Calorie Tracker CLI

print("Welcome to the Daily Calorie Tracker CLI Tool!")
print("Track your meals and calories easily.")


# Task 2: Input meal data
meal_names = []
calorie_amounts = []

num_meals = int(input("Enter the number of meals you want to track: "))

for i in range(num_meals):
    meal = input(f"Enter meal name #{i+1}: ")
    calories = float(input(f"Enter calories for {meal}: "))
    meal_names.append(meal)
    calorie_amounts.append(calories)

# Task 3: Calorie calculations
total_calories = sum(calorie_amounts)
average_calories = total_calories / num_meals

daily_limit = float(input("Enter your daily calorie limit: "))

# Task 4: Warning system
if total_calories > daily_limit:
    print("Warning: Your total calorie intake exceeds your daily limit!")
else:
    print("Great! Your calorie intake is within the daily limit.")

# Task 5: Formatted output
print("Meal Name\tCalories")
print("---------------------------")
for meal, cal in zip(meal_names, calorie_amounts):
    print(f"{meal:10}\t{cal:.2f}")
print("---------------------------")
print(f"{'Total':10}\t{total_calories:.2f}")
print(f"{'Average':10}\t{average_calories:.2f}")
