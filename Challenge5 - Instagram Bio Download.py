from selenium import webdriver

target_profile = input("Enter the User Handle of the Profile :- ")

driver_path = 'B:\\Alien Brain\\Python Warm-Up\\chromedriver.exe'
browser = webdriver.Chrome(driver_path)


url = "Https://www.instagram.com/"+target_profile

browser.get(url)

try:
	bio_path = browser.find_element_by_xpath("//*[@class='-vDIg']/span")
	bio = bio_path.get_attribute("textContent")
except:
	print("InstaHandle Bio NOT Found")
	browser.close()
	exit()

f_path = "B:\\Alien Brain\\Python Warm-Up\\Test\\"+target_profile+".txt"
fo = open(f_path,'a')
fo.write(bio)
fo.close()

browser.close()
print("Bio of "+target_profile+" has been saved in "+f_path)