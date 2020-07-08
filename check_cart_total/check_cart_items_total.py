from base_page import weather_shopper_page, verify_temperature
from add_to_cart import go_to_cart, filter_moisturizer, filter_sunscreen, close_browser


def verify_the_cart(driver):
    # Verifying the Cart with the number of rows, count of rows and extracting the sum of price

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
    driver = weather_shopper_page()
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
