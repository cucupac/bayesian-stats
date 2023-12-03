import requests
from nwi_cities import NWI_CITIES

api_key = "YOUR API KEY"
data_field = "B19013_001E"  # ACS variable for median household income


def get_median_income(state_code, place_code, api_key):
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
        # Extract and process the median household income from the response
        income_data = data[1][0] if len(data) > 1 else "Data not found"
        return income_data
    else:
        print(f"Error fetching data: {response.status_code} - {response.text}")
        return "Error"


median_incomes = {}
for city, info in NWI_CITIES.items():
    state_code = "18"  # Indiana
    place_code = info["fips_code"]
    median_income = get_median_income(
        state_code, place_code[-5:], api_key
    )  # Last 5 digits are the place code
    median_incomes[city] = median_income

# Print Results
for city, income in median_incomes.items():
    print(f"{city}: {income}")
