from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

url = "https://www.espncricinfo.com/rankings/content/page/211271.html"
pg = urlopen(url)		#get html source code of webpage
soup = BeautifulSoup(pg,'html.parser')		#creat html parser

body = soup.find('div',{'class':'ciPhotoContainer'})		#find headings
head = soup.findAll('h3')			#find all headings

name = []
for i in head:
	name.append(i.text)

column_name = ['Pos','Team','Matches','Points','Rating']
df = pd.DataFrame(columns = column_name)

tr_list = soup.findAll('tr')

tabel_count = 0
for j in tr_list:
	row = []
	td_list = j.findAll('td')
	for k in td_list:
		row.append(k.text)
		data = {}
	try:
		for l in range(len(df.columns)):
			data[df.columns[l]] = row[l]
		df = df.append(data,ignore_index=True)
	except:
		df = pd.DataFrame(columns = column_name)
		table_name = name[tabel_count]
		tabel_count = tabel_count+1
	df.to_csv("B:\\Alien Brain\\Python Warm-Up\\Test\\"+table_name+".csv")


print("DONE")