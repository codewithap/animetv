from flask import Flask, render_template, request, redirect
from bs4 import BeautifulSoup
from scrappers.gogoanimeScrapper import *
from scrappers._9animeScrapper import *

app = Flask(__name__)

@app.route("/")
def home():
	
	return render_template("home.html")

@app.route("/search", methods = ["GET", "POST"])
def search():
    q = request.args.get("query")
    arr = getSresultLinks(q)
    links = arr[0]
    img = arr[1]
    title = arr[2]
    n_arr = []
    i = 0
    while True:
        n_arr.append(i)
        i = i+1
        if i == len(links):
            break
    
    if links[0] == "none":
        return render_template("notFound.html",q = q)
    else: 
        return render_template("search.html",links = links, img = img, title = title, q=q,n_arr=n_arr)

@app.route("/episodes/<string:link>", methods = ["GET", "POST"])
def episodes(link):
    epLinks = getEpLinks("https://gogoanime.lol/category/"+link)
    info = getEpInfo("https://gogoanime.lol/category/"+link)
    n_arr = []
    i = 0
    while True:
        n_arr.append(i)
        i = i+1
        if i == len(epLinks):
            break
    return render_template("ep.html", epLinks = epLinks, info = info, n_arr = n_arr)

@app.route("/watch", methods = ["GET", "POST"])
def watch():
    name = request.args.get("name")
    url = f"https://9xbuddy.org/process?url={getEpEmbedLink('https://gogoanime.lol/'+name)}"
    
    return redirect(url)

@app.route("/top")
def random():
    url = "https://gogoanime.lol/popular.html"
    arr = getSresultLinks(url)
    links = arr[0]
    img = arr[1]
    title = arr[2]
    n_arr = []
    i = 0
    while True:
        n_arr.append(i)
        i = i+1
        if i == len(links):
            break
    
    return render_template("search.html",links = links, img = img, title = title, q="Popular Anime",n_arr=n_arr)


if __name__ == "__main__":
	app.run(debug =False,host="0.0.0.0")
