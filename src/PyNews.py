#Setup Flask and Imports
from google import genai
from flask import Flask, Response
import requests

app = Flask(__name__)

#Fetch & Generate News
data = requests.get("https://www.w3.org/services/html2txt?url=https://lite.cnn.com/")
client = genai.Client(api_key="YOUR_API_KEY")
response = client.models.generate_content(
    model="gemini-2.0-flash", contents="This is a news article's scraped HTML contents, please summarize this news in an interesting essay (Do not mention CNN, just mention the news.): " + str(data.text)
)
print(response.text)

#Display News with Flask
@app.route("/")
def display():
    return Response("PyNews is a free news service by SeafoodStudios that scrapes from CNN Lite, and summarizes the news using Google Gemini. Here is the documentation: https://github.com/SeafoodStudios/PyNews\n\n" + str(response.text), mimetype='text/plain')
