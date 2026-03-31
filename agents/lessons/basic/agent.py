"""
Lesson: Basic Agent (Global Live Tools)
=======================================
A simple conversational agent using PRO tools:
- Real Weather: Active fetch from wttr.in
- Real Time: Geocoding (geopy) + Timezone mapping (timezonefinder)
"""

import datetime
import requests
from zoneinfo import ZoneInfo
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from google.adk.agents import Agent
from google.adk.models import Gemini
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

# We initialize these once to keep the tool fast
geolocator = Nominatim(user_agent="adk_learning_playground")
tf = TimezoneFinder()

def get_real_weather(location: str) -> str:
    """Fetch live weather from any city or location on Earth.
    
    Args:
        location: The place you want to check weather for (eg. 'London', 'Tokyo').
    """
    print(f"[WeatherTool] Fetching for: {location}")
    try:
        url = f"https://wttr.in/{location}?format=3"
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return f"Could not find weather for {location}."
        return response.text.strip()
    except Exception as e:
        return f"Weather service error: {str(e)}"

def get_real_time(place_name: str) -> str:
    """Gets the current local time for ANY city or location globally.
    
    Args:
        place_name: The name of the city, town, or location (eg. 'Paris', 'Dubai').
    """
    print(f"[TimeTool] Looking up timezone for: {place_name}")
    try:
        location = geolocator.geocode(place_name, timeout=10)
        if not location:
            return f"Could not locate '{place_name}' on a map."
        
        # We find the timezone based on latitude/longitude
        tz_name = tf.timezone_at(lng=location.longitude, lat=location.latitude)
        if not tz_name:
            return f"Could not determine the timezone for '{place_name}'."
        
        tz = ZoneInfo(tz_name)
        now = datetime.datetime.now(tz)
        return (f"The current local time in {place_name} ({tz_name}) "
                f"is {now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}")
    except Exception as e:
        return f"Time service error: {str(e)}"

root_agent = Agent(
    name="global_assistant",
    model=Gemini(model="gemini-3-flash-preview"),
    instruction="You are a professional global assistant. Use your tools to find live weather and global time.",
    tools=[get_real_weather, get_real_time],
)

from google.adk.apps import App
app = App(
    name="basic",
    root_agent=root_agent,
)
