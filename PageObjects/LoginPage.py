from robot.api.deco import keyword

from robot.libraries.BuiltIn import BuiltIn


class LoginPage:

    def __init__(self):
        self.input_Email = "id=input-email"
        self.input_Password = "id=input-password"
        self.btn_Login = "//input[@type='submit']"
        self.btn_home = "//ul[@class='breadcrumb']/li[1]/a"

    def _getselib__(self):
        return BuiltIn().get_library_instance('SeleniumLibrary')

    @keyword
    def enter_login_email(self, email):
        self._getselib__().input_text(self.input_Email, email)

    @keyword
    def enter_login_password(self, password):
        self._getselib__().input_text(self.input_Password, password)

    @keyword
    def click_login_button(self):
        self._getselib__().click_element(self.btn_Login)

    @keyword
    def click_home_button(self):
        self._getselib__().click_element(self.btn_home)
