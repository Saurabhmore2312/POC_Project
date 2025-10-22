from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn


class AddToCartPage:
    def __init__(self):
        self.macbook = "//h1[contains(text(),'Shopping Cart')]/..//a[text()='MacBook']"
        self.iphone = "//h1[contains(text(),'Shopping Cart')]/..//a[text()='iPhone']"
        self.btn_checkout = "//a[text()='Checkout']"
        self.remove_iphone = "//a[text()='iPhone']//..//..//button[@data-original-title='Remove']"
        self.remove_macbook = "//a[text()='MacBook']//..//..//button[@data-original-title='Remove']"
        self.cart_is_empty = "//h1[text()='Shopping Cart']/following-sibling::p[text()='Your shopping cart is empty!']"


    def _get_selib(self):
        return BuiltIn().get_library_instance('SeleniumLibrary')

    @keyword
    def click_checkout(self):
        self._get_selib().click_element(self.btn_checkout)

    @keyword
    def remove_iphone_from_cart(self):
        self._get_selib().click_element(self.remove_iphone)

    @keyword
    def remove_macbook_from_cart(self):
        self._get_selib().click_element(self.remove_macbook)

    @keyword
    def iphone_is_visible_in_cart(self):
        status = BuiltIn().run_keyword_and_return_status("Page Should Contain Element", self.iphone)
        if status:
            BuiltIn().log("Iphone is added to Cart", "INFO")
        else:
            BuiltIn().log("Iphone is not added to Cart", "WARN")
        return status

    @keyword
    def macbook_is_visible_in_cart(self):
        status = BuiltIn().run_keyword_and_return_status("Page Should Contain Element", self.macbook)
        if status:
            BuiltIn().log("Macbook is added to Cart", "INFO")
        else:
            BuiltIn().log("Macbook is not added to Cart", "WARN")
        return status

    @keyword
    def check_if_cart_is_empty(self):
        status = BuiltIn().run_keyword_and_return_status("Page Should Contain Element", self.cart_is_empty)
        if status:
            BuiltIn().log("Cart is empty", "INFO")
        else:
            BuiltIn().log("Cart is not empty", "WARN")
        return status

