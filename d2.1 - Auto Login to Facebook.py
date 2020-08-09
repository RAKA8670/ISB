from selenium import webdriver

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
