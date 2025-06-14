## Overview
Create an automated test for this scenario:
1. Go to https:/ /www.lazada.vn/
2. If you get a captcha confirmation pop up, please refer to your country’s Lazada.
3. Search product “Logitech Keyboard”
4. Set the price filter from “150.000” to “4.000.000”
5. Sort the item to Low price to High
6. Obtain all the item names from page 1 to page 3
7. Optional, but preferable, export the result into an .xlsx file

## WebDriver Setup
# Ensure you have ChromeDriver installed and its path configured.
# Download from: https://chromedriver.chromium.org/downloads
# Make sure the ChromeDriver version matches your Chrome browser version.
# If chromedriver is not in your system's PATH, specify its executable_path:
# service = ChromeService(executable_path='/path/to/your/chromedriver')

## Dependencies (need to install)
- selenium
- pytest
- webdriver-manager
- pandas
-> pip install selenium pandas webdriver-manager


## Running Tests
python3 -m pytest tests/
pytest --pytest-html <dir> tests/