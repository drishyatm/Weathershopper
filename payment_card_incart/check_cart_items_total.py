from base_page import base_page
from base_page import verify_temperature
from add_to_cart import *


def verify_the_cart(driver):
    " Verifying the Cart with the number of rows, count of rows and extracting the sum of price"

    count_items_cart = 0
    sum_items_cart = 0
    price_xpath = driver.find_elements_by_xpath(
        "//tbody/descendant::tr/descendant::td[2]")
    for each_column in price_xpath:
        count_items_cart = count_items_cart+1
        print_columns = each_column.text
        print_columns = int(print_columns)
        sum_items_cart = int(sum_items_cart)+int(print_columns)
    print(sum)
    print("count of rows ", count_items_cart)
    return sum_items_cart


def verify_total_cost(sum, driver):
    "Verifying the sum from the calculated cart and displayed "
    xpath_for_total_cost = driver.find_element_by_id('total').text
    total_extract = xpath_for_total_cost.split()[2]
    total_extract = int(total_extract)
    print("screen total", total_extract)
    if (total_extract == sum):
        print("Verified the total and it is correct")
    else:
        print("Total is not correct")


def temperature_go_to_url(driver):
    "redirecting to the url as per the temperature"
    page_flag = verify_temperature(driver)
    if (page_flag == 'M'):
        filter_moisturizer(driver)
    elif (page_flag == 'S'):
        filter_sunscreen(driver)
    else:
        print("flag not found")
