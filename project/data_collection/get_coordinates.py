from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="indiana_geocoder")


def get_coordinates(city_name, state_code="IN"):
    location = geolocator.geocode(f"{city_name}, {state_code}, USA")
    if location:
        return {"lat": location.latitude, "lng": location.longitude}
    else:
        return {"lat": "Not found", "lng": "Not found"}


# Cleaned up city names
lake_county_cities = [
    "Cedar Lake",
    "Crown Point",
    "Dyer",
    "East Chicago",
    "Gary",
    "Griffith",
    "Hammond",
    "Highland",
    "Hobart",
    "Lake Station",
    "Leroy",
    "Lowell",
    "Merrillville",
    "Munster",
    "Saint John",
    "Schererville",
    "Schneider",
    "Shelby",
    "Whiting",
]

porter_county_cities = [
    "Beverly Shores",
    "Boone Grove",
    "Burns Harbor",
    "Chesterton",
    "Hebron",
    "Kouts",
    "Ogden Dunes",
    "Portage",
    "Porter",
    "South Haven",
    "Valparaiso",
    "Wheeler",
]

nwi_cities = {}

# Fetch coordinates for Lake County cities and add them to the dictionary
for city in lake_county_cities:
    nwi_cities[city] = get_coordinates(city)
    nwi_cities[city]["county"] = "Lake County"

# Fetch coordinates for Porter County cities and add them to the dictionary
for city in porter_county_cities:
    nwi_cities[city] = get_coordinates(city)
    nwi_cities[city]["county"] = "Porter County"

# Print the final dictionary
for city, details in nwi_cities.items():
    print(f'"{city}": {details},')
