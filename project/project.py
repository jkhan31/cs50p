import json
import requests
import sys


def main():
    my_api_key = "e42058b7-5613-4952-974c-d877629c6524"

    print("Welcome to Weather and Air Quality Index Reporter")

    # User inputs location queries data for the location
    query_data, country, state, city = get_location_data(my_api_key)

    # User selects what data to show
    while True:
        choice = choose_display_data_menu()
        if choice =='4':
            query_data, country, state, city = get_location_data(my_api_key)
        else:
            display_data(query_data, choice, country, state, city)

def get_location_data(api_key):
    print("Please input a location")
    country = get_user_country(api_key)
    state = get_user_state(api_key, country)
    city = get_user_city(api_key, country, state)
    print(f"Looking up data in {city}, {state}, {country}")
    return get_data(api_key, country, state, city), country, state, city

def get_valid_countries(api_key):
    url = f"https://api.airvisual.com/v2/countries?key={api_key}"
    response = requests.get(url)
    countries = []
    # print(json.dumps(response.json(), indent=4))
    for data in response.json()["data"]:
        countries.append(data["country"].upper())
    # countries = [data['country'].upper() for data in response.json()['data']]
    # print(json.dumps(response.json(), indent=2))
    # print(countries)
    return countries


def get_valid_states(api_key, country):
    url = f"https://api.airvisual.com/v2/states?country={country}&key={api_key}"
    # print(url)
    response = requests.get(url)
    states = []
    for data in response.json()["data"]:
        states.append(data["state"].upper())
    # states = [data['state'].upper() for data in response.json()['data']]
    # print(states)
    return states


def get_valid_cities(api_key, country, state):
    url = f"https://api.airvisual.com/v2/cities?country={country}&state={state}&key={api_key}"
    # print(url)
    response = requests.get(url)
    cities = []
    for data in response.json()["data"]:
        cities.append(data["city"].upper())

    # cities = [data['city'].upper() for data in response.json()['data']]
    # print(json.dumps(response.json(), indent=2))
    # print(cities)
    return cities


def get_user_country(api_key):
    valid_countries = get_valid_countries(api_key)
    while True:
        try:
            user_country = input(f'Input COUNTRY or "SHOW": ').strip().upper()
            if user_country == "SHOW":
                print("Input one of the following countries:")
                for country in valid_countries:
                    print(country)
            elif user_country not in valid_countries:
                raise ValueError
            else:
                return user_country
        except ValueError:
            print("Invalid country")
            pass


def get_user_state(api_key, country):
    valid_states = get_valid_states(api_key, country)
    while True:
        try:
            user_state = input(f'Input STATE or "SHOW": ').strip().upper()
            if user_state == "SHOW":
                print("Input one of the following states:")
                for state in valid_states:
                    print(state)
            elif user_state not in valid_states:
                raise ValueError
            else:
                return user_state
        except ValueError:
            print("Invalid state")
            pass


def get_user_city(api_key, country, state):
    valid_cities = get_valid_cities(api_key, country, state)
    while True:
        try:
            user_city = input(f'Input CITY or "SHOW": ').strip().upper()
            if user_city == "SHOW":
                print("Input one of the following states:")
                for city in valid_cities:
                    print(city)
            elif user_city not in valid_cities:
                raise ValueError
            else:
                return user_city
        except ValueError:
            print("Invalid city")
            pass


def get_data(api_key, country, state, city):
    url = f"https://api.airvisual.com/v2/city?city={city}&state={state}&country={country}&key={api_key}"
    # print(url)
    response = requests.get(url)
    data = response.json()
    # print(json.dumps(data, indent=4))
    return data


def get_weather_data(data, country, state, city):
    w_header = f"Weather in {city}, {state}, {country}:"
    temp = f"Temperature: {data['data']['current']['weather']['tp']}°C"
    humidity = f"Humidity: {data['data']['current']['weather']['hu']}%"
    wind = f"Wind Speed: {data['data']['current']['weather']['ws']} m/s"
    return w_header + "\n" + temp + "\n" + humidity + "\n" + wind


def get_pollution_data(data, country, state, city):
    p_header = f"Pollution in {city}, {state}, {country}:"
    aqi = f"AQI (Air Quality Index): {data['data']['current']['pollution']['aqius']}"
    pollutant = f"Main Pollutant: {data['data']['current']['pollution']['mainus']}"
    return p_header + "\n" + aqi + "\n" + pollutant


def choose_display_data_menu():
    print("--------MENU--------")
    print("[1] Current Weather")
    print("[2] Current Pollution")
    print("[3] Both")
    print("[4] Enter new location")
    print("[0] Exit program")
    while True:
        choice = input(
            "What data do you want to see? (Input number from options above) "
        ).strip()
        try:
            if choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "0":
                return choice
            else:
                raise ValueError
        except:
            print("Invalid input")
            pass


def display_data(data, choice, country, state, city):
    if choice == "1":
        print("\n")
        print(get_weather_data(data, country, state, city))
        print("\n")
    elif choice == "2":
        print("\n")
        print(get_pollution_data(data, country, state, city))
        print("\n")
    elif choice == "3":
        print("\n")
        print(get_weather_data(data, country, state, city))
        print("\n")
        print(get_pollution_data(data, country, state, city))
        print("\n")
    elif choice == "0":
        sys.exit("Goodbye!")


if __name__ == "__main__":
    main()
