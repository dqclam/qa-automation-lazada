
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, pytest
import pandas as pd


def wait_for_element(driver, by, identifier, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, identifier)))

def search_product(driver, keyword):
    search_box = wait_for_element(driver, By.ID, "q")
    search_box.clear()
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.RETURN)


def set_price_filter(driver, min_price, max_price):
    wait_for_element(driver, By.CSS_SELECTOR, "input[placeholder='Min']").send_keys(min_price)
    wait_for_element(driver, By.CSS_SELECTOR, "input[placeholder='Max']").send_keys(max_price)
    wait_for_element(driver, By.XPATH, "//button[@class='ant-btn css-1bkhbmc app ant-btn-primary ant-btn-icon-only yUcnk']").click()
    time.sleep(1)

def sort_low_to_high(driver):
    sort_dropdown = wait_for_element(driver, By.CLASS_NAME, "ant-select-selector")
    sort_dropdown.click()
    low_to_high_option = wait_for_element(driver, By.XPATH, "//*[contains(text(), 'Price low to high')]")
    low_to_high_option.click()
    time.sleep(1)

def scrape_product_names(driver, num_pages=3):
    all_item_names = []
    for page_num in range(1, num_pages + 1):
        print(f"\nScraping items from Page {page_num}")
        wait_for_element(driver, By.CSS_SELECTOR, "div[data-qa-locator='product-item']")
        items = driver.find_elements(By.CSS_SELECTOR, "div[data-qa-locator='product-item']")
        for item in items:
            try:
                name = item.find_element(By.CSS_SELECTOR, "div[data-qa-locator='product-item'] .RfADt a").get_attribute("title")
                all_item_names.append(name)
                print(f"Found item: {name}")
            except:
                continue

        if page_num < num_pages:
            next_page_button = wait_for_element(driver, By.CSS_SELECTOR, ".ant-pagination-next .ant-pagination-item-link")
            if next_page_button.is_enabled():
                next_page_button.click()
                print(f"Clicked to navigate to page {page_num + 1}.")
            else:
                print("Next page button is disabled or not found. Assuming last page.")
                break
        else:
            print(f"Reached desired number of pages (Page {num_pages}).")
    return all_item_names


def export_to_file(item_list, filename="lazada_logitech_items.csv"):
    df = pd.DataFrame(item_list)
    try:
        df.to_csv(filename, index=False)
        print(f"\nSuccessfully exported {len(item_list)} items to '{filename}'.")
    except Exception as e:
        print(f"Error exporting data : {e}")
        pytest.fail(f"Failed to export data: {e}")
