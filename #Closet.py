import requests
import json
import csv
from datetime import datetime

def record_outfit():
    # Get current date and time
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y %H:%M:%S")

    # Get current weather information
    info = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Waterloo,Canada&units=metric&APPID=2a208e91572499972c72ba6cc6e84a5f')
    weather = info.json()
    feels_like = weather['main']['feels_like']

    
    # Display occasion options and get user input
    categories = ['Tennis', 'Golf', 'Every Day', 'Gym', 'Other']
    print("Select the occasion from the following list:")
    for index, category in enumerate(categories):
        print(f"{index + 1}. {category}")
    occasion_index = int(input("Enter the number of the occasion: ")) - 1
    occasion = categories[occasion_index]
    
    # Display clothing categories and get user input
    with open('databaseset.csv', 'r') as f:
        reader = csv.reader(f, delimiter= ',')

        header = reader.__next__() #[Product Type,....]

        clothing_types = {}
        for row in reader:
            product_name, product_type = row[0], row[1]
            if product_type not in clothing_types:
                clothing_types[product_type] = set()
            clothing_types[product_type].add(row[0])
        for ctype in clothing_types:
            clothing_types[ctype] = list(clothing_types[ctype])

        f.seek(0)
        reader.__next__()
        colours = {}


        for row in reader:
            colour, product_name = row[2], row[0]
            if product_name not in colours:
                colours[product_name] = [colour]
            else:
                colours[product_name].append(colour)
 

    categories = ['Crop', 'Jacket', 'Jogger', 'Legging', 'Long Sleeve', 'Pant', 'Short Sleeve', 'Shorts', 'Skirts', 'Sports Bras', 'Sweater', 'T-Shirt', 'Tank Top']
    clothing_categories = []
    while True:
        print("\nPlease choose the clothing categories you wore from the following options:")
        for i, category in enumerate(categories):
            print(f"{i+1}. {category}")
        user_input = input("Enter the corresponding number (or 'done' if finished): ")
        if user_input.lower() == 'done':
            break
        elif user_input.isnumeric() and int(user_input) in range(1, len(categories)+1):
            clothing_categories.append(categories[int(user_input)-1])
        else:
            print("Invalid input, please try again.")

    # Initialize an empty dictionary to store the user's selections
    selections = []

    # Loop through the categories and prompt the user to select a clothing type for each one
    for category in clothing_categories:
        print(f"Available {category} types:")
        for i, item in enumerate(clothing_types[category]):
            print(f"{i + 1}. {item}")
        # Prompt the user to select a clothing type
        selection = int(input(f"Enter the number of the {category} type you wore: "))
        # Add the user's selection to the dictionary
        clothing_name = clothing_types[category][selection - 1]
        for i, colour in enumerate(colours[clothing_name]):
            print(f"{i+1}. {colour}")
        chosen_colour = int(input(f"Enter the number of the {clothing_name} colour you wore: "))
        selections.append([clothing_types[category][selection - 1], colours[clothing_name][chosen_colour - 1]])

    torecord = [date_time,(f'Temperature: {feels_like} °C'), occasion]
    torecord.extend(selections)
    return torecord


