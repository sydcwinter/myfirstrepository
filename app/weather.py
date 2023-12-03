import pgeocode
from pgeocode import Nominatim

import requests
import json
from pandas import DataFrame
from IPython.display import Image, display


degree_sign = u"\N{DEGREE SIGN}"


##Part 1
def get_location(zip_code):
    nomi = pgeocode.Nominatim('US')
    results = nomi.query_postal_code(zip_code)

    print(results)
    print(type(results))

    print("LOCATION:", f"{results['place_name']}, {results['state_code']}")
    print("LAT:", results["latitude"])
    print("LON:", results["longitude"])
    return results


##Part 2

# display images in a dataframe in colab

def display_forecast(longitude, latitude):
    """
    Displays a seven day weather forecast for the provided zip code.

    Params :

        country_code (str) a valid country code (see supported country codes list). Default is "US".

        zip_code (str) a valid US zip code, like "20057" or "06510".

    """


    request_url = f"https://api.weather.gov/points/{latitude},{longitude}"
    response = requests.get(request_url)
    print(response.status_code)
    parsed_response = json.loads(response.text)

    forecast_url = parsed_response["properties"]["forecast"]
    forecast_response = requests.get(forecast_url)
    print(forecast_response.status_code)
    parsed_forecast_response = json.loads(forecast_response.text)

    periods = parsed_forecast_response["properties"]["periods"]
    daytime_periods = [period for period in periods if period["isDaytime"] == True]

    for period in daytime_periods:
        #print(period.keys())
        print("-------------")
        #print(period["name"], period["startTime"][0:7])
        print(period["shortForecast"], f"{period['temperature']} {degree_sign}{period['temperatureUnit']}")
        #print(period["detailedForecast"])
        #display(Image(url=period["icon"]))

    return len(daytime_periods) 

if __name__ == "__main__":
    location_results = get_location("20007")

    longitude = float(location_results["longitude"])
    latitude = float(location_results["latitude"])
    zipcode = location_results["postal_code"]

    display_forecast(longitude, latitude)