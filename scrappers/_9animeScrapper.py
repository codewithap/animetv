from bs4 import BeautifulSoup
import requests

url = "https://9anime.to/random"
def getRandomEp(url):
    response = requests.get(url)
    data = response.text
    return data

