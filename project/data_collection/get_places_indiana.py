import requests


def get_places_by_state(api_key: str, state_code: int):
    base_url = "https://api.census.gov/data/2021/acs/acs5"

    params = {
        "get": "NAME",
        "for": "place:*",
        "in": f"state:{state_code}",
        "key": api_key,
    }

    # Make the API call
    response = requests.get(base_url, params=params)

    # Process the response
    if response.status_code == 200:
        data = response.json()
        return [place[0] for place in data[1:]]  # Skip header row
    else:
        print(f"Error fetching data: {response.status_code}")


# 1. Fetch all places in Indiana
places_in_indiana = get_places_by_state(api_key="YOUR_API_KEY", state_code=18)
print(places_in_indiana)
