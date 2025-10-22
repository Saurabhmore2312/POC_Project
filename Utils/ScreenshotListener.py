import os

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from datetime import datetime

@keyword("Capture Screenshot On Failure")
def capture_screenshot_on_failure():
    """Capture screenshot if the Robot test case failed."""

    # Check if the test failed
    test_status = BuiltIn().get_variable_value("${TEST STATUS}")
    if test_status == "FAIL":
        # Get the SeleniumLibrary instance
        selib = BuiltIn().get_library_instance('SeleniumLibrary')

        # Ensure Screenshots folder exists
        screenshots_dir = os.path.join(os.getcwd(), "Screenshots")
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)

        # Build filename: TestName + timestamp
        test_name = BuiltIn().get_variable_value("${TEST NAME}").replace(" ", "_")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(screenshots_dir, f"{test_name}_{timestamp}.png")

        # Capture screenshot
        selib.capture_page_screenshot(file_path)
        BuiltIn().log(f"Screenshot saved: {file_path}", level="INFO")
