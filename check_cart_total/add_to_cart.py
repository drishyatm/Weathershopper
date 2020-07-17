# Adding the items to the cart as per the instructions provided 
import time
from base_page import *


def get_product_price(product_text):
    "Parse the product price from the product text"
    price = product_text.split("Price:")[-1]
    price = price.split("Rs.")[-1]
    price = price.split("\n")[0]
    price = int(price)

    # print(price)

    return price


def get_least_expensive(actual_price):
    " Method to find the least expensive"
    least_value = 1000
    for each_value in actual_price:
        if each_value < least_value:
            least_value = each_value

   
    return least_value


def add_to_cart(least_expensive, driver):
    " Adding the least expensive one to the Cart"
    converted_least_expensive = str(least_expensive)
    xpath_button = "//div[contains(@class,'col-4') and contains(.,'{}')]/descendant::button[text()='Add']".format(
        converted_least_expensive)

    driver.find_element_by_xpath(xpath_button).click()
    
    time.sleep(3)
 


def click_cart_button(driver):
    " Verify the cart has the item"
    cart = driver.find_element_by_xpath("//button[contains(text(),'Cart')]")
    cart.click()
    time.sleep(2)
    if (driver.title == "Cart Items"):
        print("Success: Cart Page launched")
    else:
        print("Failed: Cart Page not launched")


def price_extract(product_price_list, driver):
    "extract the price from the page for the product"
    actual_price = []
    product_list = []
    # Xpath finder for Price
    product_list = driver.find_elements_by_xpath("//div[contains(@class,'col-4') and contains(.,'{}')]/descendant::p[2]".format(
        product_price_list))

    for each_price in product_list:
        price_split = each_price.text
        actual_price.append(get_product_price(price_split))

    return actual_price


def close_browser(driver):
    # Quit the browser window
    time.sleep(3)
    driver.quit()



def calculate_least_expensive(filter, driver):
    "calculate the least expensive"

    product_price_list = price_extract(filter, driver)

    # finding the least expensive
    #least_expensive = get_least_expensive(product_price_list)
    least_expensive = min(product_price_list)
    print("least expensive ", least_expensive)

    # Click on Add to cart
    add_to_cart(least_expensive, driver)


def filter_moisturizer(driver):
    "filter the moisturizer Aloe and Almond"
    # need to handle the case here
    filter1 = 'Aloe'
    filter2 = 'Almond'
    calculate_least_expensive(filter1, driver)
    calculate_least_expensive(filter2, driver)


def filter_sunscreen(driver):
    "filter the sunscreen spf 50 and spf 30"
    # need to handle the case here
    filter1 = 'SPF-50'
    filter2 = 'SPF-30'
    calculate_least_expensive(filter1, driver)
    calculate_least_expensive(filter2, driver)
