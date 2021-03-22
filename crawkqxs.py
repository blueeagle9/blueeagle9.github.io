from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random

browser = webdriver.Chrome(executable_path="chromedriver")
browser.get("https://xoso.me/xsmn-sxmn-kqxsmn-ket-qua-xo-so-mien-nam.html")
sleep(2)
Input_data=978916
Vi_tri_dai=3

Dai_trai=browser.find_elements_by_xpath('/html/body/section/div[1]/div[3]/div[2]/div[1]/table/tbody/tr[1]/th[2]/a')
for dai1 in Dai_trai:
    dai1.text
Dai_giua=browser.find_elements_by_xpath('/html/body/section/div[1]/div[3]/div[2]/div[1]/table/tbody/tr[1]/th[3]/a')
for dai2 in Dai_giua:
    dai2.text
Dai_phai=browser.find_elements_by_xpath('/html/body/section/div[1]/div[3]/div[2]/div[1]/table/tbody/tr[1]/th[4]/a')
for dai3 in Dai_phai:
    dai3.text
#Giai tam:
giai_tam=browser.find_elements_by_css_selector('#load_kq_mn_0 > div.three-city > table > tbody > tr.g8')
for g8 in giai_tam:
    a=g8.text
lst_giai_tam=[]
for giai8 in a.split():
    if giai8[0]=='0':
        lst_giai_tam.append(giai8)
    else:
        if giai8.isdigit():
            lst_giai_tam.append(giai8)

#Giai bay:
giai_bay=browser.find_elements_by_css_selector('#load_kq_mn_0 > div.three-city > table > tbody > tr:nth-child(3)')
for g7 in giai_bay:
    b=g7.text
lst_giai_bay=[]
for giai7 in b.split():
    if giai7[0]=='0':
        lst_giai_bay.append(giai7)
    else:
        if giai7.isdigit():
            lst_giai_bay.append(giai7)

#Giai sau:
giai_sau=browser.find_elements_by_css_selector('#load_kq_mn_0 > div.three-city > table > tbody > tr:nth-child(4)')
for g6 in giai_sau:
    c=g6.text
lst_giai_sau=[]
for giai6 in c.split():
    if giai6[0]=='0':
        lst_giai_sau.append(giai6)
    else:
        if giai6.isdigit():
            lst_giai_sau.append(giai6)

#Giai nam:
giai_nam=browser.find_elements_by_css_selector('#load_kq_mn_0 > div.three-city > table > tbody > tr:nth-child(5)')
for g5 in giai_nam:
    d=g5.text
lst_giai_nam=[]
for giai5 in d.split():
    if giai5[0]=='0':
        lst_giai_nam.append(giai5)
    else:
        if giai5.isdigit():
            lst_giai_nam.append(giai5)

#Giai bon:
giai_bon=browser.find_elements_by_css_selector('#load_kq_mn_0 > div.three-city > table > tbody > tr:nth-child(6)')
for g4 in giai_bon:
    e=g4.text
lst_giai_bon=[]
for giai4 in e.split():
    if giai4[0]=='0':
        lst_giai_bon.append(giai4)
    else:
        if giai4.isdigit():
            lst_giai_bon.append(giai4)

#Giai ba:
giai_ba=browser.find_elements_by_css_selector('#load_kq_mn_0 > div.three-city > table > tbody > tr:nth-child(7)')
for g3 in giai_ba:
    f=g3.text
lst_giai_ba=[]
for giai3 in f.split():
    if giai3[0]=='0':
        lst_giai_ba.append(giai3)
    else:
        if giai3.isdigit():
            lst_giai_ba.append(giai3)

#Giai nhi:
giai_nhi=browser.find_elements_by_css_selector('#load_kq_mn_0 > div.three-city > table > tbody > tr:nth-child(8)')
for g2 in giai_nhi:
    g=g2.text
lst_giai_nhi=[]
for giai2 in g.split():
    if giai2[0]=='0':
        lst_giai_nhi.append(giai2)
    else:
        if giai2.isdigit():
            lst_giai_nhi.append(giai2)

#Giai nhat:
giai_nhat=browser.find_elements_by_css_selector('#load_kq_mn_0 > div.three-city > table > tbody > tr:nth-child(9)')
for g1 in giai_nhat:
    h=g1.text
lst_giai_nhat=[]
for giai1 in h.split():
    if giai1[0]=='0':
        lst_giai_nhat.append(giai1)
    else:
        if giai1.isdigit():
            lst_giai_nhat.append(giai1)

#Giai dac biet:
giai_db=browser.find_elements_by_css_selector('#load_kq_mn_0 > div.three-city > table > tbody > tr.gdb')
for gdb in giai_db:
    i=gdb.text
lst_giai_db=[]
for giaidb in i.split():
    if giaidb[0]=='0':
        lst_giai_db.append(giaidb)
    else:
        if giaidb.isdigit():
            lst_giai_db.append(giaidb)

browser.close()

ketqua_dai_trai=[lst_giai_tam[0],lst_giai_bay[0],lst_giai_sau[0],lst_giai_sau[1],lst_giai_sau[2],lst_giai_nam[0],
    lst_giai_bon[0],lst_giai_bon[1],lst_giai_bon[2],lst_giai_bon[3],lst_giai_bon[4],lst_giai_bon[5],lst_giai_bon[6],
    lst_giai_ba[0],lst_giai_ba[1],lst_giai_nhi[0],lst_giai_nhat[0],lst_giai_db[0]]

ketqua_dai_giua=[lst_giai_tam[1],lst_giai_bay[1],lst_giai_sau[3],lst_giai_sau[4],lst_giai_sau[5],lst_giai_nam[1],
    lst_giai_bon[7],lst_giai_bon[8],lst_giai_bon[9],lst_giai_bon[10],lst_giai_bon[11],lst_giai_bon[12],lst_giai_bon[13],
    lst_giai_ba[2],lst_giai_ba[3],lst_giai_nhi[1],lst_giai_nhat[1],lst_giai_db[1]]

ketqua_dai_phai=[lst_giai_tam[2],lst_giai_bay[2],lst_giai_sau[6],lst_giai_sau[7],lst_giai_sau[8],lst_giai_nam[2],
    lst_giai_bon[14],lst_giai_bon[15],lst_giai_bon[16],lst_giai_bon[17],lst_giai_bon[18],lst_giai_bon[19],lst_giai_bon[20],
    lst_giai_ba[4],lst_giai_ba[5],lst_giai_nhi[2],lst_giai_nhat[2],lst_giai_db[2]]

if Vi_tri_dai == 1:
    for check in ketqua_dai_trai:
        if check == str(Input_data):
            print("Trung roi")
        else:
            print("Khong trung roi")
if Vi_tri_dai == 2:
    for check1 in ketqua_dai_giua:
        if check1 == str(Input_data):
            print("Trung roi")
        else:
            print("Khong trung roi")
if Vi_tri_dai == 3:
    for check2 in ketqua_dai_phai:
        if check2 == str(Input_data):
            print("Trung roi")
        else:
            print("Khong trung roi")
