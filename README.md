# PyNews
PyNews is a free, REST API for any language. It uses Google's Gemini to summarize news articles from CNN. It is hosted with Flask and PythonAnywhere. There is not rate limiting, so please don't attempt to overload the server in any way.
## Shell Languages
You can use PyNews in shell languages by entering this:
```
curl https://pynews.pythonanywhere.com/
```
## Python
You can use PyNews in Python by using this:
```
import requests
data = requests.get("https://pynews.pythonanywhere.com/")
print(data.text)
```
## Other Languages
You can use PyNews in practically every language that supports fetching from the Internet, because it is a REST API. It's just I don't comprehend those languages. Sorry.
