# Opening the page Weather Shopper
import time
from selenium import webdriver

# Create an instance of Firefox WebDriver
driver = webdriver.Firefox()

# url would be provided here and open.
URL = 'https://weathershopper.pythonanywhere.com'
driver.get(URL)
# Check if the title of the page is proper
if(driver.title == "Current Temperature"):
    print("Success: Weather shopper page launched successfully")
else:
    print("Failed: Weather Shopper page Title is incorrect")
# Reading the Temperature
current_temperature = driver.find_element_by_xpath(
    "//span[@id='temperature']").text
time.sleep(3)

# Verify the temperature
temperature_only = current_temperature.split(" ")[0]
print(temperature_only)

# redirecting to the sunscreen page
if int(temperature_only) > 34:
    print("sunscreen")
    button = driver.find_element_by_xpath(
        "//button[contains(text(),'Buy sunscreens')]")
    button.click()
    if(driver.title == "The Best Sunscreens in the World!"):
        print("Success: Sunscreen Page launched")
    else:
        print("Failed: Sunscreen Page not launched")
# redirecting to the Moisturizers page
elif int(temperature_only) < 19:
    print("moistriser")
    button = driver.find_element_by_xpath(
        "//button[contains(text(),'Buy moisturizers')]")
    button.click()
    if(driver.title == "The Best Moisturizers in the World!"):
        print("Success: Moisturizers Page launched")
    else:
        print("Failed: Moisturizers Page not launched")

time.sleep(4)

# Quit the browser window
driver.quit()
