from google import genai
from flask import Flask, Response
import requests

app = Flask(__name__)

data = requests.get("https://www.w3.org/services/html2txt?url=https://lite.cnn.com/")
client = genai.Client(api_key="YOUR_API_KEY")
#Enter your Gemini API key here as a string. Remember to not embed your API key somewhere public, because bad people can control your account with it.
response = client.models.generate_content(
    model="gemini-2.0-flash", contents="This is a news article's scraped HTML contents, please summarize this news in an interesting essay (Do not mention CNN, just mention the news.): " + str(data.text)
)
print(response.text)

@app.route("/")
def display():
    return Response(str(response.text), mimetype='text/plain')
