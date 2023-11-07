import project
from unittest.mock import Mock

mock_api = Mock()
mock_api.get_valid_countries.return_value = ["USA", "INDONESIA"]
mock_api.get_valid_states.return_value = [
        "ACEH",
        "BALI",
        "BANGKA BELITUNG",
        "BANTEN",
        "BENGKULU",
        "CENTRAL JAVA",
        "CENTRAL KALIMANTAN",
        "CENTRAL SULAWESI"
    ]
mock_api.get_valid_cities.return_value = [
        "BANDUNG",
        "BEKASI",
        "BOGOR",
        "CIBINONG",
        "CILEUNGSIR",
        "CIREBON",
        "DEPOK",
        "KARAWANG",
        "PASARKEMIS",
        "SERPONG"
    ]

mock_api.get_data.return_value = {
    "status": "success",
    "data": {
        "city": "Ann Arbor",
        "state": "Michigan",
        "country": "USA",
        "location": {"type": "Point", "coordinates": [-83.738751, 42.296027]},
        "current": {
            "pollution": {
                "ts": "2023-09-14T06:00:00.000Z",
                "aqius": 24,
                "mainus": "p2",
                "aqicn": 8,
                "maincn": "p2",
            },
            "weather": {
                "ts": "2023-09-14T06:00:00.000Z",
                "tp": 8,
                "pr": 1018,
                "hu": 88,
                "ws": 0,
                "wd": 0,
                "ic": "50n",
            },
        },
    },
}

def test_get_valid_countries():
    result = mock_api.get_valid_countries("https://api.airvisual.com/v2/countries?key=e42058b7-5613-4952-974c-d877629c6524")
    expected_output = ["USA", "INDONESIA"]

    assert result == expected_output


def test_get_valid_states():
    result = mock_api.get_valid_states("https://api.airvisual.com/v2/states?country=INDONESIA&key=e42058b7-5613-4952-974c-d877629c6524")
    expected_output = [
        "ACEH",
        "BALI",
        "BANGKA BELITUNG",
        "BANTEN",
        "BENGKULU",
        "CENTRAL JAVA",
        "CENTRAL KALIMANTAN",
        "CENTRAL SULAWESI"
    ]

    assert result == expected_output


def test_get_valid_cities():
    result = mock_api.get_valid_cities("https://api.airvisual.com/v2/cities?country=INDONESIA&state=WEST JAVA&key=e42058b7-5613-4952-974c-d877629c6524")
    expected_output = [
        "BANDUNG",
        "BEKASI",
        "BOGOR",
        "CIBINONG",
        "CILEUNGSIR",
        "CIREBON",
        "DEPOK",
        "KARAWANG",
        "PASARKEMIS",
        "SERPONG"
    ]

    assert result == expected_output


def test_get_weather_data():
    data = {
        "status": "success",
        "data": {
            "city": "Ann Arbor",
            "state": "Michigan",
            "country": "USA",
            "location": {"type": "Point", "coordinates": [-83.738751, 42.296027]},
            "current": {
                "pollution": {
                    "ts": "2023-09-14T06:00:00.000Z",
                    "aqius": 24,
                    "mainus": "p2",
                    "aqicn": 8,
                    "maincn": "p2",
                },
                "weather": {
                    "ts": "2023-09-14T06:00:00.000Z",
                    "tp": 8,
                    "pr": 1018,
                    "hu": 88,
                    "ws": 0,
                    "wd": 0,
                    "ic": "50n",
                },
            },
        },
    }

    country = "USA"
    state = "MICHIGAN"
    city = "ANN ARBOR"
    expected_output = (
        "Weather in ANN ARBOR, MICHIGAN, USA:"
        + "\n"
        + "Temperature: 8°C"
        + "\n"
        + "Humidity: 88%"
        + "\n"
        + "Wind Speed: 0 m/s"
    )

    assert project.get_weather_data(data, country, state, city) == expected_output


def test_pollution_data():
    data = {
        "status": "success",
        "data": {
            "city": "Ann Arbor",
            "state": "Michigan",
            "country": "USA",
            "location": {"type": "Point", "coordinates": [-83.738751, 42.296027]},
            "current": {
                "pollution": {
                    "ts": "2023-09-14T06:00:00.000Z",
                    "aqius": 24,
                    "mainus": "p2",
                    "aqicn": 8,
                    "maincn": "p2",
                },
                "weather": {
                    "ts": "2023-09-14T06:00:00.000Z",
                    "tp": 8,
                    "pr": 1018,
                    "hu": 88,
                    "ws": 0,
                    "wd": 0,
                    "ic": "50n",
                },
            },
        },
    }

    country = "USA"
    state = "MICHIGAN"
    city = "ANN ARBOR"
    expected_output = (
        "Pollution in ANN ARBOR, MICHIGAN, USA:"
        + "\n"
        + "AQI (Air Quality Index): 24"
        + "\n"
        + "Main Pollutant: p2"
    )

    assert project.get_pollution_data(data, country, state, city) == expected_output


def test_get_data():
    country = "USA"
    state = "MICHIGAN"
    city = "ANN ARBOR"

    url = f"https://api.airvisual.com/v2/city?city={city}&state={state}&country={country}&key=e42058b7-5613-4952-974c-d877629c6524"
    result = mock_api.get_data(url, country, state, city)
    expected_output = {
        "status": "success",
        "data": {
            "city": "Ann Arbor",
            "state": "Michigan",
            "country": "USA",
            "location": {"type": "Point", "coordinates": [-83.738751, 42.296027]},
            "current": {
                "pollution": {
                    "ts": "2023-09-14T06:00:00.000Z",
                    "aqius": 24,
                    "mainus": "p2",
                    "aqicn": 8,
                    "maincn": "p2",
                },
                "weather": {
                    "ts": "2023-09-14T06:00:00.000Z",
                    "tp": 8,
                    "pr": 1018,
                    "hu": 88,
                    "ws": 0,
                    "wd": 0,
                    "ic": "50n",
                },
            },
        },
    }

    assert result == expected_output