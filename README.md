# weather-app
weather app using API integration

Real-Time Weather App

A simple Python weather application that uses the WeatherAPI to fetch and display real-time weather information for any city entered by the user.

Features

* Enter any city name
* Display current temperature in Celsius
* Display humidity percentage
* Fetch real-time weather data using an API
* Handle invalid cities and API errors
* Handle connection and network errors
* Built using Python and the `requests` library

## Technologies Used

* Python
* Requests
* WeatherAPI
* REST API
* JSON

## How It Works

1. The user enters a city name.
2. The application sends a request to WeatherAPI.
3. The API returns the current weather information.
4. The program displays:

   * City name
   * Temperature
   * Humidity

## How to Run

Install the required library:

```bash
pip install requests
```

Run the program:

```bash
python weather.py
```

Then enter a city name when prompted.

## Example Output

```text
Enter city name: Hyderabad

Real-Time Weather Information
-----------------------------
City: Hyderabad
Temperature: 28.5 °C
Humidity: 72 %
```

## API Key Security

Do not upload your API key directly to GitHub. Store it in an environment variable or `.env` file and add `.env` to `.gitignore`.

## Project Purpose

This project was created to practice Python API integration, user input, JSON data handling, exception handling, and working with real-time data.

## Author

Vyshnavi

