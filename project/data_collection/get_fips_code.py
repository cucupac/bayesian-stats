"""This file obtains FIPS codes for all cities in NWI."""
import requests
import json

from nwi_cities import NWI_CITIES


def get_fips_code(lat, lng):
    url = f"https://geocoding.geo.census.gov/geocoder/geographies/coordinates?x={lng}&y={lat}&benchmark=Public_AR_Current&vintage=Current_Current&layers=160&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        geocode_data = response.json()
        places = geocode_data["result"]["geographies"].get("Incorporated Places")
        if places:
            place_info = places[0]
            return place_info["GEOID"]
    return None


fips_codes = {}
for city, info in NWI_CITIES.items():
    fips_code = get_fips_code(info["lat"], info["lng"])
    fips_codes[city] = fips_code
    if not fips_code:
        print(f"No FIPS code found for {city}")

print(json.dumps(fips_codes, indent=4))
