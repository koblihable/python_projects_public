from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os
from datetime import datetime

USER_EMAIL = os.environ.get("EMAIL")
USER_PWD = os.environ.get("PASSWORD")
WEBSITE_URL = "https://appbrewery.github.io/gym/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# create a folder with user data
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

# keep all preferences settings
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

# run selenium and return webpage
driver = webdriver.Chrome(options=chrome_options)
driver.get(WEBSITE_URL)

wait = WebDriverWait(driver, 2)

# log into the gym website
login_button = wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
login_button.click()

email_input = wait.until(ec.element_to_be_clickable((By.ID, "email-input")))
email_input.click()
email_input.send_keys(USER_EMAIL)

password_input = wait.until(ec.element_to_be_clickable((By.ID, "password-input")))
password_input.click()
password_input.send_keys(USER_PWD)

submit_button = wait.until(ec.element_to_be_clickable((By.ID, "submit-button")))
submit_button.click()

# find Tuesday HIIT classes
wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))

tuesday_classes = driver.find_element(By.CSS_SELECTOR, value="div[id^='day-group-tue']")
hiit_classes = tuesday_classes.find_elements(By.CSS_SELECTOR, value="div[id^='class-card-hiit']")
hiit_buttons = [hiit_class.find_element(By.CSS_SELECTOR, value="button[id^='book-button-hiit']") for hiit_class in hiit_classes]

# get date and time of the booked class
def get_date_and_time(button_id):
    date_str = button_id[-15:]
    date_format = "%Y-%m-%d-%H%M"
    return datetime.strptime(date_str, date_format)

# Book first available class or join waiting list
for button in hiit_buttons:
    availability = button.text
    class_date_obj = get_date_and_time(button.get_attribute("id"))
    class_date = f"{class_date_obj.strftime('%a %b %d')} at {class_date_obj.strftime('%H:%M')}"
    if availability == "Book Class" or availability == "Join Waitlist":
        button.click()
        if availability == "Book Class":
            print(f"Class booked for {class_date}.")
        else:
            print(f"Joined waiting list for {class_date}.")
        break
    else:
        print(f"class for {class_date} is already booked.")