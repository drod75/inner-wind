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

    meteosource = Meteosource(os.getenv('metoeosource'), tier=tiers.FREE)

    if borough == 'Bronx':
        forecast = meteosource.get_point_forecast(lat=40.84985, lon= -73.86641, units=units.US, sections = [sections.CURRENT, sections.DAILY])
        f = forecast.current.to_dict()
        n = f.pop('icon')
        n = f.pop('icon_num')
        f['Sky Condition'] = f.pop('summary')
    
        w = forecast.current.wind.to_dict()
        n = w.pop('angle')
        
        content = {'current': f, 'wind': w}
        return content
    elif borough =='Staten Island':
        forecast = meteosource.get_point_forecast(lat=40.56233, lon=-74.13986, units=units.US, sections = [sections.CURRENT, sections.DAILY])
        f = forecast.current.to_dict()
        w = forecast.current.wind.to_dict()
        content = {'current': f, 'wind': w}
        return content
    else:
        forecast = meteosource.get_point_forecast(place_id=borough, units=units.US, sections = [sections.CURRENT, sections.DAILY])
        f = forecast.current.to_dict()
        w = forecast.current.wind.to_dict()
        content = {'current': f, 'wind': w}
        return content
