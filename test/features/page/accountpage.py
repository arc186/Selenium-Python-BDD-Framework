from features.page.BasePage import BasePage
class AccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    logged_confirmation_link_text = "Edit your account information"

    def display_status(self):
        return self.display_product_status("logged_confirmation_link_text", self.logged_confirmation_link_text)
