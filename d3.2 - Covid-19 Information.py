from selenium import webdriver
import pandas as pd
import time
import os

browser = webdriver.Chrome("B:\\Alien Brain\\Python Warm-Up\\chromedriver.exe")
browser.get("https://www.worldometers.info/coronavirus/")
time.sleep(60)
df = pd.DataFrame(columns=['Rank','Country','Total Cases','New Cases','Deaths','New Deaths','Recovered','Active Cases','Critical'])


for i in browser.find_elements_by_xpath('//*[@id="main_table_countries_today"]/tbody/tr'):
	td_list = i.find_elements_by_tag_name('td')
	row = []
	for td in td_list:
		row.append(td.text)
	data = {}
	for j in range(len(df.columns)):
		data[df.columns[j]] = row[j]
	df=df.append(data,ignore_index=True)

browser.close()
print(df)

base_path='B:\\Alien Brain\\Python Warm-Up'

path=os.path.join(base_path,'Covid_Dataset2.csv')
#os.mkdir(path)
df.to_csv(path, index = False)
print("The dataset has been saved at the loction: "+path)
