from features.page.BasePage import BasePage
class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    valid_product_display_link_text = "HP LP3065"
    product_error_xpath = "/html[1]/body[1]/div[2]/div[1]/div[1]/p[2]"

    def display_valid_product_status(self):
        return self.display_product_status("valid_product_display_link_text", self.valid_product_display_link_text)

    def product_error_status(self, expected_error_message):
        return self.returning_error_message("product_error_xpath", self.product_error_xpath, expected_error_message)