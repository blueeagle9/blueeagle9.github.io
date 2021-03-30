from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
#1 Khai bao bien browser
browser = webdriver.Chrome(executable_path="chromedriver")

#2 Mo thu mot trang web
browser.get("http://facebook.com")

#2a Dien thong tin vao o user va pass
txtUser=browser.find_element_by_id("email")
txtUser.send_keys("abcxyz") # <--- Dien username that cua cac ban vao day

txtPass = browser.find_element_by_id("pass")
txtPass.send_keys("passwordfake")

#2b Submit form (login)
txtPass.send_keys(Keys.ENTER)

#3 Dung chuong trinh 5 giay
sleep(5)

#4 Dong trinh duyet
browser.close()