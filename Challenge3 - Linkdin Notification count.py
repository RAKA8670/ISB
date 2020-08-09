user_id = input("Enter Your Email or Phone : ")	#get User ID
password = input("Enter Password : ")			#get Password

from selenium import webdriver
browser = webdriver.Chrome("B:\\Alien Brain\\Python Warm-Up\\chromedriver.exe")
#Open Linkdin
browser.get("https://www.linkedin.com/")		
#Put User ID
sign_uid = browser.find_element_by_id("session_key")
sign_uid.send_keys(user_id)								
#Put Password
sign_pass = browser.find_element_by_id("session_password")
sign_pass.send_keys(password)							
#Click on Sign in Button
sign_butt = browser.find_element_by_class_name("sign-in-form__submit-button")
sign_butt.click()										

#waiting for full page load
import time
time.sleep(20)			

#get Number of Notification
k = '//*[@id="notifications-nav-item"]/a/span[1]/span[2]'
n = browser.find_element_by_xpath(k).get_attribute('textContent')

#Sign out from Linkdin
browser.get("https://www.linkedin.com/m/logout/")		
browser.close()

print("No. of Notification(s) = "+n+" ")




