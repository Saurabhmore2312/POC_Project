from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn


class HomePage:
    def __init__(self):
        self.link_Register = "//a[text()='Register']"
        self.link_Login = "//ul//a[text()='Login']"
        self.link_Cart = "//a[@title='Shopping Cart']"
        self.link_Account = "//span[text()='My Account']"
        self.link_logout = "//ul//a[text()='Logout']"
        self.add_to_cart_macbook = "//a[text()='MacBook']//..//../following-sibling::div//span[text()='Add to Cart']"
        self.add_to_cart_iphone = "//a[text()='iPhone']//..//../following-sibling::div//span[text()='Add to Cart']"
        self.logo = "//div[@id='logo']/a/img"
        self.add_to_wishlist_macbook = "//a[text()='MacBook']//..//../following-sibling::div//button[@data-original-title='Add to Wish List']"
        self.add_to_wishlist_iphone = "//a[text()='iPhone']//..//../following-sibling::div//button[@data-original-title='Add to Wish List']"
        self.link_Wishlist = "id=wishlist-total"
        self.quick_access_cart = "id=cart-total"
        self.iphone_quick_access = "//div[@id='cart']//table//a[text()='iPhone']"
        self.macbook_quick_access = "//div[@id='cart']//table//a[text()='MacBook']"
        self.quick_access_cart_is_empty = "//p[text()='Your shopping cart is empty!']"
        self.remove_iphone_quick_access = "//div[@id='cart']//table//a[text()='iPhone']//../following-sibling::td/button[@title='Remove']"
        self.remove_macbook_quick_access = "//div[@id='cart']//table//a[text()='MacBook']//../following-sibling::td/button[@title='Remove']"

    def _get_selib(self):
        return BuiltIn().get_library_instance('SeleniumLibrary')

    @keyword
    def click_account(self):
        self._get_selib().click_element(self.link_Account)

    @keyword
    def click_register(self):
        self._get_selib().click_element(self.link_Register)

    @keyword
    def click_login(self):
        self._get_selib().click_element(self.link_Login)

    @keyword
    def click_wishlist(self):
        self._get_selib().click_element(self.link_Wishlist)

    @keyword
    def click_cart(self):
        self._get_selib().click_element(self.link_Cart)

    @keyword
    def add_macbook_to_cart(self):
        self._get_selib().click_element(self.add_to_cart_macbook)

    @keyword
    def add_iphone_to_cart(self):
        self._get_selib().click_element(self.add_to_cart_iphone)

    @keyword
    def add_macbook_to_wishlist(self):
        self._get_selib().click_element(self.add_to_wishlist_macbook)

    @keyword
    def add_iphone_to_wishlist(self):
        self._get_selib().click_element(self.add_to_wishlist_iphone)

    @keyword
    def click_logo(self):
        self._get_selib().click_element(self.logo)

    @keyword
    def click_quick_access_cart(self):
        self._get_selib().click_element(self.quick_access_cart)

    @keyword
    def remove_iphone_from_quick_access(self):
        self._get_selib().click_element(self.remove_iphone_quick_access)

    @keyword
    def remove_macbook_from_quick_access(self):
        self._get_selib().click_element(self.remove_macbook_quick_access)

    @keyword
    def iphone_in_quick_access_tab(self):
        status = BuiltIn().run_keyword_and_return_status("Page Should Contain Element", self.iphone_quick_access)
        if status:
            BuiltIn().log("Iphone is visible in Quick Access Cart", "INFO")
        else:
            BuiltIn().log("Iphone is not visible in Quick Access Cart", "WARN")
        return status

    @keyword
    def macbook_in_quick_access_tab(self):
        status = BuiltIn().run_keyword_and_return_status("Page Should Contain Element", self.macbook_quick_access)
        if status:
            BuiltIn().log("Macbook is visible in Quick Access Cart", "INFO")
        else:
            BuiltIn().log("Macbook is not visible in Quick Access Cart", "WARN")
        return status

    @keyword
    def logout_is_visible(self):
        status = BuiltIn().run_keyword_and_return_status("Page Should Contain Element", self.link_logout)
        if status:
            BuiltIn().log("Logout link is visible", "INFO")
        else:
            BuiltIn().log("Logout link is not visible", "WARN")
        return status

    @keyword
    def check_if_quick_access_cart_is_empty(self):
        status = BuiltIn().run_keyword_and_return_status("Page Should Contain Element", self.quick_access_cart_is_empty)
        if status:
            BuiltIn().log("Quick Access Cart is empty", "INFO")
        else:
            BuiltIn().log("Quick Access Cart is not empty", "WARN")
        return status
