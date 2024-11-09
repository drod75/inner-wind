
from langchain_mistralai.chat_models import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from pathlib import Path
from ratelimit import limits
import os

load_dotenv(Path(".env"))

mistralai = ChatMistralAI(model = 'open-mixtral-8x22b',api_key=os.getenv("MISTRAL_API_KEY"))
prompt_template = ChatPromptTemplate.from_messages([
    ("system", '''You are a helpful assistant that takes in weather data via a list with two dictionaries, 
     and give advice for each point in each dictionary in the list, for each dictionary provide a list of 
     3 bullet points for each feature and then return it. Make sure you format the output so when
     it is placed in html code it appears nice and neat.'''),
    ("human", "{input}"),
])
chain = prompt_template | mistralai

hour_interval = 3600;
@limits(calls=24, period=hour_interval)
def get_weather_output(weather_list):
    output = chain.invoke({"input": weather_list})
    return output