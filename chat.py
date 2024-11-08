
from langchain_mistralai.chat_models import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from pathlib import Path
from ratelimit import limits
import os

load_dotenv(Path(".env"))

mistralai = ChatMistralAI(model = 'open-mistral-7b',api_key=os.getenv("MISTRAL_API_KEY"))
prompt_template = ChatPromptTemplate.from_messages([
    ("system", '''You are a helpful assistant that takes in weather data via a dictionary,
     with this data you use it to give people advice for what to do depending on the weather.'''),
    ("human", "{input}"),
])
chain = prompt_template | mistralai

hour_interval = 3600;
@limits(calls=24, period=hour_interval)
def get_weather_output(weather_list):
    output = chain.invoke({"input": weather_list})
    return output