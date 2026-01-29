# import time
#
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
#
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)
# driver.get("https://uk.wikipedia.org/")
#
#
# url = driver.current_url
# print(url)
#
# current_title = driver.title
# print(current_title)
#
# assert current_title == "Вікіпедія", "That`s wrong title!"
# assert url.startswith("https://uk.wikipedia.org/wiki/"),"That`s wrong URL!"
#
# time.sleep(10)




# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)
# driver.get("https://demo.opencart.com/")
# search_field = driver.find_element(By.XPATH, '//*[@id="search"]')
# search_field.send_keys("MacBook")
# submit_button = driver.find_element(By.CLASS_NAME,"btn btn-light btn-lg")
# submit_button.click()

# //*[@id="search"]/button


# firstname_field = driver.find_element(By.ID, "firstname")
# firstname_field.send_keys("Nikita")
# Last_name_filed = driver.find_element(By.ID,"lastname")
# Last_name_filed.send_keys("Tsyruk")
# username_field = driver.find_element(By.ID,"userName")
# username_field.send_keys("GUUTS")
# password_field = driver.find_element(By.ID,"password")
# password_field.send_keys("24061556Nik")
#
# submit_button = driver.find_element(By.ID,"register")
# submit_button.click()


import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

try:

    user_field = driver.find_element(By.XPATH, '//div[contains(@class,"form_group")]//input[@id="user-name"]')
    user_field.clear()
    user_field.send_keys("standard_user")
    print("User_name has written")
    password_field = driver.find_element(By.XPATH, '//input[@id="password"]')
    password_field.clear()
    password_field.send_keys("secret_sauce")
    print("Password has written")
    login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
    print("Login button has clicked")
    login_button.click()

    time.sleep(3)

    print("Успешный вход. Начинаем скупать всё...")

    buttons = driver.find_elements(By.XPATH, "//button[contains(@class,'btn_inventory')]")
    print(f"Найдено товаров: {len(buttons)}")

    for button in buttons:
        add_to = button.find_elements(By.XPATH, "//button[contains(@class,'btn btn_primary btn_small btn_inventory ')] ")
        button.click()
        print("Товар добавлен!")









    # Backpack_prod = driver.find_element(By.XPATH,"//button[contains(@id,'add-to-cart-sauce-labs-backpack')]")
    # Backpack_prod.click()
    # print("Backpack has been added to cart")
    #
    # bike_light = driver.find_element(By.XPATH,"//button[contains(@id,'add-to-cart-sauce-labs-bike-light')]")
    # bike_light.click()
    # print("Bike light has been added to cart")
    #
    #
    # bin_trash = driver.find_element(By.XPATH,"//span[contains(@class,'shopping_cart_badge')]")
    # bin_trash.click()
    # print(driver.current_url)
    #
    # checkout_button = driver.find_element(By.XPATH,"//button[contains(@id, 'checkout')]")
    # checkout_button.click()
    # print("Checkout button has clicked",driver.current_url)
    #
    # checkout_name_field = driver.find_element(By.XPATH,"//input[@id='first-name']")
    # checkout_name_field.send_keys("Nikita")
    #
    # checkout_last_name_field = driver.find_element(By.XPATH,"//input[@id='last-name']")
    # checkout_last_name_field.send_keys("Guts")
    #
    # zip_postal_code = driver.find_element(By.XPATH,"//input[@id='postal-code']")
    # zip_postal_code.send_keys("020097")
    #
    # continue_button = driver.find_element(By.XPATH,'//input[contains(@id,"continue")]')
    # continue_button.click()
    # print("Continue button has clicked",driver.current_url)
    #
    # total_price = driver.find_element(By.XPATH, "//div[@class ='summary_total_label']")
    # print("Total price:",total_price.text)
    #
    # finish_button = driver.find_element(By.XPATH, '//button[contains(@id,"finish")]')
    # finish_button.click()
    # print("Finish button has clicked",driver.current_url)
    #
    # complete_order = driver.find_element(By.XPATH, "//h2[contains(@data-test,'complete-header')]")
    #
    # if complete_order.text == "Thank you for your order!":
    #     print("Thank you for your order!")
    # else:
    #     print("Sorry, your order is invalid!")



    time.sleep(3)

except Exception as e:
    print(f"Ошибка! Проверь правильность ID. Текст ошибки: {e}")

finally:
    driver.quit()