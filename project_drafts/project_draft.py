### IQAir Quality Reporter ###

'''
API DOC = https://api-docs.iqair.com/
1. X- User input country from list, if not found, re-prompt country
2. X- List States
3. X- User input state from list, if not found, re-prompt state
4. X- List Cities
5. X- User input city from list, if not found, re-prompt city
7. Select data to show (pick from printed list)
8. Print data
'''

import json
import requests
import sys

api_key = "2c81fdee-274d-4db3-b7dd-1db18406af2c"

def main():
    print("Welcome to Air Quality Index Reporter")
    valid_countries = get_valid_country_list()
    country = get_user_country(valid_countries)
    # print(country)
    state = get_state_in_country(api_key, country)
    city = get_city(api_key, country, state)
    print(f"{city}, {state}, {country}")
    data = get_iqair_data(api_key, country, state, city)
    show_available_data(data)



# Return list of searchable countries
def get_valid_country_list():
    payload={}
    files={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload, files=files)

    o = response.json()

    country_list = []
    for result in o["data"]:
        country_list.append(result["country"].upper())
    return country_list


# Get searchable country from user input
def get_user_country(valid_countries):
    while True:
        try:
            user_country = input(f'Input COUNTRY or \"SHOW\": ').strip().upper()
            if user_country == "SHOW":
                print("Input one of the following countries:")
                for country in valid_countries:
                    print(country)
            elif user_country not in valid_countries:
                raise ValueError
            else:
                return user_country
        except ValueError:
            pass



# Get searchable state from selected country
def get_state_in_country(api_key, country_name):
    # Get list of valid states
    supported_states_url = f"http://api.airvisual.com/v2/states?country={country_name}&key={api_key}"
    payload={}
    files={}
    headers = {}

    response = requests.request("GET", supported_states_url, headers=headers, data=payload, files=files)
    o = response.json()

    valid_states = []
    for result in o["data"]:
        valid_states.append(result["state"].upper())

    while True:
        try:
            user_state = input(f'Input STATE or \"SHOW\": ').strip().upper()
            if user_state == "SHOW":
                print("Input one of the following states:")
                for state in valid_states:
                    print(state)
            elif user_state in valid_states:
                return user_state
        except ValueError:
            pass

def get_city(api_key, country_name, state_name):
    # Get list of valid states
    supported_cities_url = f"http://api.airvisual.com/v2/cities?state={state_name}&country={country_name}&key={api_key}"
    payload={}
    files={}
    headers = {}

    response = requests.request("GET", supported_cities_url, headers=headers, data=payload, files=files)
    o = response.json()

    valid_cities = []
    for result in o["data"]:
        valid_cities.append(result["city"].upper())

    while True:
        try:
            user_city = input(f'Input CITY or \"SHOW\": ').strip().upper()
            if user_city == "SHOW":
                print("Input one of the following states:")
                for city in valid_cities:
                    print(city)
            elif user_city in valid_cities:
                return user_city
        except ValueError:
            pass

# Get data for specified city from IQAir
def get_iqair_data(api_key, country_name, state_name, city_name):
    url = f"http://api.airvisual.com/v2/city?city={city_name}&state={state_name}&country={country_name}&key={api_key}"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    o = response.json()
    # print(json.dumps(o), indent=2))
    return o

def show_available_data(o):
    '''
    pollution_data = {}
    weather_data = {}

    for result in o['data']['current']:
        print(o['data']['current'][result])
         o['data']['current'][result]
    '''

def print_data(o):
    ...

if __name__ == "__main__":
    main()