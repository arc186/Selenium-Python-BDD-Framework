from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_to_element(self, locator_type, locator_value):
        element = self.get_element(locator_type, locator_value)
        element.click()

    def verification_of_title_page(self, expected_title):
        return self.driver.title.__eq__(expected_title)

    def returning_warning_message(self, locator_type, locator_value, expected_warning_text):
        element = self.get_element(locator_type, locator_value)
        return element.text.__contains__(expected_warning_text)

    def display_product_status(self, locator_type, locator_value):
        element = self.get_element(locator_type, locator_value)
        return element.is_displayed()

    def returning_error_message(self, locator_type, locator_value, expected_error_message):
        element = self.get_element(locator_type, locator_value)
        return element.text.__contains__(expected_error_message)

    def entering_text_value_into_element(self, locator_type, locator_value, text_value):
        element = self.get_element(locator_type, locator_value)
        element.clear()
        element.click()
        element.send_keys(text_value)

    def get_element(self, locator_type, locator_value):
        element = None
        if locator_type.endswith("_id"):
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_type.endswith("_name"):
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_type.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_type.endswith("_link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_type.endswith("_class_name"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        elif locator_type.endswith("_css"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        else:
            print(locator_type)
        return element
