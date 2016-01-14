
#coding=utf-8
import time
from splinter import Browser

def splinter(url):
    browser = Browser()
    #login qq email websize
    browser.visit(url)
    #wait web element loading
    time.sleep(10)
    #fill in account and password
    browser.find_by_id('idInput').fill('*****')
    browser.find_by_id('pwdInput').fill('*****')
    #click the button of login
    browser.find_by_id('loginBtn').click()
    time.sleep(10)
    #close the window of brower
    browser.driver.close()
    browser.quit()

if __name__ == '__main__':
    websize3 ='http://www.126.com'
    splinter(websize3)
    websize2='http://www.126.com'
    splinter(websize2)
    
