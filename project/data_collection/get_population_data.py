import requests
from nwi_cities import NWI_CITIES

api_key = "YOUR_API_KEY"
data_field = "B01003_001E"  # ACS variable for population


def get_population(state_code, place_code, api_key):
    url = f"https://api.census.gov/data/2021/acs/acs5"
    params = {
        "get": data_field,
        "for": f"place:{place_code}",
        "in": f"state:{state_code}",
        "key": api_key,
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        # Extract and process the population from the response
        population_data = data[1][0] if len(data) > 1 else "Data not found"
        return population_data
    else:
        print(f"Error fetching data: {response.status_code} - {response.text}")
        return "Error"


population_data = {}
for city, info in NWI_CITIES.items():
    state_code = "18"  # Indiana
    place_code = info["fips_code"]
    population = get_population(
        state_code, place_code[-5:], api_key
    )  # Last 5 digits are the place code
    population_data[city] = population

# Print Results
for city, population in population_data.items():
    print(f'"{city}": {population},')
