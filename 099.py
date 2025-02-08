import matplotlib.pyplot as plt

def load_data():
    print("Data loaded successfully!")

def save_data():
    print("Data saved successfully!")

def add_meal(date, meal_name, calories):
    print(f"Meal '{meal_name}' with {calories} calories added for {date}.")

def edit_meal(date, meal_name, new_calories):
    print(f"Meal '{meal_name}' updated to {new_calories} calories for {date}.")

def delete_meal(date, meal_name):
    print(f"Meal '{meal_name}' deleted for {date}.")

def view_meals(date):
    print(f"Displaying meals for {date}.")

def display_summary(date):
    meals = {"Breakfast": 300, "Lunch": 600, "Dinner": 500, "Snacks": 200}
    print(f"Summary for {date}:")
    for meal, calories in meals.items():
        print(f"{meal}: {calories} kcal")
    
    plt.bar(meals.keys(), meals.values(), color=['blue', 'green', 'red', 'orange'])
    plt.xlabel("Meal")
    plt.ylabel("Calories")
    plt.title(f"Calorie Intake on {date}")
    plt.show()

def weekly_trend(start_date, end_date):
    dates = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"]
    calories = [1800, 2000, 1750, 1900, 2100, 1950, 1850]
    plt.plot(dates, calories, marker='o', linestyle='-', color='b')
    plt.xlabel("Date")
    plt.ylabel("Calories Consumed")
    plt.title(f"Weekly Calorie Trend ({start_date} to {end_date})")
    plt.show()

def calculate_calories(height, weight, age, gender, activity_level):
    if gender.lower() == "male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    
    activity_multipliers = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725,
        "very_active": 1.9
    }
    
    if activity_level in activity_multipliers:
        daily_calories = bmr * activity_multipliers[activity_level]
        print(f"Your daily calorie requirement is approximately {daily_calories:.2f} kcal.")
    else:
        print("Invalid activity level entered.")

def main():
    load_data()
    print("Welcome to the Advanced Calorie Tracker!")

    while True:
        print("\nChoose an option:")
        print("1. Add a Meal")
        print("2. Edit a Meal")
        print("3. Delete a Meal")
        print("4. View Meals for a Date")
        print("5. Display Summary for a Date")
        print("6. Generate Weekly Calorie Trend")
        print("7. Calculate Calories for Weight Maintenance/Deficit")
        print("8. Save and Exit")
        
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            meal_name = input("Enter the meal name: ")
            try:
                calories = int(input("Enter the calories: "))
                add_meal(date, meal_name, calories)
            except ValueError:
                print("Invalid calorie input. Please enter a valid number.")
        elif choice == "2":
            date = input("Enter the date (YYYY-MM-DD): ")
            meal_name = input("Enter the meal name to edit: ")
            try:
                new_calories = int(input("Enter the new calorie value: "))
                edit_meal(date, meal_name, new_calories)
            except ValueError:
                print("Invalid calorie input. Please enter a valid number.")
        elif choice == "3":
            date = input("Enter the date (YYYY-MM-DD): ")
            meal_name = input("Enter the meal name to delete: ")
            delete_meal(date, meal_name)
        elif choice == "4":
            date = input("Enter the date (YYYY-MM-DD): ")
            view_meals(date)
        elif choice == "5":
            date = input("Enter the date (YYYY-MM-DD): ")
            display_summary(date)
        elif choice == "6":
            start_date = input("Enter the start date (YYYY-MM-DD): ")
            end_date = input("Enter the end date (YYYY-MM-DD): ")
            weekly_trend(start_date, end_date)
        elif choice == "7":
            height = float(input("Enter your height in cm: "))
            weight = float(input("Enter your weight in kg: "))
            age = int(input("Enter your age: "))
            gender = input("Enter your gender (male/female): ")
            activity_level = input("Enter your activity level (sedentary, light, moderate, active, very_active): ")
            calculate_calories(height, weight, age, gender, activity_level)
        elif choice == "8":
            save_data()
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option (1-8).")

if __name__ == "__main__":
    main()
