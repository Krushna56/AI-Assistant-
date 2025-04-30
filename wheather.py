from requests_html import HTMLSession
import sys

def get_weather(city):
    try:
        s = HTMLSession()
        url = f"https://www.google.com/search?q=weather+{city}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
        }
        
        r = s.get(url, headers=headers)
        
        if r.status_code != 200:
            return f"Error: Unable to fetch weather data (Status code: {r.status_code})"
        
        temp = r.html.find('span#wob_tm', first=True)
        unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True)
        desc = r.html.find('span#wob_dc', first=True)
        
        if not all([temp, unit, desc]):
            return "Error: Could not find weather information"
            
        return {
            "temperature": temp.text,
            "unit": unit.text,
            "description": desc.text
        }
        
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    city = "patna"  # You can modify this or take user input
    weather_data = get_weather(city)
    
    if isinstance(weather_data, dict):
        print(f"Temperature: {weather_data['temperature']}°{weather_data['unit']}")
        print(f"Condition: {weather_data['description']}")
    else:
        print(weather_data)  # Print error message

if __name__ == "__main__":
    main()
