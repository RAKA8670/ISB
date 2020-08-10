from selenium import webdriver
from bs4 import BeautifulSoup
import time

uid = input("Enter Email or Phone No. - ")
password = input("Enter Password - ")

browser = webdriver.Chrome("B:\\Alien Brain\\Python Warm-Up\\chromedriver.exe")
browser.get("https://www.facebook.com/")

eui = browser.find_element_by_id("email")
eui.send_keys(uid)

epass = browser.find_element_by_id("pass")
epass.send_keys(password)

log_but = browser.find_element_by_id("u_0_b")
log_but.click()

time.sleep(60)

profile = browser.find_element_by_xpath('//a[@class="_2s25 _606w"]')
profile.click()

time.sleep(60)

frn = browser.find_element_by_xpath('//ul[@class="_6_7 clearfix"]/li[3]/a')
frn.click()

time.sleep(10)

while True:
	browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
	time.sleep(0.1)
	browser.execute_script("window.scrollTo(0,0);")
	time.sleep(0.1)
	try:
		exit_loop = browser.find_element_by_xpath("//*[contains(text(),'More About You')]")
		break
	except:
		continue


ps = browser.page_source

soup = BeautifulSoup(ps,'html.parser')

flist = soup.find('div',{'class':'_3i9'})

friends=[]
for i in flist.findAll('a'):
	friends.append(i.text)

friend_names = []
for name in friends:
	if (name == "FriendFriends"):
		continue
	if (name == ""):
		continue
	if ('friends' in name):
		continue
	else:
		friend_names.append(name)

browser.close()
print(friend_names)


