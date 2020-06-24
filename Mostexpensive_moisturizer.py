# Opening the page Weather Shopper
import time
from selenium import webdriver


def get_product_price(product_text):
    # Parse the product price from the product text
    price = product_text.split("Price: ")[-1]
    price = price.split("Rs.")[-1]
    price = price.split("\n")[0]
    price = int(price)

    # print(price)

    return price


def get_most_expensive(actual_price):
    # Method to find the Most expensive
    max_value = 1
    for each_value in actual_price:
        if each_value > max_value:
            max_value = each_value

   # print("maximum value inside function ", max_value)
    return max_value


def add_to_cart(most_expensive, driver):
    # Adding the most expensive one to the Cart
    converted_most_expensive = str(most_expensive)
    xpath_button = "//div[contains(@class,'col-4') and contains(.,'{}')]/descendant::button[text()='Add']".format(
        converted_most_expensive)

    driver.find_element_by_xpath(xpath_button).click()
    #print("Added to cart")
    time.sleep(3)
    #print("most expensive button is ", xpath_button)


def go_to_cart(driver):
    # Verify the cart has the item
    cart = driver.find_element_by_xpath("//button[contains(text(),'Cart')]")
    cart.click()
    time.sleep(2)
    if (driver.title == "Cart Items"):
        print("Success: Cart Page launched")
    else:
        print("Failed: Cart Page not launched")


def call_browser():
    # Create an instance of Firefox WebDriver
    driver = webdriver.Chrome()
    url = 'https://weathershopper.pythonanywhere.com/moisturizer'
    driver.get(url)
    # Check if the title of the page is proper
    if(driver.title == "The Best Moisturizers in the World!"):
        print("Success: Moisturizers Page launched")
    else:
        print("Failed: Moisturizers Page not launched")

    # Xpath finder for Price
    product_text = driver.find_elements_by_xpath(
        "//div[contains(@class,'text-center')]/child::p[2]")

    # Get only the price value
    actual_price = []
    for each_price in product_text:
        price_split = each_price.text
        actual_price.append(get_product_price(price_split))
    """
    for this_price in actual_price:
        print(this_price)
    """
    # finding the most expensive
    most_expensive = get_most_expensive(actual_price)
    print("most expensive ", most_expensive)

    # Click on Add to cart
    add_to_cart(most_expensive, driver)

    #Verify in Cart
    go_to_cart(driver)

    # close the Browser
    close_browser(driver)


def close_browser(driver):
    # Quit the browser window
    time.sleep(3)
    driver.quit()


# ----START OF SCRIPT
if __name__ == '__main__':
    call_browser()
