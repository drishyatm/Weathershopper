import time
from selenium import webdriver


def base_page_2():
    # Create an instance of Firefox WebDriver
    driver = webdriver.Chrome()
    url = 'https://weathershopper.pythonanywhere.com/moisturizer'
    driver.get(url)
    # Check if the title of the page is proper
    if(driver.title == "The Best Moisturizers in the World!"):
        print("Success: Moisturizers Page launched")
    else:
        print("Failed: Moisturizers Page not launched")

    return driver
