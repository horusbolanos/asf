from appium import webdriver
from os import path

CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, 'TheApp.apk')
APPIUM = 'http://localhost:4723'

CAPS = {
    'platformName': 'Android',
    'deviceName': 'Android Emulator',
    'automationName': 'UiAutomator2',
    'app': APP,
}

driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)

app = path.join(CUR_DIR, 'ApiDemos.apk' )
app_id = 'io.appium.android.apis'
try:
    driver.remove_app(app_id)
    driver.install_app(app)
    driver.activate_app(app_id)
    driver.terminate_app(app_id)
finally:
   driver.quit()