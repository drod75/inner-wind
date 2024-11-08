
from langchain_mistralai.chat_models import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(".env"))

mistralai = ChatMistralAI(api_key=os.getenv("MISTRAL_API_KEY"))
prompt_template = ChatPromptTemplate.from_messages([
    ("system", '''You are a helpful assistant that takes in weather data such'''),
    ("human", "{input}"),
])
chain = prompt_template | mistralai

def get_weather_output(weather_dict):
    pass