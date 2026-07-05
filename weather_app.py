import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=3"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"--- Weather Update for {city.capitalize()} ---")
            print(response.text)
        else:
            print("Could not fetch weather data. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)
