from selenium import webdriver  
import time

driver = webdriver.Chrome()

try:
    driver.get("https://portal.web100.com.ua/reporting/create-report")
    time.sleep(3)

    screenshot_path = "SS_test.png"
    driver.save_screenshot(screenshot_path)

    print(f"Збережено: {screenshot_path}")
    
finally:
    time.sleep(4)
    driver.quit()