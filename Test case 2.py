from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import alert
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
class Orange:
   def __init__(self, url):
       self.url = url
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

   def boot(self):

       self.driver.get(self.url)

       sleep(3)
# Maximizing the window
       self.driver.maximize_window()

   def quit(self):
               self.driver.quit()

   def Negativelogin(self):

       self.boot()
       sleep(3)
       username=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
# Entering username
       username.send_keys("Admin")
       password=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
# Entering password
       password.send_keys("Invalid password")
       loginbutton=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')

       loginbutton.click()
       sleep(3)
# warning message
       print("Invalid credentials is displayed !!!")
# Passing url into the class Orange
obj = Orange("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
obj.Negativelogin()