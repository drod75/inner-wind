from flask import Flask, render_template
from chat import get_weather_output
from weather import get_weather

app = Flask(__name__)

@app.route('/')
@app.route('/forecast')
def forecast():
    weather_content = get_weather()
    ai_suggestions = get_weather_output(weather_content)
    content = [weather_content, ai_suggestions]
    return render_template('home.html', content=content)    
