from selenium import webdriver
import time
import sys

#take user id and Password
uid = input("Enter Email or Phone No. - ")
password = input("Enter Password - ")

#open Google Chrome
browser = webdriver.Chrome("B:\\Alien Brain\\Python Warm-Up\\chromedriver.exe")
browser.get("https://www.facebook.com/")

#login to Facebook
eui = browser.find_element_by_id("email")
eui.send_keys(uid)

epass = browser.find_element_by_id("pass")
epass.send_keys(password)

log_but = browser.find_element_by_id("u_0_b")
log_but.click()

time.sleep(20)			#wait for Page Loading

#open notification page in facebook
browser.get("https://www.facebook.com/notifications/")

time.sleep(10)			#wait for Page Loading

#Take all notifications or exit program if login failure
try:
	notif_list = browser.find_elements_by_xpath("//*[@class='_4l_v']/span")
except:
	print("Account Not Found in facebook")
	sys.exit()

#Print 5 notifications
count = 1
for i in notif_list:
	print(i.get_attribute("textContent")+"\n")
	count = count+1
	if (count == 6):
		break

browser.close()
print("\n\nDONE")