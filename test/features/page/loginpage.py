from features.page.BasePage import BasePage
from features.page.accountpage import AccountPage
class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    email_address_id = "input-email"
    password_id = "input-password"
    login_button_xpath = "//input[@value='Login']"
    warning_message_xpath = "//div[@id='account-login']/div[1]"

    def enter_email_address(self, email_address):
        self.entering_text_value_into_element("email_address_id", self.email_address_id, email_address)

    def enter_password(self, pwd):
        self.entering_text_value_into_element("password_id", self.password_id, pwd)

    def login_button(self):
        self.click_to_element("login_button_xpath", self.login_button_xpath)
        return AccountPage(self.driver)

    def warning_message(self, expected_warning_text):
        return self.returning_warning_message("warning_message_xpath", self.warning_message_xpath, expected_warning_text)

