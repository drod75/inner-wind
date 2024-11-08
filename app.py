from flask import Flask, render_template
from chat import get_weather_output
import pandas as pd
from weather import get_weather

app = Flask(__name__ ,static_folder='static')

@app.route('/')
@app.route('/forecast')
def forecast():
    weather_content = get_weather()
    ai_suggestions = get_weather_output(weather_content)
    content = {'weather': weather_content, 'ai': ai_suggestions}
    return render_template('base.html', **content)
