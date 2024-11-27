"""
Owner : Hiranmayee Kamde
Assignment :    Automation Analyst Assignment
Project submission Date : 27/11/2024
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# REQUIRED FOR SCROLL DOWN OR UP
from selenium.webdriver.common.keys import Keys
# REQUIRED FOR DRAG AND DROP
from selenium.webdriver import ActionChains
# REQUIRE FOR IMAGE COMPAIR
from PIL import Image


def test_FitPeo_Homepage():
    driver = webdriver.Chrome()
    driver.maximize_window()
    # Step 1 : Open and Navigate to the FitPeo homepage
    driver.get("https://www.fitpeo.com")
    driver.implicitly_wait(10)
    assert driver.current_url == "https://www.fitpeo.com/"
    # Provides delay to observe interactions
    time.sleep(2)

    # Step 2 : Navigate to the Revenue Calculator Page:
    folder = driver.find_element(By.XPATH, "//div[contains(text(),'Revenue Calculator')]")
    folder.click()
    time.sleep(2)
    assert driver.current_url == "https://www.fitpeo.com/revenue-calculator"
    time.sleep(2)

    # Step 3 : Scroll Down to the Slider section:
    scroll = driver.find_element(By.XPATH, "//h4[contains(text(),'Medicare Eligible Patients')]")
    driver.execute_script('arguments[0].scrollIntoView(true)', scroll)
    time.sleep(2)

    # Step 4 : Adjust the Slider:
    slider = driver.find_element(By.XPATH, "//span[@data-index='0']")
    ActionChains(driver).drag_and_drop_by_offset(slider, 94, 0).perform()
    time.sleep(2)
    value = driver.find_element(By.XPATH, "//input[(@type='number')]")
    input_val = value.get_attribute('value')
    print("The value in Text Box =", input_val)
    assert input_val == "823"

    # Step 5 : Update the Text Field:
    input_ele = driver.find_element(By.XPATH, "//input[(@type='number')]")
    input_ele.send_keys(Keys.CONTROL + "a")
    input_ele.send_keys(Keys.BACKSPACE)
    input_ele.screenshot("slider_screenshot_0.png")
    print("Screenshot of element saved.")
    time.sleep(2)
    new_value = '560'
    input_ele.send_keys(new_value)
    entered_value = input_ele.get_attribute("value")
    print("Value entered into input box =", entered_value)
    time.sleep(2)
    assert entered_value == new_value

    # Step 6 :Validate Slider Value:
    slider_ele = driver.find_element(By.XPATH, "//div[(@class='MuiBox-root css-j7qwjs')]")
    slider_ele.screenshot("slider_screenshot_560.png")
    print("Screenshot of element saved.")

    # Calculate image Hash
    # actual_hash = imagehash.average_hash(Image.open("slider_screenshot_0.png"))
    # expected_hash = imagehash.average_hash(Image.open("slider_screenshot_560.png"))

    # Assert similarity
    # assert actual_hash != expected_hash
    time.sleep(5)

    # Step 7: Select CPT Codes:
    scroll_to_CPT_99091= driver.find_element(By.XPATH,"//div[(@class='MuiBox-root css-m1khva')]")
    driver.execute_script('arguments[0].scrollIntoView(true)',scroll_to_CPT_99091)
    time.sleep(2)

    # Click Check box of CPT_99091
    check_box_CPT_99091 = driver.find_element(By.XPATH,"//span[text()='57']")
    check_box_CPT_99091.click()
    time.sleep(2)
    # Click Check box of CPT-99453
    check_box_CPT_99453 = driver.find_element(By.XPATH,"//span[text()='19.19']")
    check_box_CPT_99453.click()
    time.sleep(2)
    # Click Check box of CPT-99454
    check_box_CPT_99454 = driver.find_element(By.XPATH,"//span[text()='63']")
    check_box_CPT_99454.click()
    time.sleep(2)
    # Click Check box of CPT-99474
    check_box_CPT_99474 = driver.find_element(By.XPATH,  "//span[text()='15']")
    check_box_CPT_99474.click()
    time.sleep(2)

    # Step 8 and Step 9: Verify that the header displaying Total Recurring Reimbursement for all Patients Per Month : shows the value $110700.
    input_ele = driver.find_element(By.XPATH, "//input[(@type='number')]")
    input_ele.send_keys(Keys.CONTROL + "a")
    input_ele.send_keys(Keys.BACKSPACE)
    time.sleep(2)
    new_value = '820'

    input_ele.send_keys(new_value)
    entered_value = input_ele.get_attribute("value")
    print("Value entered into input box =", entered_value)
    time.sleep(2)
    assert entered_value == new_value

    # Scroll Just to display popup
    scroll_to_CPT_99091 = driver.find_element(By.XPATH, "//div[(@class='MuiBox-root css-m1khva')]")
    driver.execute_script('arguments[0].scrollIntoView(true)', scroll_to_CPT_99091)
    time.sleep(2)

    TRR_per_month = driver.find_element(By.XPATH,"(//p[text()='$' and text()='110700'])[1]")
    print("TRR_value",TRR_per_month.text)
    assert TRR_per_month.text == '$110700'