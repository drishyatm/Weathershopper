from base_page import base_page_1
from base_page import verify_temperature
from add_to_cart import *


def verify_the_cart(driver):
    # Verifying the Cart with the number of rows, count of rows and extracting the sum of price

    count = 0
    """
    count_xpath = driver.find_elements_by_xpath(
        "//tbody/descendant::tr")
    for each_row in count_xpath:
        count = count + 1
        print_rows = each_row.text
        print("count of rows", print_rows)
    print("count of rows ", count)
    """
    sum = 0
    price_xpath = driver.find_elements_by_xpath(
        "//tbody/descendant::tr/descendant::td[2]")
    for each_column in price_xpath:
        count = count+1
        print_columns = each_column.text
        print_columns = int(print_columns)
        sum = int(sum)+int(print_columns)
    print(sum)
    print("count of rows ", count)
    return sum


def verify_total_cost(sum, driver):
    xpath_for_total_cost = driver.find_element_by_id('total').text
    total_extract = xpath_for_total_cost.split()[2]
    total_extract = int(total_extract)
    print("screen total", total_extract)
    if (total_extract == sum):
        print("Verified the total and it is correct")
    else:
        print("Total is not correct")


if __name__ == '__main__':
    driver = base_page_1()
    page_flag = verify_temperature(driver)
    if (page_flag == 'M'):
        filter_moisturizer(driver)
    elif (page_flag == 'S'):
        filter_sunscreen(driver)
    else:
        print("flag not found")

    # Verify in Cart
    go_to_cart(driver)
    sum = verify_the_cart(driver)
    verify_total_cost(sum, driver)
    # close the Browser
    close_browser(driver)
