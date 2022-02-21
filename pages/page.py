from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, wait, base_url):
        self.browser = browser
        self.wait = wait
        self.base_url = base_url

    def open(self):
        self.browser.get(self.base_url)


class LoginPage(BasePage):
    user_name_locator = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button_locator = (By.CSS_SELECTOR, "#login-button")
    error_box = (By.CSS_SELECTOR, ".error-message-container")

    def login(self, user_name, password):
        user_name_input = self.browser.find_element(*self.user_name_locator)
        user_name_input.send_keys(user_name)
        password_input = self.browser.find_element(*self.password)
        password_input.send_keys(password)
        login_button = self.browser.find_element(*self.login_button_locator)
        login_button.click()
        return ProductsPage(self.browser, self.wait, self.base_url)

    def login_button_is_clickable(self):
        return EC.element_to_be_clickable(self.login_button_locator)

    def get_login_error_message(self):
        return self.browser.find_element(*self.error_box).text.strip()


class ProductsPage(BasePage):
    product_title_locator = (By.CLASS_NAME, "title")
    hamburger_button_locator = (By.ID, "react-burger-menu-btn")
    log_out_button_locator = (By.CSS_SELECTOR, "#logout_sidebar_link")

    def open_side_bar_menu(self):
        hamburger_button = self.wait.until(
            EC.element_to_be_clickable(
                self.hamburger_button_locator
            )
        )
        hamburger_button.click()

    def logout(self):
        self.open_side_bar_menu()
        log_out_button = self.wait.until(
            EC.element_to_be_clickable(
                self.log_out_button_locator
            )
        )
        log_out_button.click()
        return LoginPage(self.browser, self.wait, self.base_url)
