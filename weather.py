from ratelimit import limits
from datetime import datetime, timedelta
from pymeteosource.api import Meteosource
from pymeteosource.types import tiers, sections, langs, units
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='.env')
hour_interval = 1800;

@limits(calls=24, period=hour_interval)
def get_weather():
    places = ['The Bronx', 'Manhattan', 'Brooklyn', 'Queens', 'Staten Island']
    forecast_city = []
    meteosource = Meteosource(os.getenv('metoeosource'), tier=tiers.FREE)
    for place in places:
        forecast = meteosource.get_point_forecast(place_id=place, units=units.US)
        forecast_city.append(forecast)
    return forecast