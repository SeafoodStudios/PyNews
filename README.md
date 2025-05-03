# PyNews
PyNews is a free, REST API for any language. It uses Google's Gemini to summarize news articles from CNN. It is hosted with Flask and PythonAnywhere. It updates every day at 5:00 PM Eastern Daylight Time. No API Key or is required, and there is no rate limit, so please do not try to overload the server.
## Bash or Zsh
You can use PyNews in Bash or Zsh by entering this:
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
