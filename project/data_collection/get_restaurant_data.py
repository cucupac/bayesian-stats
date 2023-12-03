import requests
import time
import csv

from nwi_cities import NWI_CITIES

API_KEY = "YOUR_API_KEY"


def get_restaurant_details(restaurant):
    """Extracts required details from a restaurant JSON object"""
    details = {
        "business_status": restaurant.get("business_status"),
        "name": restaurant.get("name"),
        "latitude": restaurant["geometry"]["location"]["lat"],
        "longitude": restaurant["geometry"]["location"]["lng"],
        "is_meal_takeaway": "meal_takeaway" in restaurant.get("types", []),
        "rating": restaurant.get("rating"),
        "user_ratings_total": restaurant.get("user_ratings_total"),
        "price_level": restaurant.get("price_level"),
    }
    return details


def get_restaurants(api_key: str, location: str, radius: int, place_type: str):
    base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    restaurants = []
    next_page_token = None
    query_count = 0  # Counter for the number of queries made

    while True:
        params = {
            "location": location,
            "radius": radius,
            "type": place_type,
            "key": api_key,
        }

        if next_page_token:
            params["pagetoken"] = next_page_token

        response = requests.get(base_url, params=params)
        query_count += 1  # Increment the query count

        if response.status_code == 200:
            data = response.json()
            restaurants.extend(
                [get_restaurant_details(r) for r in data.get("results", [])]
            )

            next_page_token = data.get("next_page_token")
            if not next_page_token:
                break

            time.sleep(2)  # Delay for API limits
        else:
            print(f"Error fetching data: {response.status_code}")
            break

    print(f"Total number of queries made: {query_count}")
    return restaurants


def write_to_csv(filename, data):
    """Writes data to a CSV file"""
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)


# Modify the main part of the script to loop through each city
for city_name, city_data in NWI_CITIES.items():
    print(f"Processing data for {city_name}...")
    location = f"{city_data['lat']},{city_data['lng']}"
    city_filename = f"{city_name.replace(' ', '_')}_restaurants.csv"

    # Fetch restaurants for this city
    restaurants_data = get_restaurants(
        api_key=API_KEY, location=location, radius=5000, place_type="restaurant"
    )
    if restaurants_data:
        write_to_csv(city_filename, restaurants_data)
        print(
            f"Data written to {city_filename}. Total restaurants: {len(restaurants_data)}"
        )
    else:
        print(f"No data to write for {city_name}.")

    time.sleep(2)  # Add a short delay between API calls for different cities
