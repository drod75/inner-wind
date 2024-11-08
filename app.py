from flask import Flask, render_template
from chat import get_weather_output
import pandas as pd
from weather import get_weather

app = Flask(__name__ ,static_folder='static')

@app.route('/')
@app.route('/home')
def home():
    ai_content = get_weather_output('New York City')
    return render_template('home.html', content=ai_content)

@app.route('/forecast_brooklyn')
def forecast_brooklyn():
    content = get_weather('Brooklyn')
    return render_template('brooklyn.html', content=content)

@app.route('/forecast_manhattan')
def forecast_manhattan():
    content = get_weather('Manhattan')
    return render_template('manhattan.html', content=content)
@app.route('/forecast_queens')
def forecast_queens():
    content = get_weather('Queens')
    return render_template('queens.html', content=content)

@app.route('/forecast_bronx')
def forecast_bronx():
    content = get_weather('Bronx')
    return render_template('bronx.html', content=content)

@app.route('/forecast_staten_island')
def forecast_staten_island():
    content = get_weather('Staten Island')
    return render_template('staten_island.html', content=content)