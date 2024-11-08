from flask import Flask, render_template
from chat import get_weather_output
import pandas as pd
from weather import get_weather

app = Flask(__name__ ,static_folder='static')

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/forecast_brooklyn')
def forecast_brooklyn():
    weather_content = get_weather('brooklyn')
    ai_suggestions = get_weather_output(weather_content)
    content = {'weather': weather_content, 'ai': ai_suggestions}
    return render_template('brooklyn.html', **content)

@app.route('/forecast_manhattan')
def forecast_manhattan():
    weather_content = get_weather('manhattan')
    ai_suggestions = get_weather_output(weather_content)
    content = {'weather': weather_content, 'ai': ai_suggestions}
    return render_template('manhattan.html', **content)

@app.route('/forecast_queens')
def forecast_queens():
    weather_content = get_weather('queens')
    ai_suggestions = get_weather_output(weather_content)
    content = {'weather': weather_content, 'ai': ai_suggestions}
    return render_template('queens.html', **content)
