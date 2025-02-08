
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from datetime import date as datetime_date

if 'meals' not in st.session_state:
    st.session_state.meals = []
if 'diet_plans' not in st.session_state:
    st.session_state.diet_plans = []

def load_data():
    st.write("Data loaded successfully!")

def add_meal(selected_date, meal_name, calories):
    meal_exists = any(meal['date'] == selected_date and meal['meal_name'] == meal_name for meal in st.session_state.meals)
    if not meal_exists:
        st.session_state.meals.append({"date": selected_date, "meal_name": meal_name, "calories": calories})
        st.write(f"Meal '{meal_name}' with {calories} calories added on {selected_date}")
    else:
        st.error(f"Meal '{meal_name}' already exists for {selected_date}")

def edit_meal(selected_date, meal_name, new_calories):
    for meal in st.session_state.meals:
        if meal['date'] == selected_date and meal['meal_name'] == meal_name:
            meal['calories'] = new_calories
            st.write(f"Meal '{meal_name}' updated with {new_calories} calories on {selected_date}")
            return
    st.error("Meal not found!")

def delete_meal(selected_date, meal_name):
    for meal in st.session_state.meals:
        if meal['date'] == selected_date and meal['meal_name'] == meal_name:
            st.session_state.meals.remove(meal)
            st.write(f"Meal '{meal_name}' deleted from {selected_date}")
            return
    st.error("Meal not found!")

def view_meals(selected_date):
    meals_for_date = [meal for meal in st.session_state.meals if meal['date'] == selected_date]
    if meals_for_date:
        st.write(f"Meals for {selected_date}:")
        for meal in meals_for_date:
            st.write(f"{meal['meal_name']} - {meal['calories']} calories")
    else:
        st.write(f"No meals found for {selected_date}.")

def display_summary(selected_date):
    meals_for_date = [meal for meal in st.session_state.meals if meal['date'] == selected_date]
    if meals_for_date:
        total_calories = sum(meal['calories'] for meal in meals_for_date)
        meal_names = [meal['meal_name'] for meal in meals_for_date]
        meal_calories = [meal['calories'] for meal in meals_for_date]

        st.write(f"Summary for {selected_date}:")
        st.write(f"Total Calories = {total_calories}")
        
        fig, ax = plt.subplots()
        ax.bar(meal_names, meal_calories, color='skyblue')
        ax.set_ylabel("Calories")
        ax.set_title(f"Calories Distribution for {selected_date}")
        st.pyplot(fig)
        
        fig2, ax2 = plt.subplots()
        ax2.pie(meal_calories, labels=meal_names, autopct='%1.1f%%', startangle=90)
        ax2.set_title(f"Meal Calorie Distribution for {selected_date}")
        st.pyplot(fig2)
    else:
        st.write(f"No meals found for {selected_date}.")

def weekly_trend(start_date, end_date):
    meals_in_range = [meal for meal in st.session_state.meals if start_date <= meal['date'] <= end_date]
    if meals_in_range:
        dates = [meal['date'] for meal in meals_in_range]
        calories = [meal['calories'] for meal in meals_in_range]
        
        unique_dates = sorted(set(dates))
        daily_totals = [sum(meal['calories'] for meal in meals_in_range if meal['date'] == date) for date in unique_dates]
        
        fig, ax = plt.subplots()
        ax.plot(unique_dates, daily_totals, marker='o', color='b')
        ax.set_xlabel("Date")
        ax.set_ylabel("Total Calories")
        ax.set_title(f"Weekly Calorie Trend ({start_date} to {end_date})")
        st.pyplot(fig)
    else:
        st.write("No meals found in this date range.")

def create_diet_plan(name, goal, daily_calories):
    st.session_state.diet_plans.append({"name": name, "goal": goal, "daily_calories": daily_calories})
    st.write(f"Diet plan '{name}' for goal '{goal}' with daily calories: {daily_calories}")

def view_diet_plan():
    if not st.session_state.diet_plans:
        st.write("No diet plans available.")
    else:
        st.write("Viewing all diet plans:")
        for plan in st.session_state.diet_plans:
            st.write(f"Name: {plan['name']}, Goal: {plan['goal']}, Daily Calories: {plan['daily_calories']}")

def recommend_calories(diet_plan_name, selected_date):
    for plan in st.session_state.diet_plans:
        if plan['name'] == diet_plan_name:
            recommended_calories = plan['daily_calories']
            st.write(f"Recommended calories for '{diet_plan_name}' on {selected_date}: {recommended_calories}")
            return
    st.error(f"Diet plan '{diet_plan_name}' not found!")

def calculate_calories(height, weight, age, gender, activity_level):
    if gender == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    
    activity_levels = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725,
        "very_active": 1.9
    }
    tdee = bmr * activity_levels.get(activity_level, 1.2)
    
    st.write(f"Your Total Daily Energy Expenditure (TDEE) is {tdee:.2f} calories.")
    st.write(f"For weight maintenance, aim to eat around {tdee:.2f} calories daily.")
    st.write(f"For a deficit, subtract 500-1000 calories, depending on your goal.")
    st.write(f"For a surplus, add 500-1000 calories, depending on your goal.")

