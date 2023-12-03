import pandas as pd
import os

from fastfood import FAST_FOOD_LIST


# Function to calculate the percentage of fast food restaurants
def calculate_fast_food_percentage(city_restaurants):
    total_restaurants = len(city_restaurants)
    fast_food_count = sum(
        restaurant in FAST_FOOD_LIST for restaurant in city_restaurants
    )
    return (fast_food_count / total_restaurants) if total_restaurants > 0 else 0


# Process each CSV file
csv_directory = "project/restaurants"
fast_food_percentages = {}
for filename in os.listdir(csv_directory):
    if filename.endswith(".csv"):
        city_name = filename.split(".")[0]
        csv_path = os.path.join(csv_directory, filename)
        data = pd.read_csv(csv_path)

        # Filter and get list of restaurant names
        restaurant_names = data["name"].tolist()

        # Calculate the percentage and store it
        fast_food_percentages[city_name] = calculate_fast_food_percentage(
            restaurant_names
        )

# Print the results
for city, percentage in fast_food_percentages.items():
    print(f"{city}: {percentage:.4f}")
