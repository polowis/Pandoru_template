from app.config import Config
from selenium import webdriver
def getDriver():
    """Get web driver"""
    driver = Config.SELENIUM_DRIVER.lower()
    if driver == 'chrome':
        return webdriver.Chrome()

    elif driver == "firefox":
        return webdriver.Firefox()

    elif driver == 'ie':
        return webdriver.Ie()

    elif driver == 'opera':
        return webdriver.Opera()

    elif driver == 'edge':
        return webdriver.Edge()