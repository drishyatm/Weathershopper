# Verifying the Cart, number of items and the calculated price


from base_page import *
from add_to_cart import*


def verify_the_cart(driver):
    " Verifying the Cart with the number of rows, count of rows and extracting the sum of price"

    count_of_items = 0
    sum_of_items = 0
    price_xpath = driver.find_elements_by_xpath(
        "//tbody/descendant::tr/descendant::td[2]")
    for each_column in price_xpath:
        count_of_items = count_of_items+1
        print_columns = each_column.text
        print_columns = int(print_columns)
        sum_of_items = int(sum_of_items)+int(print_columns)
    print(sum_of_items)
    print("count of rows ", count_of_items)
    return sum_of_items


def verify_total_cost(sum_of_items, driver):
    "Veifying the cart total and displayed total"
    xpath_for_total_cost = driver.find_element_by_id('total').text
    total_extract = xpath_for_total_cost.split()[2]
    total_extract = int(total_extract)
    print("screen total", total_extract)
    if (total_extract == sum_of_items):
        print("Verified the total and it is correct")
    else:
        print("Total is not correct")


if __name__ == '__main__':
    #launch the main URL current temperature
    driver = current_temperature_page()
    driver= verify_title(driver)
    page_flag = verify_temperature(driver)
    if (page_flag == 'M'):
        filter_moisturizer(driver)
    elif (page_flag == 'S'):
        filter_sunscreen(driver)
    else:
        print("flag not found")

    # Verify in Cart
    click_cart_button(driver)
    sum_of_items= verify_the_cart(driver)
    verify_total_cost(sum_of_items, driver)
    # close the Browser
    close_browser(driver)
