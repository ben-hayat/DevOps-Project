import sys, os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#purpose: test our web service.
#Input: the application URL as an input,
#Do: open a browser to that URL, select the score element in our web page, check that it is a number between 1 to 1000
# and return a boolean value if it’s true or not.
def test_scores_service (app_url):
    driver = webdriver.Chrome(executable_path=r'C:\Ben\DeVOps\chromedriver_win32_83\chromedriver.exe')
    wait = WebDriverWait(driver, 3)
    visible = EC.visibility_of_element_located
    time.sleep(1)
    driver.get(app_url)
    # Getting browser current page title
    #print("url: " + drivel)r.current_ur
    #print("title: " + driver.title)
    try:
        element = driver.find_element(By.ID, "score")
        print("score is: " + element.text + " And return value is : " + str((1000 > int(element.text) > 1)))
        return (1000 > int(element.text) > 1)
    except:
        print (app_url + " is not available !!!")
        return False
#purpose: call our tests function.
#output : return -1 as an OS exit code if the tests failed and 0 if they passed.
def main_function ():
    return sys.exit(-1)

#debug
test_scores_service("http://127.0.0.1:5000/")
#main_function()