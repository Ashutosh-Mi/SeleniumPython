# import pytest
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     yield driver
#     driver.quit()

# import pytest
# from selenium import webdriver
# import time

# def pytest_addoption(parser):
#     parser.addoption(
#         "--headed",
#         action="store_true",
#         default=False,
#         help="Run in headed mode"
#     )

# @pytest.fixture
# def driver(request):
#     driver = webdriver.Chrome()
#     driver.maximize_window()

#     yield driver

#     if request.config.getoption("--headed"):
#         print("DEBUG MODE: keeping browser open for 5 seconds")
#         time.sleep(5)

#     driver.quit()
#############################################################
    
# from drivers.driver_factory import get_driver
# import pytest

# @pytest.fixture
# def driver():
#     driver = get_driver()
#     yield driver
#     driver.quit()

    #######################################################################

import pytest
import os
from datetime import datetime
from drivers.driver_factory import get_driver

# FIXTURE 
@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


# HOOK (new for screenshots)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Only take screenshot on test failure
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"{item.name}_{timestamp}.png"

            driver.save_screenshot(f"{screenshots_dir}/{file_name}")