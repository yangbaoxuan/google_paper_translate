from googletrans import Translator
from selenium import webdriver
import socks
import socket
import os
import time

browser = webdriver.Chrome('D:\Program Files (x86)\chromedriver\chromedriver.exe')

def zh(text):
    url='https://translate.google.cn/#view=home&op=translate&sl=auto&tl=zh-CN&text='+text
    browser.get(url)
    time.sleep(5)
    jg=browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div/span[1]')
    return jg.text


socks.set_default_proxy(proxy_type=socks.SOCKS5, addr="127.0.0.1", port=10808, rdns=True, )
socket.socket = socks.socksocket
outfile='temp.txt'
imputfile="bare_conf.pdf"
os.system("pdf2txt.py  -o "+outfile+" "+imputfile)
f = open(outfile,"r",encoding='utf-8')   #设置文件对象
str = f.read()     #将txt文件的所有内容读入到字符串str中
str=str.replace('\n\n','000000')
str=str.replace('-\n','')
str=str.replace('\n',' ')
str=str.replace('000000','\n')

str_len=len(str)
pp=''
strs=str.split('\n')
stt=''
for i in strs:
     stt+=i+'%0A'
     while len(stt)>4000:
       src_text=stt
       t=zh(src_text)
       pp+=t+'\n'
       stt=''
src_text=stt
t=zh(src_text)
pp+=t
f2=open("tt.txt","w+",encoding='utf-8')
f2.write(pp)
f2.close()
