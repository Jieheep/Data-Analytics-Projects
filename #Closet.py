import requests
import json
import csv
from datetime import datetime

def record_outfit():
    # Get current date and time
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y %H:%M:%S")
    
    # Display occasion options and get user input
    categories = ['Tennis', 'Golf', 'Every Day', 'Gym', 'Other']
    print("Select the occasion from the following list:")
    for index, category in enumerate(categories):
        print(f"{index + 1}. {category}")
    occasion_index = int(input("Enter the number of the occasion: ")) - 1
    occasion = categories[occasion_index]
    print(occasion_index)
    print(occasion)
    
    # Display clothing categories and get user input
    clothing_types = {'Crop': ['Dance Studio Crop'], 'Jacket': ['Down for it all Jacket'], \
                   'Jogger': ['Adapted State Jogger', 'Beyond the Studio Jogger', 'Dance Studio Jogger', 'Dance Studio Jogger *Lined*', 'On the Fly Jogger', 'Ready to Rulu Jogger', 'Scuba High-Rise French Terry Jogger'],\
                     'Legging': ['Fast and Free Tight', 'In Movement', 'Power Thru Tight', 'Speed up Tight *Brushed*', 'Wunder Train Crop', 'Wunder Train Tight', 'Zoned in Tight'], \
                     'Long Sleeve': ['Metal Vent Long Sleeve', 'Swiftly Breathe Long Sleeve', 'Swiftly Tech Long Sleeve'], 'Pant': ['Dance Studio Pant', 'Dance Studo Pant', 'Keep Moving Pant', 'On the Fly Pant'],\
                       'Short Sleeve': ['Metal Vent Short Sleeve', 'Time to Restore Mock Neck Short Sleeve'], 'Shorts': ['City Sleek Shorts', 'Hotty Hot Shorts', 'On the Fly Shorts', 'Soft Ambition Shorts', 'Speed up Shorts', 'Stroll at Sundown Shorts', 'Track That Shorts', 'Tracker Shorts'], \
                         'Skirts': ['Court Rival Skirt', 'Hotty Hot Skirt', 'Pace Rival Skirt', 'Play off the pleats skirt'], 'Sports Bras': ['Always Aligned Bra', 'Ebb to Train', 'Energy Bra', 'Energy Bra High Neck Long Line Zip Special Edition', 'Energy Bra Longline', 'Flow Y Bra *Long line*', 'Free to be Wild Bra', 'Free to be Wild Bra *peak*', 'Free to be Wild Bra Longline', 'Ribbed Back-Twist Yoga Bra'], \
                           'Sweater': ['All Yours Cropped Hoodie', 'All Yours Hoodie', 'Define Jacket', 'Engineered Warmth Half-Zip', "It's Rulu Half Zip", 'Scuba Full Zip', 'Scuba Half Zip'], 'T-Shirt': ['All Yours Crop T-Shirt', 'All Yours Tee', 'All Yours Tee *Spray', 'Back in Action T-Shirt', 'Knot Stopping Tee', 'LA All Yours Boxy Crop T-Shirt', 'Swiftly Tech Short Sleeve', 'Train to be T-Shirt'], \
                             'Tank Top': ['Align Tank', 'Align Tank *Diamond Dye', 'Align Tank *Gold', 'All Tied Up Tank', 'All Yours Crop Tank *Wash', 'Back in Action Tank', 'Base Pace Tank *Ribbed', 'Cinch it Up Tank', 'Ebb to Street Tank', 'Essential Tank', 'Find Your Pace Tank', 'High Neck Align Tank', 'Keep UR Cool Racer', 'Power Pivot Tank', 'Power Pivot Tank *Rib',  'Sculpt Tank', 'Sculpt Tank Cropped', 'Sleeveless Golf Polo', 'Swiftly Tech Tank', 'Train to be Tank *Shibori*', 'Wild Tank']}
    colours = {'Adapted State Jogger': ['Mineral Blue'], 'Beyond the Studio Jogger': ['Cadet Blue'], 'Dance Studio Crop': ['Black', 'Dark Olive', 'Graphite Grey', 'Chambray', 'Grey Sage'], 'Dance Studio Jogger': ['Black', 'Cadet Blue', 'Navy', 'Dark Chrome', 'Garnet', 'Briar Rose', 'Half moon'], 'Dance Studio Jogger *Lined*': ['Vapor'], 'Dance Studio Pant': ['Vapor'], 'Dance Studo Pant': ['Black', 'Iron Blue'], \
               'Fast and Free Tight': ['Cassis', 'Incognito Camo Multi Grey ', 'Game Day Red Black Multi', 'Ice Wash Violet Verbena'], 'In Movement': ['Black'], 'Keep Moving Pant': ['Savannah'], 'On the Fly Jogger': ['True Navy'], 'On the Fly Pant': ['Grey Sage', 'Black'], 'Power Thru Tight': ['Mulled Wine', 'Black'], 'Ready to Rulu Jogger': ['Black', 'Heatherd True Navy'], 'Scuba High-Rise French Terry Jogger': ['Heathered Core Ultra Light Grey'], \
                'Speed up Tight *Brushed*': ['True Navy', 'Black'], 'Wunder Train Crop': ['Chambray', 'Blue Nile', 'Diamond Dye Shade Naval Blue', 'Savannah'], 'Wunder Train Tight': ['Smoked Spruce'], 'Zoned in Tight': ['Black'], 'City Sleek Shorts': ['Black', 'Spiced Chai'], 'Hotty Hot Shorts': ['Poco Logo Foil Amber Orange', 'Daydream', 'Savannah', 'Midnight Navy', 'Vitalize Multi/Black', 'Dark Red', 'Rosemary Green', 'Icing Blue', 'Sunset', 'True Navy', 'Heather Lux Multi Violet Verbena', 'Heather Lux Multi Black', 'Aquila Black Multi/ Black', 'Kaleidofloral Multi/ Blue Cast', 'Ripened Raspberry', 'Heritage 365 Camo Dark Olive Multi', 'No Limits White Multi'],\
                      'On the Fly Shorts': ['Black', 'Wee are From Space Nimbus Battleship/ Alpine White'], 'Soft Ambition Shorts': ['Beechwood'], 'Speed up Shorts': ['Black', 'White', 'Scarlet ', 'Heathered Willow Green', 'Lucid Lime', 'Midnight Navy', 'Incognito Camo Multi Grey '], 'Stroll at Sundown Shorts': ['Spiced Chai', 'Hype Stripe Raceway Grey White'], 'Track That Shorts': ['Rapid Flourish Multi', 'Floral Electric Multi', 'Pale Raspberry', 'Pink Puff'], 'Tracker Shorts': ['Velocity Mesh Island Mist Black', 'Island Mist', 'Le Tigre Camo Deep Coal Multi/ Black', 'Floral Metropolis Multi'], \
                        'Court Rival Skirt': ['White', 'Strawberry Milkshake', 'Dark Red', 'Black', 'True Navy', 'Blue Nile', 'Heather Lux Multi Black/ Black', 'Pink Savannah', 'Cherry Tint', 'Pale Raspberry', 'Poolside', 'Strawberry Milkshake'], 'Hotty Hot Skirt': ['True Navy', 'White'], 'Pace Rival Skirt': ['Sonic Pink', 'Tide Water Teal', 'Heather Lux Multi Black/ Black', 'Delicate Mint', 'True Navy', 'Black', 'City Breeze Alpine White Multi', 'Dark Prism Pink'], 'Play off the pleats skirt': ['Everglade '], 'Always Aligned Bra': ['Black', 'Savannah'], 'Ebb to Train': ['Grey Sage', 'Iron Blue'], \
                            'Energy Bra': ['Pink Punch', 'Ombre Speckle Stop Jacquard Interlock Power Luxtreme Black Blazer Blue', 'Breezy', 'Incognito Camo Multi Grey '], 'Energy Bra High Neck Long Line Zip Special Edition': ['White'], 'Energy Bra Longline': ['Floral Electric Multi', 'Dark Red', 'Scattered Herringbone Black White'], 'Flow Y Bra *Long line*': ['Indigo Lace Starlight Multi'], 'Free to be Wild Bra': ['True Navy/ Pink Puff', 'Formation Camo Deep Coal Multi'], 'Free to be Wild Bra ': ['Deep Fuschia', 'Green Twill', 'Lemon Vibe', 'Hideaway Camo Deep Coal Multi', 'Pink Mist', 'Date Brown', 'Incognito Multi Camo Alpine white', 'Icing Blue', 'White', 'True Navy/ Flush Pink', 'Offbeat Alpine White Black/ Highlight Yellow'], \
                                'Free to be Wild Bra *peak*': ['Larkspur'], 'Free to be Wild Bra Longline': ['Water Blossom', 'Vintage Plum'], 'Ribbed Back-Twist Yoga Bra': ['Charged Indigo'], 'Align Tank': ['Botanical Bloom Anchor Multi', 'Ancient Copper', 'Lavender Dew'], 'Align Tank *Diamond Dye': ['Diamond Dye Cassis Black'], 'Align Tank *Gold': ['Black '], 'All Tied Up Tank': ['Yachtie Stripe Black Chrome', 'Autumn Red'], 'All Yours Crop T-Shirt': ['Autumn Red'], 'All Yours Crop Tank *Wash': ['Cloudy Wash True Navy'], 'All Yours Tee ': ['Black'], 'All Yours Tee *Spray': ['Vertical Spray Dye Chrome Violet Verbena'], 'Back in Action T-Shirt': ['Short Serve Stripe Heathered Spiced Chai White'], 'Back in Action Tank': ['Quick Sand'], \
                                    'Base Pace Tank *Ribbed': ['Scream Green Light', 'Silver Blue'], 'Cinch it Up Tank': ['Black'], 'Ebb to Street Tank': ['Peri Purple'], 'Essential Tank': ['White'], 'Find Your Pace Tank': ['Violet Verbena'], 'High Neck Align Tank': ['Pink Taupe'], 'Keep UR Cool Racer': ['Citrus Ice'], 'Knot Stopping Tee': ['White'], 'LA All Yours Boxy Crop T-Shirt': ['Heathered Grey'], 'Metal Vent Long Sleeve': ['Chambray/White'], 'Metal Vent Short Sleeve': ['Rainforest Green/Pink Lychee'], 'Power Pivot Tank ': ['Black'], 'Power Pivot Tank *Rib': ['White'], 'Sculpt Tank': ['Sonic Pink', 'Mulled Wine', 'Icing Blue', 'White'], 'Sculpt Tank Cropped': ['Delicate Mint'], 'Sleeveless Golf Polo': ['Dew Pink'],\
                                          'Swiftly Breathe Long Sleeve': ['Delicate Mint', 'Ancient Copper'], 'Swiftly Tech Long Sleeve ': ['Wee Are From Space White', 'Black', 'Pink Savannah / Pink Mist'], 'Swiftly Tech Short Sleeve': ['Iron Purple', 'Wisteria Purple', 'Black', 'Pink Punch', 'Tempo Stripe White/Black', 'Forest Green/Green Twill', 'Spiced Chai', 'Wild Mint', 'White'], 'Swiftly Tech Tank': ['Water Surface Copper Brown / Bold Beige', 'Iron Blue', 'Slate/White', 'Dark Prism Pink/ White', 'Lavender Dew', 'Sunset', 'Wisteria Purple/Lavender Dew'], 'Time to Restore Mock Neck Short Sleeve': ['Iron Blue / White'], 'Train to be T-Shirt': ['Blue Linen/Chalk Wash Water Drop'], 'Train to be Tank *Shibori*': ['Deep Coal'], \
                                            'Wild Tank': ['Tiger Space Dye Black White / Deep Coal'], 'All Yours Cropped Hoodie': ['Sonic Pink'], 'All Yours Hoodie': ['White', 'Feather Pink'], 'Define Jacket': ['Ice Wash Asphalt Grey'], 'Down for it all Jacket': ['Chambray'], 'Engineered Warmth Half-Zip': ['Light Ivory'], "It's Rulu Half Zip": ['Incognito Mult Camo Grey'], 'Scuba Full Zip': ['Blue Nile'], 'Scuba Half Zip': ['Heather Core Light Ultra Grey', 'Black', 'Pink Blossom', 'Date Brown']}

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

    torecord = [date_time, occasion]
    torecord.extend(selections)
    return torecord

print(record_outfit())


