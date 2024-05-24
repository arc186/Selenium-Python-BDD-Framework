from features.page.BasePage import BasePage
from features.page.loginpage import LoginPage
from features.page.searchpage import SearchPage
class Homepage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)  # to calling constructor of base class

    my_account_xpath = "//span[normalize-space()='My Account']"
    login_option_link_text = "Login"
    search_name = "search"
    search_click_xpath = "//button[@class='btn btn-default btn-lg']"

    def click_on_my_account(self):
        self.click_to_element("my_account_xpath", self.my_account_xpath)

    def click_on_login_option(self):
        self.click_to_element("login_option_link_text", self.login_option_link_text)
        # self.driver.find_element(By.LINK_TEXT, self.login_option_Link_text).click()
        return LoginPage(self.driver)

    def check_home_page_title(self, expected_title):
        return self.verification_of_title_page(expected_title)

    def search_product_field(self, product):
        self.entering_text_value_into_element("search_name", self.search_name, product)

    def search_click(self):
        self.click_to_element("search_click_xpath", self.search_click_xpath)
        # self.driver.find_element(By.XPATH, self.search_click_xpath).click()
        return SearchPage(self.driver)
