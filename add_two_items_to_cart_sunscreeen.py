# Opening the page Weather Shopper
import time
from selenium import webdriver


def get_product_price(product_text):
    # Parse the product price from the product text
    price = product_text.split("Price:")[-1]
    price = price.split("Rs.")[-1]
    price = price.split("\n")[0]
    price = int(price)

    # print(price)

    return price


def get_least_expensive(actual_price):
    # Method to find the Most expensive
    least_value = 1000
    for each_value in actual_price:
        if each_value < least_value:
            least_value = each_value

   # print("maximum value inside function ", max_value)
    return least_value


def add_to_cart(least_expensive, driver):
    # Adding the most expensive one to the Cart
    converted_least_expensive = str(least_expensive)
    xpath_button = "//div[contains(@class,'col-4') and contains(.,'{}')]/descendant::button[text()='Add']".format(
        converted_least_expensive)

    driver.find_element_by_xpath(xpath_button).click()
    # print("Added to cart")
    time.sleep(3)
    # print("most expensive button is ", xpath_button)


def go_to_cart(driver):
    # Verify the cart has the item
    cart = driver.find_element_by_xpath("//button[contains(text(),'Cart')]")
    cart.click()
    time.sleep(2)
    if (driver.title == "Cart Items"):
        print("Success: Cart Page launched")
    else:
        print("Failed: Cart Page not launched")


def price_extract(filter_by_product, driver):
    actual_price = []
    product_list = []
    # Xpath finder for Price
    product_list = driver.find_elements_by_xpath("//div[contains(@class,'col-4') and contains(.,'{}')]/descendant::p[2]".format(
        filter_by_product))

    for each_price in product_list:
        price_split = each_price.text
        actual_price.append(get_product_price(price_split))

    return actual_price


def close_browser(driver):
    # Quit the browser window
    time.sleep(3)
    driver.quit()


def base_page():
    # Create an instance of Firefox WebDriver
    driver = webdriver.Firefox()
    url = 'https://weathershopper.pythonanywhere.com/sunscreen'
    driver.get(url)
    # Check if the title of the page is proper
    if(driver.title == "The Best Sunscreens in the World!"):
        print("Success: Sunscreen Page launched")
    else:
        print("Failed: Sunscreen Page not launched")

    return driver


def calculate_least_expensive(filter, driver):

    filter_by_product = price_extract(filter, driver)

    # finding the least expensive
    least_expensive = get_least_expensive(filter_by_product)
    print("least expensive ", least_expensive)

    # Click on Add to cart
    add_to_cart(least_expensive, driver)


# ----START OF SCRIPT
if __name__ == '__main__':
    driver = base_page()

    # Filter the Aloe and Almond
    filter1 = 'SPF-50'
    filter2 = 'SPF-30'
    calculate_least_expensive(filter1, driver)
    calculate_least_expensive(filter2, driver)

    # Verify in Cart
    go_to_cart(driver)

    # close the Browser
    close_browser(driver)
