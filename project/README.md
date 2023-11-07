# Weather and AQI Reporter
#### Video Demo:  <URL HERE>
#### Description:
I came up with this program due to recent events in my hometown of Jakarta, Indonesia. This year (2023), the air pollution in Jakarta has been extremely bad. Based on the Air Quality Index (or AQI), particularly for PM2.5 particles, Jakarta has had the highest pollution in the world on multiple occasions.

As a result of the bad pollution, I have begun monitoring my local AQI readings on a daily basis. This inspire me to create my own program where I can use an Air Visual's API to pull data to see both the current weather and AQI readings for any city in the world.

The program starts with a greeting and then prompts the user to input the location they want to search from. The user must input 3 variables: a valid country, a valid state in that country, and a valid city in that state. There is a function to get user input for each of these variables: get_user_country(api_key), get_user_state(api_key, country), and get_user_city(api_key, country, state)

Additionally, there are 3 functions to help validate the user input for each of the above variables: get_valid_countries(api_key), get_valid_states(api_key, country), and get_valid_cities(api_key, country, state). get_valid_countries(api_key) returns a list of all the valid countries available from the API. This list is then used in get_user_country(api_key) to validate whether the user's input is in the valid countries list. get_valid_states and get_valid_cities works in a similar manner to compare with user input for each variable.

Once the user has input a valid country, state, and city, the program calls get_data() and makes an API call to get the current weather and pollution data in the selected city.

Next, a menu will appear with 4 options for the user to input. Option [1] shows the current weather data, option [2] shows the current pollution data, and option [3] shows both the weather and pollution data. The program will continue prompting the user to select which option to print for the selected city until option [0] is selected, which exits the program.
