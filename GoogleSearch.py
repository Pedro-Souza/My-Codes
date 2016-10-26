#!/usr/bin/python
# coding=utf-8

# Author Fnkoc

from bs4 import BeautifulSoup
from mechanize import Browser


def google(query):
    print("\n\t[!] Searching on Google...\n")
    print("[QUERY] >> " + query)

    try:
        query = query.replace(" ", "+")
        req = "https://www.google.com.br/search?q=%s&num=50&start=0" % query
        br = Browser()
        br.set_handle_robots(False)
        br.addheaders = [("User-agent", "chrome")]
        html = br.open(req).read()
        soup = BeautifulSoup(html, "html5lib")

        with open("./output/google-%s.txt" % query[8:], "w") as log:
            for results in soup.findAll(attrs={"class": "g"}):
                for title in results.findAll("h3", attrs={"class": "r"}):
                    t = title.text
                    t = t.title()
                    for link in results.findAll(attrs={"class": "s"}):
                        l = link.cite.text
                        print(t)
                        print(l + '\n')
                        log.write(str(l) + '\n')

    except Exception as e:
        print(e)


query = input("Keyword: ")
google(query)
