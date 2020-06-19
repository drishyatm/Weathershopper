import time
import selenium
from selenium import webdriver

 # Create an instance of Firefox WebDriver
driver = webdriver.Firefox()

 # url would be provided here and open. 
url = 'https://weathershopper.pythonanywhere.com/moisturizer'
driver.get(url)
 # Check if the title of the page is proper
if(driver.title=="The Best Moisturizers in the World!"):
       print ("Success: Moisturizers Page launched")
else:
       print ("Failed: Moisturizers Page not launched")


button_list=[]
#button=driver.find_element_by_xpath("html/body/div[1]/div[2]/div[1]/button[contains(text(),'Add')]")
buttons_list = driver.find_elements_by_xpath("//div[contains(@class,'text-center')]/child::button")
for each_button in buttons_list:
    each_button.click()
    time.sleep(1)
    





# Quit the browser window
time.sleep(3)
driver.quit() 