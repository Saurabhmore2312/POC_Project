from robot.api.deco import keyword

from robot.libraries.BuiltIn import BuiltIn


class AccountRegisterPage:
    def __init__(self):
        self.input_FirstName = "id=input-firstname"
        self.input_LastName = "id=input-lastname"
        self.input_Email = "id=input-email"
        self.input_Password = "id=input-password"
        self.input_cfm_Password = "id=input-confirm"
        self.btn_register = "id=register-button"
        self.btn_Continue = "//input[@type='submit']"
        self.input_Phone = "id=input-telephone"
        self.rdbtnAgree = "//input[@name='agree']"
        self.cfm_msg = "//h1"


    def _get_selib(self):
        return BuiltIn().get_library_instance('SeleniumLibrary')

    @keyword
    def enter_phone_number(self, input_Phone):
        self._get_selib().input_text(self.input_Phone, input_Phone)

    @keyword
    def enter_firstname(self, first_name):
        self._get_selib().input_text(self.input_FirstName, first_name)

    @keyword
    def enter_lastname(self, last_name):
        self._get_selib().input_text(self.input_LastName, last_name)

    @keyword
    def enter_email(self, email):
        self._get_selib().input_text(self.input_Email, email)

    @keyword
    def enter_password(self, password):
        self._get_selib().input_text(self.input_Password, password)

    @keyword
    def enter_cfm_password(self, cfm_password):
        self._get_selib().input_text(self.input_cfm_Password, cfm_password)

    @keyword
    def click_agree(self):
        self._get_selib().click_element(self.rdbtnAgree)

    @keyword
    def click_continue(self):
        self._get_selib().click_element(self.btn_Continue)

    @keyword
    def get_confirmation_message(self):
        try:
            return self._get_selib().get_text(self.cfm_msg)
        except Exception as e:
            return str(e)
