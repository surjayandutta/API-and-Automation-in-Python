import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # Import Keys here
from pages.google_search_page import GoogleSearchPage
from pages.search_results_page import SearchResultsPage

class GoogleSearchTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Initialize the WebDriver
        self.driver.implicitly_wait(10)  # Set implicit wait

    def test_search_selenium(self):
        # Create page objects
        google_search_page = GoogleSearchPage(self.driver)
        search_results_page = SearchResultsPage(self.driver)

        # Open Google and search for "Selenium"
        google_search_page.open()
        google_search_page.enter_search_query("Selenium")
        google_search_page.submit_search()

        # Verify results
        result_stats = search_results_page.get_result_stats()
        self.assertIn("results", result_stats)  # Assert that results are displayed

    def tearDown(self):
        self.driver.quit()  # Close the browser