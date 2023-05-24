from tkinter import *
import requests
"""def move_circle(event):
    canvas.coords(circle, event.x-25, event.y-25, event.x+25, event.y+25)"""
window=Tk()
window.title("Weather App")
window.geometry("400x200")
window.minsize(400,200)
"""canvas =Canvas(window, width=400, height=300)
canvas.pack()"""
def get_weather():
    country = country_entry.get()
    city = city_entry.get()
    access_key = "2e978bd2e7ed7457d9f10cdaff350ddb"  # Replace with your weatherstack API access key
    url = f"http://api.weatherstack.com/current?access_key={access_key}&query={city},{country}"
    response = requests.get(url)
    data = response.json()
    if "error" in data:
        weather_label.config(text="Error retrieving weather data")
    else:
        temperature = data["current"]["temperature"]
        weather_description = data["current"]["weather_descriptions"][0]
        humidity = data["current"]["humidity"]
        wind_speed = data["current"]["wind_speed"]
        cloud_cover = data["current"]["cloudcover"]

        weather_label.config(text=f"Temperature: {temperature}°C\n"
                                  f"Weather: {weather_description}\n"
                                  f"Humidity: {humidity}%\n"
                                  f"Wind Speed: {wind_speed} km/h\n"
                                  f"Cloud Cover: {cloud_cover}%")
country_label = Label(window, text="Country:")
country_label.pack()
country_entry =Entry(window,relief=SUNKEN,borderwidth=3)
country_entry.pack()
city_label = Label(window, text="City:")
city_label.pack()
city_entry =Entry(window,relief=SUNKEN,borderwidth=3)
city_entry.pack()
button = Button(window, text="Get Weather", command=get_weather)
button.pack()
weather_label =Label(window, text="")
weather_label.pack()
window.mainloop()