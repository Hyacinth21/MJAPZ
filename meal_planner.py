import os
import json
import random
import datetime
import time

# ---------------------- FILE PATH ----------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEALS_FILE = os.path.join(BASE_DIR, "meal.json")  # your file name

# ---------------------- LOAD DATA ----------------------
def load_meals():
    with open(MEALS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def load_user_data():
    if os.path.exists("user_data.json"):
        with open("user_data.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_user_data(data):
    with open("user_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

# ---------------------- MEAL GENERATOR ----------------------
def generate_meal_plan(tdee, meals):
    plan = {}
    total_cal = 0
    categories = ["Breakfast", "Lunch", "Dinner", "Snacks", "Other Meals"]

    for cat in categories:
        meal = random.choice(meals[cat])
        plan[cat] = meal
        total_cal += meal["calories"]

    # Add extra meals if total_cal < TDEE
    extra_count = 1
    while total_cal < tdee:
        cat = random.choice(categories)
        meal = random.choice(meals[cat])
        plan[f"Extra {cat} {extra_count}"] = meal
        total_cal += meal["calories"]
        extra_count += 1

    return plan, total_cal

# ---------------------- TDEE CALCULATOR ----------------------
def calculate_tdee(weight, height, age, sex, activity_choice, goal):
    activity_multipliers = [1.2, 1.375, 1.55, 1.725, 1.9]
    activity_level = activity_multipliers[activity_choice - 1]

    if sex == "male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    tdee = bmr * activity_level

    if goal == "1":
        tdee -= 500
        goal_text = "Lose Weight"
    elif goal == "2":
        goal_text = "Maintain Weight"
    else:
        tdee += 500
        goal_text = "Gain Weight"

    protein_g = 1.6 * weight
    protein_cal = protein_g * 4
    fat_cal = tdee * 0.30
    fat_g = fat_cal / 9
    carb_cal = tdee - (protein_cal + fat_cal)
    carb_g = carb_cal / 4

    macros = {
        "Calories": round(tdee),
        "Protein (g)": round(protein_g),
        "Fats (g)": round(fat_g),
        "Carbs (g)": round(carb_g),
        "Goal": goal_text
    }
    return macros

# ---------------------- DISPLAY ----------------------
def display_summary(name, macros, meal_plan, total_cal):
    print("\n" + "=" * 50)
    print(f" Personalized Meal Plan for {name}")
    print("=" * 50)
    print(f"Goal: {macros['Goal']}")
    print(f"Calories: {macros['Calories']} kcal/day")
    print(f"Protein: {macros['Protein (g)']} g")
    print(f"Fats: {macros['Fats (g)']} g")
    print(f"Carbs: {macros['Carbs (g)']} g")
    print(f"Generated Total: {total_cal} kcal")
    print("=" * 50)

    for category, meal in meal_plan.items():
        print(f"\n{category}: {meal['name']}")
        print(f"  Calories: {meal['calories']} kcal | Protein: {meal['protein']}g | Carbs: {meal['carbs']}g | Fats: {meal['fat']}g")

    print("\n" + "=" * 50)
    print("1. Show recipe links")
    print("2. Exit")
    print("3. Back to menu")
    print("=" * 50)

# ---------------------- SHOW LINKS ----------------------
def show_links(meal_plan):
    print("=== RECIPE LINKS ===\n")
    for category, meal in meal_plan.items():
        print(f"{category}:")
        if isinstance(meal, dict):
            print(f"  - {meal['name']}")
            print(f"    URL: {meal['link']}\n")
        elif isinstance(meal, list):
            for m in meal:
                print(f"  - {m['name']}")
                print(f"    URL: {m['link']}\n")

# ---------------------- MAIN MENU ----------------------

# --- COLOR CODES (for terminal) ---
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def intro_page():
    clear_screen()
    print(CYAN + BOLD + "=" * 50 + RESET)
    print(GREEN + BOLD + "      🍽️  FILIPINO MEAL PLANNER SYSTEM  🍽️" + RESET)
    print(CYAN + "=" * 50 + RESET)
    print(YELLOW +
          "\nWelcome to the Filipino Meal Planner!\n"
          "This program helps you create personalized Filipino\n"
          "meal plans based on your body stats, lifestyle, and goal.\n"
          "You'll receive your daily calorie and macronutrient\n"
          "requirements along with recommended meals.\n" + RESET)
    print(GREEN + "Developed by: GROUP 4 \n" + RESET)

    # --- Loading Animation ---
    print(CYAN + "Loading system", end="", flush=True)
    for _ in range(3):
        time.sleep(0.6)
        print(".", end="", flush=True)
    time.sleep(0.4)
    print(RESET + "\n")
    input("Press ENTER to continue...")
    clear_screen()


def main_menu():
    meals = load_meals()
    users = load_user_data()

    # --- SHOW INTRO ---
    intro_page()

    while True:
        print(CYAN + BOLD + "\n=== FILIPINO MEAL PLANNER ===" + RESET)
        print("1. New User")
        print("2. Old User")
        print("3. Exit")

        choice = input(YELLOW + "Enter choice (1-3): " + RESET).strip()

        if choice == "1":
            # --- Name ---
            while True:
                name = input("Enter your name: ").strip().title()
                if name.replace(" ", "").isalpha():
                    break
                print(RED + " Invalid name. Please enter letters only." + RESET)

            # --- Age ---
            while True:
                age_input = input("Enter your age: ").strip()
                if age_input.isdigit() and 5 <= int(age_input) <= 120:
                    age = int(age_input)
                    break
                print(RED + " Invalid age. Enter a number between 5 and 120." + RESET)

            # --- Sex ---
            while True:
                sex = input("Enter your sex (male/female): ").strip().lower()
                if sex in ["male", "female"]:
                    break
                print(RED + " Invalid input. Type 'male' or 'female'." + RESET)

            # --- Height ---
            while True:
                try:
                    height = float(input("Enter your height (cm): ").strip())
                    if 50 <= height <= 250:
                        break
                    print(RED + " Invalid height. Enter between 50 cm and 250 cm." + RESET)
                except ValueError:
                    print(RED + " Please enter a valid number." + RESET)

            # --- Weight ---
            while True:
                try:
                    weight = float(input("Enter your weight (kg): ").strip())
                    if 20 <= weight <= 300:
                        break
                    print(RED + " Invalid weight. Enter between 20 kg and 300 kg." + RESET)
                except ValueError:
                    print(RED + " Please enter a valid number." + RESET)

            # --- Activity Level ---
            print(CYAN + "\nActivity Level:" + RESET)
            print("1 - Sedentary (little or no exercise)")
            print("2 - Lightly Active (light exercise 1–3 days/week)")
            print("3 - Moderately Active (exercise 3–5 days/week)")
            print("4 - Very Active (hard exercise 6–7 days/week)")
            print("5 - Extra Active (physical job or twice-a-day training)")

            while True:
                activity_input = input("Enter activity level (1-5): ").strip()
                if activity_input.isdigit() and 1 <= int(activity_input) <= 5:
                    activity = int(activity_input)
                    break
                print(RED + " Invalid choice. Enter a number between 1 and 5." + RESET)

            # --- Goal ---
            print(CYAN + "\nGoal Options:" + RESET)
            print("1 - Lose Weight")
            print("2 - Maintain Weight")
            print("3 - Gain Weight")

            while True:
                goal_input = input("Enter your goal (1-3): ").strip()
                if goal_input in ["1", "2", "3"]:
                    goal = goal_input
                    break
                print(RED + " Invalid choice. Enter 1, 2, or 3." + RESET)

            # --- Calculate and Save ---
            macros = calculate_tdee(weight, height, age, sex, activity, goal)
            meal_plan, total_cal = generate_meal_plan(macros["Calories"], meals)

            users[name] = {
                "age": age,
                "sex": sex,
                "height": height,
                "weight": weight,
                "macros": macros,
                "meal_plan": meal_plan,
                "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            save_user_data(users)

            display_summary(name, macros, meal_plan, total_cal)

            # --- Post Menu ---
            while True:
                opt = input("Select option (1-3): ").strip()
                if opt == "1":
                    show_links(meal_plan)
                elif opt == "2":
                    print(GREEN + "Goodbye!" + RESET)
                    return
                elif opt == "3":
                    break
                else:
                    print(RED + " Invalid choice. Try again." + RESET)

        elif choice == "2":
            if not users:
                print(RED + " No records found. Please register first." + RESET)
                continue

            print(CYAN + "\n=== OLD USER RECORDS ===" + RESET)
            for i, user_name in enumerate(users.keys(), start=1):
                print(f"{i}. {user_name}")

            while True:
                select_input = input("Select user number: ").strip()
                if select_input.isdigit() and 1 <= int(select_input) <= len(users):
                    select = int(select_input)
                    break
                print(RED + " Invalid selection. Choose a valid user number." + RESET)

            name = list(users.keys())[select - 1]
            user = users[name]

            print(f"\nLoaded record for {name}")
            display_summary(name, user["macros"], user["meal_plan"], user["macros"]["Calories"])

            while True:
                opt = input("Select option (1-3): ").strip()
                if opt == "1":
                    show_links(user["meal_plan"])
                elif opt == "2":
                    print(GREEN + "Goodbye!" + RESET)
                    return
                elif opt == "3":
                    break
                else:
                    print(RED + " Invalid choice. Try again." + RESET)

        elif choice == "3":
            print(GREEN + " Exiting... Goodbye!" + RESET)
            break
        else:
            print(RED + " Invalid choice. Please enter 1, 2, or 3." + RESET)

# ---------------------- RUN PROGRAM ----------------------
if __name__ == "__main__":
    main_menu()
         