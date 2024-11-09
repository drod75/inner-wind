from ratelimit import limits
from pymeteosource.api import Meteosource
from pymeteosource.types import tiers, sections, langs, units
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='.env')
hour_interval = 3600;

@limits(calls=24, period=hour_interval)
def get_weather(borough):

    meteosource = Meteosource(os.getenv('metoeosource'), tier=tiers.FREE)
    units_weather = {}

    if borough == 'Bronx':
        forecast = meteosource.get_point_forecast(lat=40.84985, lon= -73.86641, units=units.US, sections = [sections.CURRENT, sections.DAILY])
        f = forecast.current.to_dict()
        n = f.pop('icon')
        n = f.pop('icon_num')
        f['Sky Condition'] = f.pop('summary')

        w = forecast.current.wind.to_dict()
        n = w.pop('angle')
        n = w.pop('dir')
        n = w.pop('speed')

        f1 = dict()
        w1 = dict()

        for key, value in f.items():
            if key == 'icon_num':
                image_path = f"/static/images/{value}.png"
                f1[key] = image_path
            else:
                new_key = (key.replace('_', ' ')).title()
                f1[new_key] = (str(value))
        for key, value in w.items():
            new_key = (key.replace('_', ' ')).title()
            w1[new_key] = (str(value))
        
        content = {'current': f1, 'wind': w1}
        return content
    elif borough =='Staten Island':
        forecast = meteosource.get_point_forecast(lat=40.56233, lon=-74.13986, units=units.US, sections = [sections.CURRENT, sections.DAILY])
        f = forecast.current.to_dict()
        n = f.pop('icon')
        n = f.pop('icon_num')
        f['Sky Condition'] = f.pop('summary')

        w = forecast.current.wind.to_dict()
        n = w.pop('angle')
        n = w.pop('dir')
        n = w.pop('speed')

        f1 = dict()
        w1 = dict()

        for key, value in f.items():
            if key == 'icon_num':
                image_path = f"/static/images/{value}.png"
                f1[key] = image_path
            else:
                new_key = (key.replace('_', ' ')).title()
                f1[new_key] = (str(value))
        for key, value in w.items():
            new_key = (key.replace('_', ' ')).title()
            w1[new_key] = (str(value))
        
        content = {'current': f1, 'wind': w1}
        return content
    else:
        forecast = meteosource.get_point_forecast(place_id=borough, units=units.US, sections = [sections.CURRENT, sections.DAILY])
        f = forecast.current.to_dict()
        n = f.pop('icon')
        n = f.pop('icon_num')
        f['Sky Condition'] = f.pop('summary')

        w = forecast.current.wind.to_dict()
        n = w.pop('angle')
        n = w.pop('dir')
        n = w.pop('speed')

        f1 = dict()
        w1 = dict()

        for key, value in f.items():
            if key == 'icon_num':
                image_path = f"/static/images/{value}.png"
                f1[key] = image_path
            else:
                new_key = (key.replace('_', ' ')).title()
                f1[new_key] = (str(value))
        for key, value in w.items():
            new_key = (key.replace('_', ' ')).title()
            w1[new_key] = (str(value))
        
        content = {'current': f1, 'wind': w1}
        return content
