from ratelimit import limits
from datetime import datetime, timedelta
from pymeteosource.api import Meteosource
from pymeteosource.types import tiers, sections, langs, units
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='.env')
seconds = 0;

def get_weather():
    meteosource = Meteosource(os.getenv('metoeosource'), tier=tiers.FREE)
    forecast = meteosource.get_point_forecast(place_id=place, units=units.US)
    return forecast