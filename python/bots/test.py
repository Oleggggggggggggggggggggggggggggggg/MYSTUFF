"""from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Open a Chrome browser window
driver = webdriver.Chrome()

try:
    # Navigate to a website
    driver.get("https://python.org")
    
    # Locate the search bar element using its name property
    search_bar = driver.find_element(By.NAME, "q")
    
    # Type text and hit Enter
    search_bar.send_keys("automation")
    search_bar.send_keys(Keys.RETURN)
    
    # Let the results load for 5 seconds
    time.sleep(5)

finally:
    # Close the browser windows safely
    driver.quit()"""
