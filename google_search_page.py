from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class GoogleSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.NAME, "q")  # Locator for the search box

    def open(self):
        self.driver.get("https://www.google.com")

    def enter_search_query(self, query):
        self.driver.find_element(*self.search_box).send_keys(query)

    def submit_search(self):
        self.driver.find_element(*self.search_box).send_keys(Keys.RETURN)