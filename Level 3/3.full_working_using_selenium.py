from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path='C:\\Users\\Forge\\Downloads\\chrome\\chromedriver.exe')
driver.get('https://mail.google.com/mail/u/0/#inbox')
emailid=driver.find_element_by_id("identifierId")
emailid.send_keys("harshavardhan.19.1@protosem.tech")
nextBut=driver.find_element_by_id("identifierNext")
nextBut.click()
time.sleep(3)
Pw=driver.find_element_by_name("password")
Pw.clear()
Pw.send_keys("Harsrosh@671")
nextBut2=driver.find_element_by_id("passwordNext")
nextBut2.click()
time.sleep(3)
#inbox = driver.find_element_by_class("//*[contains(@title,'Inbox')]").text
inbox =driver.find_element_by_id(":hu").text
l=inbox.split()
print ('Unread:'+l[1])
