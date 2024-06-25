from selenium import webdriver
from selenium.webdriver.chrome.service import Service
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
# Maximize the browser window
        self.driver.maximize_window()

    def quit(self):
        self.driver.quit()  # Close the browser session

    def Positivelogin(self):
        self.boot()  # Start the browser and navigate to the URL
        sleep(3)  # Wait to ensure the page has fully loaded

# Locating username and entering the value
        username = self.driver.find_element(By.XPATH,
                                            '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
        username.send_keys("Admin")

# Locating the password and entering the password
        password = self.driver.find_element(By.XPATH,
                                            '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
        password.send_keys("admin123")


        loginbutton = self.driver.find_element(By.XPATH,
                                               '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
        loginbutton.click()

        print("The User is logged in successfully !!!")
        sleep(3)
        self.quit()


# Creating an instance of the Orange class with the URL
obj = Orange("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
obj.Positivelogin()
