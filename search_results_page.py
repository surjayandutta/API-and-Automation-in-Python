from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver
        self.result_stats = (By.ID, "result-stats")  # Locator for result stats

    def get_result_stats(self):
        return self.driver.find_element(*self.result_stats).text