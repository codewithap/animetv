from bs4 import BeautifulSoup 
import requests
import json

####################################################
def getSresultLinks(query):
    url = f"https://gogoanime.lol/search.html?keyword={query}"
    data = requests.request("GET", url)
    soup = BeautifulSoup(data.text, 'html.parser')
    #### Get all links in search result ####
    links = soup.select('div.img a')
    links_arr = []
    if len(links) > 0:
        for link in links:
            links_arr.append(link["href"].replace("https://gogoanime.lol/category/", ""))
    else:
        links_arr.append("none")
    #### Get all images in search result ####
    img_links = soup.select('div.img a img')
    img_links_arr = []
    if len(img_links) > 0:
        for link in img_links:
            img_links_arr.append(link["src"])
    else:
        img_links_arr.append("none")
    #### Get all anime titles in search results ####
    titles = soup.select('div.img a img')
    titles_arr = []
    if len(titles) > 0:
        for title in titles:
            titles_arr.append(title["alt"])
    else:
        titles_arr.append("none")
    arr = [links_arr, img_links_arr, titles_arr]
    return arr
####################################################

####################################################
def getEpLinks(url):
    data = requests.request("GET", url)
    soup = BeautifulSoup(data.text, 'html.parser')
    movie_id = (soup.select("#movie_id"))[0]["value"]
    alias_anime = (soup.select("#alias_anime"))[0]["value"]
    epUrl = f"https://gogoanime.lol/ajax/load_list_episode?ep_start=1&ep_end=9999&id={movie_id}&default_ep=1&alias={alias_anime}"
    epData = requests.request("GET", epUrl)
    epHtml = BeautifulSoup(epData.text, 'html.parser')
    epLinksArr = epHtml.select("a")
    return epLinksArr
####################################################

####################################################
def getEpInfo(url):
    data = requests.request("GET", url)
    soup = BeautifulSoup(data.text, 'html.parser')
    name = soup.select(".anime_info_body_bg h1")[0].get_text()
    image = (soup.select(".anime_info_body_bg img"))[0]["src"]
    summary = (soup.select(".anime_info_body_bg p"))

    arr = [name, image, summary]
    return arr
####################################################

####################################################
def getEpEmbedLink(epUrl):
    data = requests.request("GET",epUrl)
    soup = BeautifulSoup(data.text,"html.parser")
    iframe = soup.select("iframe")[0]["src"]
    return iframe
####################################################
    