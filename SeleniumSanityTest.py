from selenium import webdriver
import unittest

class GetURL(unittest.TestCase):

    def set_up(self):
        self.driver = webdriver.Chrome(executable_path='C:/automation/drivers/chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)


    def get_url(self):
        driver=self.driver
        driver.get("http://192.168.99.100:5000/")
        html_source = driver.page_source
        if "Hello Eli" in html_source:
            print("Test passed Succesfuly")
        else:
            print("Doesnt find this text")


    def Close_browser(self):
        self.driver.quit()

def main():

        getURL = GetURL() # get url
        getURL.set_up()#  set_up function for Running Chrome driver
        driver = getURL.get_url()# Call get_url function for openning http://192.168.99.100:5000/ url
        getURL.Close_browser() #Close and quite from a current browser

if __name__ == '__main__':

      main()
