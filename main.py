from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
URL="https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
driver_location="C:\Dev\chromedriver"

driver=webdriver.Chrome(driver_location)

driver.get(url=URL)

sign_in=driver.find_element_by_link_text("Sign in")
sign_in.click()
username=driver.find_element_by_id("username")
password=driver.find_element_by_id("password")
username.send_keys("youaremyfire46@gmail.com")
password.send_keys("Sunday")
button=driver.find_element_by_class_name("login__form_action_container ")
button.click()
time.sleep(10)

all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()

    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()

        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text=="":
            phone.send_keys(78895678453)
        
        submit_button = driver.find_element_by_css_selector("footer button")

        if submit_button.get_attribute("data-control-name")=="continue_unify":
            close_button=driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            discard_button=driver.find_element_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("complex application,skipped")

            continue
        else:
            submit_button.click()

        close_button=driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("NO application button , skipped ")
        continue



driver.click()

