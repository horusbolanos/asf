import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from os import path


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


def test_echo_box(driver):
    wait = WebDriverWait(driver, 10)

    wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'messageInput'))).send_keys('Hello')
    driver.find_element(MobileBy.ACCESSIBILITY_ID, 'messageSaveBtn'). click()
    saved_text = driver.find_element(MobileBy.ACCESSIBILITY_ID, 'savedMessage').text
    assert saved_text == 'Hello'
    driver.back()
    wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'Echo Box'))).click()    
    saved_text = wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'savedMessage'))).text
    assert saved_text == 'Hello'
