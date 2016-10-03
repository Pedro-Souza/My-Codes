#!/usr/bin/python
#coding=utf-8

from bs4 import BeautifulSoup
from urllib.request import urlopen

count = 0
exception = False

with open("log.txt", "w") as log:
	while exception == False:
		if count == 0:
			page = ""
		else:
			page = "/%s" % count
		print("Page = ", count)
		url = "http://pt.aliexpress.com/category/201002178/replacement-keyboards%s.html?site=bra&shipCountry=BR&g=n&needQuery=n&tag=" % page

		try:
			print("Opening: ", url)
			code = urlopen(url).getcode()
			print("HTTP code: ", code)
			if code == "404":
				break
			else:
				count += 1
				html = urlopen(url)
			
				soup = BeautifulSoup(html.read().decode("utf-8"), "html5lib")
				for i in soup.findAll("ul", attrs={"class":"util-clearfix lazy-load"}):
					for j in i.findAll("a", attrs={"class":"product"}):
						title = j.get("title")
						print(title + "\n")
					
						link = j.get("href")
						print(link + "\n")
						
						if "sony" in title or "Sony" in title or "SONY" in title:
							log.write(str(title) + "\n" + str(link) + "\n")
						else:
							pass
					
		except Exception as e:
			print(e)
			exception = True
