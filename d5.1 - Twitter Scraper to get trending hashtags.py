from selenium import webdriver
import time
import pandas as pd

driver_path = 'B:\\Alien Brain\\Python Warm-Up\\chromedriver.exe'
browser = webdriver.Chrome(driver_path)

browser.get("https://twitter.com/explore/tabs/trending")

time.sleep(10)
spans = browser.find_elements_by_tag_name("span")
htag_list = []
for i in spans:
	a = i.get_attribute("textContent")
	if (a.startswith('#')):
		if a not in htag_list:
			htag_list.append(a)

browser.close()


urls = []
for j in htag_list:
	url = "https://twitter.com/search?q=%23"+j+"&src=trend_click"
	urls.append(url)

dic = {'Hashtag':htag_list,'URL':urls}
df = pd.DataFrame(dic)

df.to_csv("B:\\Alien Brain\\Python Warm-Up\\Test\\Hashtag.csv")
print("DONE")