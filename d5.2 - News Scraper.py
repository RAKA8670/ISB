from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd 

no_page = input("Enter No. of pages for Scrapping : ")

titles = []
links = []
for i in range(no_page):
	url = "https://news.ycombinator.com/news?p="+str(i+1)
	pg = urlopen(url)
	ps = pg.read()
	soup = BeautifulSoup(ps,'html.parser')
	d = soup.find('table',{'class':'itemlist'}).find_all('a',{'class':'storylink'})

	for j in d:
		title = j.text
		link = j.get('href')

		titles.append(title)
		links.append(link)

df = pd.DataFrame({'News_Title':titles,'URL':links})
df.to_csv("B:\\Alien Brain\\Python Warm-Up\\Test\\Hacker News.csv",index=False)
print("DONE")