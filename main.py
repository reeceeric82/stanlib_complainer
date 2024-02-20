from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BINARY = "./your_driver_file/your_driver"

NAME = "your_name"
SURNAME = "your_surname"
EMAIL = "your_email"
ID = "your_id_number"
PHONE = "your_phone_number"
COMMENT = "your complaint"


def run():
    # Uncomment the driver your need
    driver = webdriver.Firefox()
    # driver = webdriver.Chrome()
    # driver = webdriver.Edge()

    driver.get("https://stanlib.com/contact-us-individual/")

    dropdown_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "wpforms-16275-field_20")))
    dropdown = Select(dropdown_element)
    dropdown.select_by_visible_text("Complaint")

    first_name_input = driver.find_element(By.ID, "wpforms-16275-field_8")
    first_name_input.send_keys(NAME)

    surname_input = driver.find_element(By.ID, "wpforms-16275-field_9")
    surname_input.send_keys(SURNAME)

    phone_input = driver.find_element(By.ID, "wpforms-16275-field_5")
    phone_input.send_keys(PHONE)

    email_1st_input = driver.find_element(By.ID, "wpforms-16275-field_4")
    email_1st_input.send_keys(EMAIL)
    email_2nd_input = driver.find_element(By.ID, "wpforms-16275-field_4-secondary")
    email_2nd_input.send_keys(EMAIL)

    id_field = driver.find_element(By.ID, "wpforms-16275-field_24")
    id_field.send_keys(ID)

    comment_input = driver.find_element(By.ID, "wpforms-16275-field_6")
    comment_input.send_keys(COMMENT)

    n1_input = driver.find_element(By.CLASS_NAME, "n1")
    n2_input = driver.find_element(By.CLASS_NAME, "n2")
    operation = driver.find_element(By.CLASS_NAME, "cal")

    n1_value = int(n1_input.text)
    n2_value = int(n2_input.text)
    op_value = operation.text

    cap_sum = 0

    if op_value == "+":
        cap_sum = n1_value + n2_value
    elif op_value == "-":
        cap_sum = n1_value - n2_value
    elif op_value == "*":
        cap_sum = n1_value * n2_value
    elif op_value == "/":
        cap_sum = n1_value / n2_value

    captcha = driver.find_element(By.ID, "wpforms-16275-field_10")
    captcha.send_keys(cap_sum)

    submit_button = driver.find_element(By.ID, "wpforms-submit-16275")
    submit_button.click()

    driver.close()


while True:
    run()
