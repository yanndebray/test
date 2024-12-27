import streamlit as st
import requests
st.title('My Weather App')

import matplotlib.pyplot as plt

# Function to get weather data
def get_weather():
    api_key = 'b1b15e88fa797225412429c1c50c122a1'  # Sample API key
    url = f'http://samples.openweathermap.org/data/2.5/forecast?q=Muenchen,DE&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    if 'list' in data:
        return data
    else:
        st.error("Error fetching weather data. Please check your API key and try again.")
        return None

# Function to plot weather data
def plot_weather(data):
    if data:
        dates = [item['dt_txt'] for item in data['list']]
        temps = [item['main']['temp'] for item in data['list']]
        
        plt.figure(figsize=(10, 5))
        plt.plot(dates, temps, marker='o')
        plt.xlabel('Date')
        plt.ylabel('Temperature (°C)')
        plt.title('5 Day Weather Forecast for Muenchen')
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(plt)

# Main app
weather_data = get_weather()
if weather_data:
    plot_weather(weather_data)