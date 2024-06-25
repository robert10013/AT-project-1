from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
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
       #Quiting function
       self.driver.quit()

   def AddPIM(self):

       self.boot()
       sleep(3)
       username = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
# Passing username
       username.send_keys("Admin")
       password = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
# Passing password
       password.send_keys("admin123")
       loginbutton = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
       loginbutton.click()
       sleep(3)
# Clicking on PIM module
       PIM=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
       PIM.click()
       sleep(3)
# Adding employee details
       addpim=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')
       addpim.click()
       sleep(3)
# Passing firstname, lastname, employeeid values
       fname=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input')
       fname.send_keys("Robee")
       Lname=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input')
       Lname.send_keys("raj")
       empid=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input')
       empid.send_keys("1995")
       save1 = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')
       save1.click()
       sleep(5)
       print("New employee is added successfully !!!")

# Passing URL into the class to perform all activities
obj = Orange("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# Adding PIM
obj.AddPIM()