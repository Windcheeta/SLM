import requests
from bs4 import BeautifulSoup
import csv
import re

next_page = ""
file = open("Web scraper/quotes.csv","w",encoding="utf-8")
writer = csv.writer(file)
writer.writerow(["Quotes","Authors","tags"])
more = True
tags =[]

while more:
        
    r = requests.get("https://quotes.toscrape.com"+next_page)
    soup = BeautifulSoup(r.text,"lxml")
    all = soup.find_all("div",attrs={"class":"text"})
    quote = soup.find_all("span",attrs={"class":"text"})
    author = soup.find_all("small",attrs={"class":"author"})
    for i in soup.find_all("div",attrs={"class":"tags"}):
        tags.append([a.text for a in i.find_all("a")])

 
    more = soup.find_all("li",attrs={"class":"next"})   #,
    if more: next_page= more[0].a.attrs["href"]
    
    for a,b,c in zip(quote,author,tags):
        writer.writerow([a.text,b.text,c])  
    tags = []
    