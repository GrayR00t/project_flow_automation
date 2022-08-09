import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

os.chmod("/Users/neerajsingh/chromedriver", 0o755)
s = Service('/Users/neerajsingh/chromedriver')

path = "/Users/neerajsingh/Documents/projects/"
browser = webdriver.Chrome(service = s)
browser.get("https://github.com/login")


def create():
    folderName = str(sys.argv[1])
    os.makedirs(path + folderName)
    python_button = browser.find_element("xpath", "//input[@name='login']")
    python_button.send_keys("ns28@iitbbs.ac.in")
    python_button = browser.find_element("xpath", "//input[@name='password']")
    python_button.send_keys("rc633725")
    python_button = browser.find_element("xpath", "//input[@name='commit']")
    python_button.click()
    browser.get("https://github.com/new")
    python_button = browser.find_element("xpath", '//input[@name="repository[name]"]')
    python_button.send_keys(folderName)
    python_button = browser.find_element("xpath", '//button[@class="btn-primary btn"]')
    python_button.submit()
    browser.quit()


if __name__ == "__main__":
    create()
