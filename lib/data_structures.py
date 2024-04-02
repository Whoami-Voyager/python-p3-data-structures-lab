spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [food["name"] for food in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    icespice = []
    for spice in spicy_foods:
        if spice["heat_level"] > 5:
            icespice.append(spice)
    return icespice

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level_emojis = "🌶" * food['heat_level']
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if cuisine is food['cuisine']:
            return food

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            heat_level_emojis = "🌶" * food['heat_level']
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")

def get_average_heat_level(spicy_foods):
    spice = []
    for heat in spicy_foods:
        spice.append(heat['heat_level'])
    spice_average = sum(spice)/len(spice)
    return spice_average

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
