from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn


class AddToWishlistPage:
    def __init__(self):
        self.macbook = "//h2[contains(text(),'My Wish List')]/..//a[text()='MacBook']"
        self.iphone = "//h2[contains(text(),'My Wish List')]/..//a[text()='iPhone']"
        self.btn_add_macbook_to_cart = "//h2[contains(text(),'My Wish List')]/..//td/a[text()='MacBook']/../following-sibling::td//button[@data-original-title='Add to Cart']"
        self.btn_add_iphone_to_cart = "//h2[contains(text(),'My Wish List')]/..//td/a[text()='iPhone']/../following-sibling::td//button[@data-original-title='Add to Cart']"
        self.btn_continue = "//a[text()='Continue']"


    def _get_selib(self):
        return BuiltIn().get_library_instance('SeleniumLibrary')

    @keyword
    def click_continue(self):
        self._get_selib().click_element(self.btn_continue)

    @keyword
    def iphone_is_visible_in_wishlist(self):
        status = BuiltIn().run_keyword_and_return_status("Page Should Contain Element", self.iphone)
        if status:
            BuiltIn().log("Iphone is added to Cart", "INFO")
        else:
            BuiltIn().log("Iphone is not added to Cart", "WARN")
        return status

    @keyword
    def macbook_is_visible_in_wishlist(self):
        status = BuiltIn().run_keyword_and_return_status("Page Should Contain Element", self.macbook)
        if status:
            BuiltIn().log("Macbook is added to Cart", "INFO")
        else:
            BuiltIn().log("Macbook is not added to Cart", "WARN")
        return status

    @keyword
    def add_macbook_to_cart_through_wishlist(self):
        self._get_selib().click_element(self.btn_add_macbook_to_cart)

    @keyword
    def add_iphone_to_cart_through_wishlist(self):
        self._get_selib().click_element(self.btn_add_iphone_to_cart)

