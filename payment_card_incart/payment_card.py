from base_page import base_page
from base_page import verify_temperature
from add_to_cart import *
from check_cart_items_total import temperature_got_to_url, verify_the_cart, verify_total_cost


def payment_click(driver):
    driver.find_element_by_xpath(
        "//body/div[1]/div[3]/form/button/span").click()
    # //button/span[contains(text(),'Pay with Card')]
    print("Clicked")
    time.sleep(3)


def enter_details_to_payment(driver):
    # switch to frame
    # driver.switch_to_frame(driver.find_element_by_xpath(
    #  "//iframe[contains(@name,'stripe checkout app')]"))
    driver.switch_to_frame(
        driver.find_element_by_class_name("stripe_checkout_app"))
    # Enter the name
    email = driver.find_element_by_xpath("//input[@type='email']")
    email.send_keys('drishyatm@qxf2.com')
    time.sleep(1)
    # Enter card details
    driver.find_element_by_xpath(
        "//input[@type='tel'][@placeholder='Card number']").send_keys('6200000000000005')
    driver.find_element_by_xpath(
        "//input[@type='tel'][@placeholder='MM / YY']").send_keys('0921')
    driver.find_element_by_xpath(
        "//input[@type='tel'][@placeholder='CVC']").send_keys('137')
    time.sleep(2)
    driver.find_element_by_xpath(
        "//input[@type='tel'][@autocomplete='postal-code']").send_keys('560036')
    time.sleep(3)
    # verifying checkbox
    checkbox = driver.find_element_by_class_name("Checkbox")
    # if check box is not selected then click the checkbox
    if(not checkbox.is_selected()):
        checkbox.click()
    # enter phone number
    driver.find_element_by_xpath(
        "//input[@type='tel'][@autocomplete='mobile tel']").send_keys('1234567890')

    time.sleep(2)
    driver.find_element_by_xpath("//button[@type='submit']").click()
    time.sleep(3)


def verify_payment(driver):
    if (driver.title == 'Confirmation'):
        print("successfull payment")
    else:
        print(" not successfull")


if __name__ == '__main__':
    driver = base_page
    temperature_got_to_url(driver)
    # Verify in Cart
    go_to_cart(driver)
    sum = verify_the_cart(driver)
    verify_total_cost(sum, driver)
    payment_click(driver)
    enter_details_to_payment(driver)
    verify_payment(driver)
    # close the Browser
    close_browser(driver)
