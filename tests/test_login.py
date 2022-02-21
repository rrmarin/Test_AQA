from pages.page import LoginPage


class TestLogin:
    def test_login_successfully(self, browser, wait, base_url):
        page = LoginPage(browser, wait, base_url)
        page.open()
        products_page = page.login(user_name="standard_user", password="secret_sauce")
        login_page = products_page.logout()
        assert login_page.login_button_is_clickable()

    def test_invalid_credentials(self, browser, wait, base_url):
        page = LoginPage(browser, wait, base_url)
        page.open()
        page.login(user_name="locked_out_user", password="secret_sauce")
        assert page.get_login_error_message() == "Epic sadface: Sorry, this user has been locked out."
