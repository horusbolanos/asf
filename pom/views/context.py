import pytest
from appium import webdriver
from os import path
from views.home_view import HomeView

CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, '..', 'mobile', 'TheApp.app.zip')
APPIUM = 'http://localhost:4723'

@pytest.fixture
def driver():    
    CAPS = {
        'platformName': 'IOS',
        'platformVersion': '13.6',
        'deviceName': 'iphone 11',
        'automationName': 'XCUITest',
        'app': APP,
    }
    driver = webdriver.Remote(
        command_executor=APPIUM,
        desired_capabilities=CAPS
    )
    yield driver
    driver.quit()
    

@pytest.fixture
def home(driver):
    return HomeView(driver)
