import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    global davinder
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        davinder = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
    elif browser_name == "firefox":
        davinder = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    elif browser_name == "IE":
        print("IE driver")

    davinder.get("https://davinder19.github.io/BMI-Calculator/")  # get method help you hit the URL on browser
    davinder.maximize_window()  # maxmize method maximaize your window
    request.cls.davinder = davinder
    yield
    # davinder.close()


