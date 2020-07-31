# Akhbar Padhke Sunao

import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.speak(str)
if __name__=='__main__':
    speak("News for today..Lets begin")
    url = "http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=ee124bc59f964401a991406135aba1ff"
    news = requests.get(url).text
    news_py = json.loads(news)
    print(news_py["articles"])
    arts = news_py["articles"]
    for article in arts:
        speak(article["title"])
        speak("Moving on to the next news..Listen carefully")
    speak("Thanks for listening..")
