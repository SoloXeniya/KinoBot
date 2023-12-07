
import json 
import requests
from bs4 import BeautifulSoup
#from .config import URL, HEADERS
URL = "https://rezka.ag/page/{0}/"
HEADERS= {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.1.1215 Yowser/2.5 Safari/537.36"
}


def get_html(url, header):                             # програмнмный  код хранится 
    responce = requests.get(url, headers=header)      # отправляет данные на сайт   #куда отправить отправить запрос 1 парам.  header параметр
    if responce.status_code == 200:                       
        return responce.text                             # возвращает HTML cс сайта
    else:
        raise Exception(f"Error responce code {responce.status_code}")


def processing(html):
    soup = BeautifulSoup(html,"lxml").find("div", 
        {"class": "b-content__inline_items"}).find_all("div", {"class":"b-content__inline_item"})
    
    info = []

    for item in soup:
        title = item.find("div", {"class": "b-content__inline_item-link"}).find("a").text
        desc = item.find("div", {"class": "b-content__inline_item-link"}).find("div").text
        year = str(desc).split(",")[0]
        country = str(desc).split(",")[1].strip()
        try:
            genre = str(desc).split(",")[2].strip()
        except Exception:
            genre = "None"    
        url = item.find("div", {"class": "b-content__inline_item-link"}).find("a").get("href")
        movie = item.find("div", {"class": "b-content__inline_item-cover"}).find("a").find("span", {"class":"cat"}).text
        img = item.find("div", {"class": "b-content__inline_item-cover"}).find("a").find("img").get("src")
        
        info.append({
            "title": title,
            "year" : year,
            "genre" : genre,
            "country" : country,
            "url" : url,
            "movie": movie,
            "img" : img
        })
    return info
        
def PARSRUN(url, header):
    my_list = []
    for page in range(1, 10):
        html = get_html(url.format(page), header)             #хранит всю страницу в переменной .    параметры передаются get_html чтоб вытащить
        source = processing(html)                # запускается processing
        my_list.extend(source)
        print(f"страинца {page} спарсилась")


    with open("pars.json", "w") as file:
        json.dump(my_list, file, indent=4, ensure_ascii=False)
    return "парсинг завершен"

#print(PARSRUN(URL, HEADERS))







