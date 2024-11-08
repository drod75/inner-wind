from ratelimit import limits
from datetime import datetime, timedelta
from pymeteosource.api import Meteosource
from pymeteosource.types import tiers, sections, langs, units
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv(dotenv_path='.env')
hour_interval = 1800;

@limits(calls=24, period=hour_interval)
def get_weather(borough):
    borough_data = []
    meteosource = Meteosource(os.getenv('metoeosource'), tier=tiers.FREE)
    forecast = meteosource.get_point_forecast(place_id=borough, units=units.US, sections = [sections.CURRENT, sections.DAILY], langs = [langs.ENGLISH])
    current_weather = forecast.current.to_pandas()      
    current_wind = forecast.current.wind.to_pandas()
    borough_data.append(current_weather)
    borough_data.append(current_wind)
    return borough_data
