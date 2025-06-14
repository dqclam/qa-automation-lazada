from selenium import webdriver
from utils import *
import pytest


url = "https://www.lazada.vn/"
search_query = "Logitech Keyboard"
min_price = "150000"
max_price = "4000000"

@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("window-size=1240,800")
    # options.add_argument('--incognito')
    # options.add_argument('--headless')
    # options.add_argument('--slow-motions')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.delete_all_cookies()
    driver.quit()

def test_obtain_searched_items(driver):
    
    # 1. Navigate to Lazada Vietnam
    print("Navigating to https://www.lazada.vn/")
    driver.get(url)
    driver.implicitly_wait(10)
    # time.sleep(5)  # Wait for manual captcha if any

    # 2. Search for product "Logitech Keyboard"
    print("Searching for 'Logitech Keyboard'")
    search_product(driver, search_query)

    # 3. Set the price filter
    print("Setting price filter from {} to {}".format(min_price, max_price))
    set_price_filter(driver, min_price, max_price)

    # 4. Sort the item to "Price low to High"
    print("Sorting items by price from low to high")
    sort_low_to_high(driver)

    # 5. Scrape the names of items on the first 3 pages
    print("Scraping item names from the first 3 pages...")
    all_item_names = scrape_product_names(driver, num_pages=3)

    # 6. Export the result into an CSV file
    export_to_file(all_item_names)
