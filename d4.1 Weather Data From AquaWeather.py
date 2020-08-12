from selenium import webdriver
import time
import pandas as pd

month = input("Enter Month - ")
year  = input("Enter Year - ")

driver_path = 'B:\\Alien Brain\\Python Warm-Up\\chromedriver.exe'
browser = webdriver.Chrome(driver_path)

browser.get("https://www.accuweather.com/en/in/kolkata/206690/"+month+"-weather/206690?year="+year+"&view=list")

time.sleep(10)

high = browser.find_elements_by_class_name("high")
high_list = []
for i in high:
	temp = i.get_attribute("textContent")
	high_list.append(int(temp[:2]))

low = browser.find_elements_by_class_name("low")
low_list = []
for j in low:
	temp = j.get_attribute("textContent")
	low_list.append(int(temp[3:5]))

precip = browser.find_elements_by_xpath("//*[@class='info precip']/p[2]")
precip_list = []
for k in precip:
	temp = k.get_attribute("textContent")
	precip_list.append(float(temp[:2]))

date=[]
d=1
for l in range(len(high_list)):
	date.append(int(d))
	d=d+1

dictionary = {'Date':date, 'High_Tempareture':high_list, 'Low_Tempurature':low_list, 'Precipitation':precip_list}
df = pd.DataFrame(dictionary)

browser.close()
print(df)

path = 'B:\\Alien Brain\\Python Warm-Up\\Test\\Weather_Data.csv'
df.to_csv(path,index=False)


print("DONE")


