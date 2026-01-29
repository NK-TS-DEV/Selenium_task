import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from tabulate import tabulate


class BrainSeleniumParser:
    def __init__(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.data = {}


    def open_site(self):
         self.driver.get("https://brain.com.ua/")

    def search_product(self, product_name):
        print(f"Looking for a product {product_name}")
        search = self.driver.find_element(By.XPATH,"//div[contains(@class, 'header-bottom')]//input[@type='search']")
        search.click()
        search.send_keys(product_name)

        time.sleep(3)

        search_button = self.driver.find_element(By.XPATH,"//input[contains(@class, 'search-button-first-form')]")
        self.driver.execute_script("arguments[0].click();",search_button)

        time.sleep(3)


    def go_to_first_product(self):
        self.driver.find_elements(By.XPATH,"//div[contains(@class,'qsr-products-list')]//a[contains(@class,'qsr-item')]")
        find_first_product = self.driver.find_element(By.XPATH,"//a[contains(@href, 'iPhone_15_128GB_Black')]")
        find_first_product.click()
        time.sleep(3)

    def parse_main_info(self):
        self.data["Title"] = self.driver.find_element(By.XPATH,"//h1[@class='desktop-only-title']").text
        codes = self.driver.find_elements(By.XPATH, "//div[@id='product_code']//span[contains(@class, 'br-pr-code-val')]")

        self.data["Code"] = "Code not found"

        for c in codes:
            text_value = c.get_attribute("textContent").strip()

            if text_value:
                self.data["Code"] = text_value
                break


    def parse_price(self):
        price =self.driver.find_element(By.XPATH,"//div[contains(@class, 'main-price-block')]//div[contains(@class, 'br-pr-op')]//div[contains(@class, 'price-wrapper')]/span")
        self.data["Price"] = price.text

        new_price = self.driver.find_element(By.XPATH,"//div[contains(@class, 'main-price-block')]//div[contains(@class, 'br-pr-np')]//div[contains(@class, 'price-wrapper')]//span[contains(@class,'red-price')]")

        if new_price:
            self.data["Sale_Price"] = new_price.text
        else:
            print("The sale already done")
            self.data["Sale_Price"] = None


    def parse_display_specs(self):
        try:
            display = self.driver.find_element(By.XPATH,"//span[contains(text(), 'Діагональ екрану')]/following-sibling::span//a")
            self.data["Display"] = display.get_attribute("textContent").strip()

            resolution = self.driver.find_element(By.XPATH,"//span[contains(text(), 'Роздільна здатність екрану')]/following-sibling::span//a")
            self.data["Resolution"] = resolution.get_attribute("textContent").strip()

        except Exception as e:
            print(f"Mistake connect with parsing {e}")
            self.data["Display"] = "-"
            self.data["Resolution"] = "-"

    def parse_detailed_specs(self):
        memory =self.driver.find_element(By.XPATH,"//span[contains(text(), 'Вбудована пам')]/following-sibling::span")
        self.data["Memory"] = memory.get_attribute("textContent").strip()

        color = self.driver.find_element(By.XPATH,'//span[contains(text(), "Колір")]/following-sibling::span')
        self.data["Color"] = color.get_attribute("textContent").strip()

        Manufacturer = self.driver.find_element(By.XPATH,"//span[normalize-space(text())='Виробник']/following-sibling::span")
        self.data["Manufacturer"] = Manufacturer.get_attribute("textContent").strip()

    def parse_images(self):
        try:
            list_photo = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'series-product-pictures')]//img")
            photo_url = []

            for img in list_photo:
                url = img.get_attribute("data-observe-src")
                if not url:
                    url = img.get_attribute("src")
                if url:
                    photo_url.append(url)

            self.data["Image"] = photo_url
        except Exception as e:
            print(f"Mistake connect with parsing {e}")
            self.data["Image"] = []


    def parse_reviews(self):
        self.data["Reviews"]= "0"
        try:
            review_links = self.driver.find_elements(By.XPATH, "//a[contains(@href, 'reviews-list')]")
            if len(review_links) > 0:
                raw_text = review_links[0].get_attribute("textContent")

                digit_string = "".join(filter(str.isdigit, raw_text))
                if digit_string:
                    self.data["Reviews"] = digit_string
        except Exception as e:
            print(f"Mistake connect with parsing {e}")



    def parse_all_characteristics(self):
        characteristics = {}

        all_row = self.driver.find_elements(By.XPATH,"//div[contains(@class, 'br-w306 br-characteristics-wrapper')]//div[./span]")

        for row in all_row:
            tag_span = row.find_elements(By.TAG_NAME, "span")

            if len(tag_span) >= 2:
                raw_keys = tag_span[0].get_attribute("textContent").strip()
                raw_values = tag_span[1].get_attribute("textContent").strip()

                keys =  " ".join(raw_keys.split())
                values = " ".join(raw_values.split())

                if keys and values:
                    characteristics[keys] = values
            self.data["Characteristics"] = characteristics


    def run_parser(self):
        self.parse_main_info()
        self.parse_price()
        self.parse_images()
        self.parse_display_specs()
        self.parse_detailed_specs()
        self.parse_reviews()
        self.parse_all_characteristics()

        return self.data



if __name__ == "__main__":
    bot = BrainSeleniumParser()

    try:
        bot.open_site()
        bot.search_product("Apple iPhone 15 128GB Black")
        bot.go_to_first_product()


        product_data = bot.run_parser()

        table = []
        for key, value in product_data.items():
            table.append([key, value])

        print("\nResult:")
        print(tabulate(table, headers=["Field", "Value"], tablefmt="grid"))


    except Exception as e:
        print(f"Mistake: {e}")
    finally:
        time.sleep(5)


if __name__ == "__main__":
    bot = BrainSeleniumParser()

    try:
        bot.open_site()
        bot.search_product("Apple iPhone 15 128GB Black")
        bot.go_to_first_product()


        product_data = bot.run_parser()

        table = []
        for key, value in product_data.items():
            table.append([key, value])

        print("\nResult:")
        print(tabulate(table, headers=["Field", "Value"], tablefmt="grid"))


    except Exception as e:
        print(f"Mistake: {e}")
    finally:
        time.sleep(5)