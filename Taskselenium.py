import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
wait = WebDriverWait(driver, 10)

driver.get("https://brain.com.ua/")

try:

    xpath_search = "//div[contains(@class, 'header-bottom')]//input[@type='search']"
    search_field = wait.until(EC.visibility_of_element_located((By.XPATH, xpath_search)))

    search_field.click()
    search_field.clear()
    search_field.send_keys("Apple iPhone 15 128GB Black")


    time.sleep(2)

    xpath_button = "//input[contains(@class, 'search-button-first-form')]"
    search_button = wait.until(EC.presence_of_element_located((By.XPATH, xpath_button)))


    driver.execute_script("arguments[0].click();", search_button)

    print("Клик выполнен успешно через JS!")

    first_phone = driver.find_elements(By.XPATH, "//div[contains(@class,'qsr-products-list')]//a[contains(@class,'qsr-item')]")
    find_phone = driver.find_element(By.XPATH,"//a[contains(@href, 'iPhone_15_128GB_Black')]")
    find_phone.click()




    time.sleep(5)

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    driver.quit()