from selenium import webdriver


terget_profile = input("Enter the User Handle of the Profile :- ")

driver_path = "B:\\Alien Brain\\Python Warm-Up\\chromedriver.exe"
browser = webdriver.Chrome(driver_path)

url = "Https://www.instagram.com/"+terget_profile
browser.get(url)

try:
	img_path = browser.find_element_by_xpath("//img[@class='_6q-tv']")
except:
	img_path = browser.find_element_by_xpath("//img[@class='be6sR']")

img_link = img_path.get_attribute('src')
down_path = "B:\\Alien Brain\\Python Warm-Up\\Test\\"+terget_profile+".jpg"

import urllib.request
urllib.request.urlretrieve(img_link,down_path)

print("Done")
browser.close()