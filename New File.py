f_name = input("Input NEW File name :- ")
fo = open("B:\\Alien Brain\\Python Warm-Up\\"+f_name+".py","a")
fo.write("from selenium import webdriver\n\ndriver_path = \'B:\\\\Alien Brain\\\\Python Warm-Up\\\\chromedriver.exe\'\nbrowser = webdriver.Chrome(driver_path)\n")
fo.close()