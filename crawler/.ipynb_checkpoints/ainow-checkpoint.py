#https://ainow.ai/new/

from urllib import request  # urllib.requestモジュールをインポート
from bs4 import BeautifulSoup  # BeautifulSoupクラスをインポート

def getLatestLinks():
    urls = []
    titles = []
    url = "https://ainow.ai/new/"
    response = request.urlopen(url)
    soup = BeautifulSoup(response)
    response.close()

    #target class : article_title
    ti = soup.find_all("div",class_="article_title")
    ur = soup.find_all("a",class_="article_link")

    #print(ti)
    #print(ur)

    for i in range(len(ti)):
        t = ti[i].find("h2")
        title = t.text
        #print(title)
        titles.append(title)
        url = ur[i].get("href")
        #print(url)
        urls.append(url)
    
    return titles, urls