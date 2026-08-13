import requests

API_KEY = "9c17b818d7714f6585053233261308"

city = input("Enter city name: ")

url = "https://api.weatherapi.com/v1/current.json"

params = {
    "key": API_KEY,
    "q": city
}

try:
    response = requests.get(url, params=params)

    data = response.json()

    if response.status_code == 200:
        print("\nReal-Time Weather Information")
        print("-----------------------------")
        print("City:", data["location"]["name"])
        print("Temperature:", data["current"]["temp_c"], "°C")
        print("Humidity:", data["current"]["humidity"], "%")

    else:
        print("Error:", data["error"]["message"])

except requests.exceptions.RequestException as e:
    print("Connection error:", e)