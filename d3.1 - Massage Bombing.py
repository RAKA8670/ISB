phone_no = input("Enter Email or Phone : ")
times = input("How many times? : ")

from selenium import webdriver

browser = webdriver.Chrome("B:\\Alien Brain\\Python Warm-Up\\chromedriver.exe")

browser.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fref%3Dap_frn_logo%2F%3F_encoding%3DUTF8%26ref_%3Dnav_newcust&prevRID=49ZS0W2H0BR8JJ0C9CER&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=inflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

phone_no_input = browser.find_element_by_id("ap_email")
phone_no_input.send_keys(phone_no)

click_continue = browser.find_element_by_id("continue")
click_continue.click()

import time
time.sleep(5)

click_otp = browser.find_element_by_id("continue")
click_otp.click()
print("OTP Send "+str(1)+" ")

time.sleep(2)

for i in range(int(times)-1):
	resend_otp = browser.find_element_by_link_text("Resend OTP")
	resend_otp.click()
	print("OTP Send "+str(i+2)+" ")
	time.sleep(2)

browser.close()
print("Done")
