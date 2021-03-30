from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

#1 Khai bao browser
browser = webdriver.Chrome(executable_path="./chromedriver")

#2 Mo URL cua post
browser.get("https://www.facebook.com/groups/miagroup/permalink/730028114435130/")
sleep(random.randint(5,10)) #sleep trong ngau nhien tu 5 toi 10 giay de FB ko phat hien la may

#3 Lay link hien comment
showcomment link = browser.find_element_by_xpath("link chia thang vao trang can lay")
showcomment_link.click()
sleep(5)
#4 Lay comment
showmore_link = browser.find_element_by_xpath("Xem cac binh luan truoc")
showmore_link.click()
sleep(5)

showmore_link.click()
sleep(5)
#5 Tim tat ca cac comment va ghi ra man hinh (hoac file)
#--> lay all the div co thuoc tinh aria-label='Binh luan'
comment_list = browser.find_elements_by_xpath("cho x path vao day. VD: //div[@aria-label='Binh luan']")

# Lap trong tat ca cac comment va hien thi noi dung comment ra man hinh
for comment in comment_list
    # hien thi ten nguoi va noi dung, cach nhau boi dau:
    poster = comment.find_element_by_class_name("id cua ten nguoi binh luan")
    content = comment.find_element_by_class_name("ten class name content")
    print("*",poster.text,":",content.text) 

#3 Dong browser
browser.close()