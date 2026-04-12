import wait
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


RENTAL_URL = "https://appbrewery.github.io/Zillow-Clone/"


# get the contents of the San Francisco rentals website
contents = requests.get(RENTAL_URL).text
bs_contents = BeautifulSoup(contents, "html.parser")

# find all rental cards with all the information
rental_cards = bs_contents.find_all(name="div", class_="StyledCard-c11n-8-84")
cards = {}
i = 1
for card in rental_cards[:5]:
    card_dict = {
        "address": card.find(name="address").text.strip(),
        "price": card.find(name="span", class_="PropertyCardWrapper__StyledPriceLine").text,
        "link": card.a.get("href")
    }
    cards[str(i)] = card_dict
    i += 1
    print(card_dict)

# set up selenium driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 2)

# use selenium to get the form and fill in the rental details

form_url = "..."
driver.get(form_url)

for card in cards.values():
    driver.get(form_url)

    # get and fill in the input elements
    address_input = wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    address_input.click()
    address_input.send_keys(card["address"])
    price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.click()
    price_input.send_keys(card["price"])
    link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.click()
    link_input.send_keys(card["link"])

    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()

    new_form_link = wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a'))).get_attribute("href")
    form_url = new_form_link