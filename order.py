import os 
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import pandas as pd 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

    
import time, datetime

startTime = datetime.datetime(2022, 2, 22, 23, 36, 0)
print('Program not starting yet...')
while datetime.datetime.now() < startTime:
    time.sleep(1)
print('Program now starts on %s' % startTime)


driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")
# driver = webdriver.Edge("C:\Program Files (x86)\Microsoft\Edge\Application\edgedriver_win32\msedgedriver.exe")       
default_url ="https://www.feastogether.com.tw/booking/2"

driver.get(default_url)
note_element=driver.find_element_by_xpath("/html/body/div[12]/div/div/div/button")
time.sleep(1)
note_element.click()
menu_element=driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[6]/i")
menu_element.click()

#ID & Password 
cell_number_element=driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[6]/ul/li[4]/form/ul/li[1]/input")
cell_number_element.send_keys("YOUR_ID")
time.sleep(1)

password_element=driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[6]/ul/li[4]/form/ul/li[2]/input")
password_element.send_keys("YOUR_PASSWORD")
time.sleep(1)

#Login Enter 
login_element=driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[6]/ul/li[4]/form/ul/li[4]/button")
login_element.send_keys(Keys.ENTER)

#Alert (need to use WebDriverWait to wait until the alert is present) 
WebDriverWait(driver, 3).until(EC.alert_is_present())
driver.switch_to.alert.accept()

#Input Numbers
people_number_element=driver.find_element_by_xpath("/html/body/div[4]/div/div/div/ul/li[2]/input")
people_number_element.send_keys("4")

#Select Dates 
date= WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div/ul/li[3]/div/input")))
driver.execute_script(f"arguments[0].setAttribute('value', '2022-04-20')", date)

#Serach Lunch Time 
time_element=driver.find_element_by_xpath("/html/body/div[4]/div/div/div/ul/li[4]/div/ul/li[1]")
driver.execute_script("arguments[0].click();", time_element)
time.sleep(2)

#Select Branch 
store_list=driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[4]/div[2]/table/tr[3]/td[1]/div/span[2]")
driver.execute_script("arguments[0].click();", store_list)

#Select time again 
time_list=driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[2]/ul[1]/li[5]/select/option[3]")
time_list.click()

print('Finishing program...')
#Submit
# submit=driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[2]/ul[2]/li[4]/button")
# driver.execute_script("arguments[0].click();", submit)

