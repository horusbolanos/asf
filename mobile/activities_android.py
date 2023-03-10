import time 
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
app_act1 = '.graphics.TouchPaint'
app_act2 = '.text.Marquee'
try:
    driver.install_app(app)
    driver.start_activity(app_id, app_act1)
    time.sleep(1)
    driver.start_activity(app_id, app_act2)
    time.sleep(1)
finally:
   driver.quit()