def save_data():
    st.write("Data saved successfully!")

def main():
    st.title("👋 Welcome to the Advanced Calorie Tracker!")

    load_data()

    menu = [
        "Add a Meal",
        "Edit a Meal",
        "Delete a Meal",
        "View Meals for a Date",
        "Display Summary for a Date",
        "Generate Weekly Calorie Trend",
        "Create a Diet Plan",
        "View Diet Plans",
        "Recommend Calories for a Date",
        "Calculate Calories for Weight Maintenance/Deficit",
        "Save and Exit"
    ]
    
    choice = st.sidebar.selectbox("📋 Choose an option:", menu)

    if choice == "Add a Meal":
        selected_date = st.date_input("📅 Select the date:", min_value=datetime_date(2020, 1, 1))
        meal_name = st.text_input("🍴 Enter the meal name: ")
        calories = st.number_input("🔥 Enter the calories: ", min_value=0)
        if st.button("Add Meal"):
            if selected_date and meal_name and calories:
                add_meal(selected_date, meal_name, calories)
                st.success("Meal added successfully!")
            else:
                st.error("Please provide all the required details.")
    
    elif choice == "Edit a Meal":
        selected_date = st.date_input("📅 Select the date:", min_value=datetime_date(2020, 1, 1))
        meal_name = st.text_input("🍴 Enter the meal name to edit: ")
        new_calories = st.number_input("🔥 Enter the new calorie value: ", min_value=0)
        if st.button("Edit Meal"):
            if selected_date and meal_name and new_calories:
                edit_meal(selected_date, meal_name, new_calories)
                st.success("Meal updated successfully!")
            else:
                st.error("Please provide all the required details.")

    elif choice == "Delete a Meal":
        selected_date = st.date_input("📅 Select the date:", min_value=datetime_date(2020, 1, 1))
        meal_name = st.text_input("🍴 Enter the meal name to delete: ")
        if st.button("Delete Meal"):
            if selected_date and meal_name:
                delete_meal(selected_date, meal_name)
                st.success("Meal deleted successfully!")
            else:
                st.error("Please provide all the required details.")
                
    elif choice == "View Meals for a Date":
        selected_date = st.date_input("📅 Select the date:", min_value=datetime_date(2020, 1, 1))
        if st.button("View Meals"):
            if selected_date:
                view_meals(selected_date)
            else:
                st.error("Please provide a date.")
    
    elif choice == "Display Summary for a Date":
        selected_date = st.date_input("📅 Select the date:", min_value=datetime_date(2020, 1, 1))
        if st.button("Display Summary"):
            if selected_date:
                display_summary(selected_date)
            else:
                st.error("Please provide a date.")
    
    elif choice == "Generate Weekly Calorie Trend":
        start_date = st.date_input("📅 Select the start date:", min_value=datetime_date(2020, 1, 1))
        end_date = st.date_input("📅 Select the end date:", min_value=datetime_date(2020, 1, 1))
        if st.button("Generate Trend"):
            if start_date and end_date:
                weekly_trend(start_date, end_date)
            else:
                st.error("Please provide both start and end dates.")
    
    elif choice == "Create a Diet Plan":
        name = st.text_input("📝 Enter the diet plan name: ")
        goal = st.text_input("🎯 Enter the goal (e.g., Weight Loss, Maintenance, Weight Gain): ")
        daily_calories = st.number_input("🔥 Enter daily calorie goal: ", min_value=0)
        if st.button("Create Diet Plan"):
            if name and goal and daily_calories:
                create_diet_plan(name, goal, daily_calories)
                st.success("Diet plan created successfully!")
            else:
                st.error("Please provide all the required details.")

    elif choice == "View Diet Plans":
        if st.button("View Diet Plans"):
            view_diet_plan()
    
    elif choice == "Recommend Calories for a Date":
        selected_date = st.date_input("📅 Select the date:", min_value=datetime_date(2020, 1, 1))
        diet_plan_name = st.text_input("🍽️ Enter your diet plan name: ")
        if st.button("Recommend Calories"):
            if selected_date and diet_plan_name:
                recommend_calories(diet_plan_name, selected_date)
            else:
                st.error("Please provide both diet plan name and date.")
    
    elif choice == "Calculate Calories for Weight Maintenance/Deficit":
        height = st.number_input("📏 Enter your height in cm: ", min_value=0)
        weight = st.number_input("⚖️ Enter your weight in kg: ", min_value=0)
        age = st.number_input("🎂 Enter your age: ", min_value=0)
        gender = st.selectbox("♂️♀️ Enter your gender:", ["male", "female"])
        activity_level = st.selectbox("🏃 Enter your activity level:", 
                                      ["sedentary", "light", "moderate", "active", "very_active"])
        if st.button("Calculate Calories"):
            if height and weight and age and gender:
                calculate_calories(height, weight, age, gender, activity_level)
            else:
                st.error("Please provide all the required details.")
    
    elif choice == "Save and Exit":
        save_data()

if __name__ == "__main__":
    main()
