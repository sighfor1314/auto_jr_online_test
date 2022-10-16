import os
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import configparser  # for using .ini file
import platform


class Actions:
    def __init__(self):
        # 開啟設定檔 config.ini
        self.driver = self.setupEnvironment()

    def setupEnvironment(self):
        tries = 3
        for i in range(tries):
            try:
                # 開啟設定檔 config.ini
                ini_file_name = "config.ini"
                self.config = self.getConfig(ini_file_name)
                desired_caps = {}
                desired_caps['platformName'] = self.config['ENVIRONMENT']['platform_name']  # setup platformName
                desired_caps['platformVersion'] = self.config['ENVIRONMENT'][
                    'platform_version']  # setup platformVersion
                desired_caps['appPackage'] = self.config['ENVIRONMENT']['app_package']  # setup appPackage
                desired_caps['appActivity'] = self.config['ENVIRONMENT']['app_activity']  # setup appActivity
                desired_caps['automationName'] = self.config['ENVIRONMENT']['automation_name']
                desired_caps['noReset'] = bool(self.config['ENVIRONMENT']['no_reset'])
                return webdriver.Remote(self.config['ENVIRONMENT']['url'], desired_caps)
            except KeyError as e:
                if i < tries - 1:  # i is zero indexed
                    continue
                else:
                    raise
            break

    def getConfig(self, ini_file_name):
        configuration = configparser.ConfigParser()
        configuration.optionxform = str
        configuration.read(ini_file_name)
        return configuration

    def pressEnter(self):
        self.driver.press_keycode(66)

    def executeScreenshot(self, file_name):
        if not os.path.isdir("./test_result"):
            os.mkdir("./test_result")
        time.sleep(3)
        self.driver.save_screenshot("./test_result/" + file_name + ".png")

    # 移動游標並點擊 Item
    def clickElement(self, xpath):
        # 等待 xpath 出現（這裡假設 xpath 正確）
        WebDriverWait(self.driver, 300).until(lambda driver: self.driver.find_element(By.XPATH, value=xpath))
        self.driver.find_element(By.XPATH, value=xpath).click()

    def getElementCount(self, xpath):
        elements = self.driver.find_elements(By.XPATH, xpath)
        return len(elements)

    # 定位xpath輸入content
    def inputXpath(self, xpath, content):
        WebDriverWait(self.driver, 300).until(lambda driver: self.driver.find_element(By.XPATH, value=xpath))
        self.driver.find_element(By.XPATH, value=xpath).send_keys(content)

    # 定位id 輸入content
    def inputID(self, id, content):
        WebDriverWait(self.driver, 300).until(lambda driver: self.driver.find_element(By.ID, value=id))
        self.driver.find_element(By.ID, value=id).send_keys(content)

    # 清除input
    def clearInput(self, xpath):
        sleep(0.1)
        # 取得 input 當前內容，若有 value 則清空
        while self.getAttribute(xpath, "value") != "":
            if (platform.system() == "Darwin"):  # mac
                self.driver.find_element(By.XPATH, value=xpath).send_keys(Keys.COMMAND, "a")
            else:
                self.driver.find_element(By.XPATH, value=xpath).send_keys(Keys.CONTROL, "a")
            sleep(0.2)
            self.driver.find_element(By.XPATH, value=xpath).send_keys(Keys.BACK_SPACE)
        sleep(1)

    # 等待按鈕可以按
    def waitUntilButtonEnable(self, xpath):
        WebDriverWait(self.driver, 300).until(
            EC.element_to_be_clickable((By.XPATH, xpath)))

    # 等待 Item 出現
    def waitUntilAppear(self, xpath):
        WebDriverWait(self.driver, 300).until(
            EC.presence_of_element_located((By.XPATH, xpath)))

    # 判斷是否存在
    def isExist(self, xpath):
        try:
            self.driver.find_element(By.XPATH, value=xpath)
            '''
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, xpath)))
            '''
            return True
        except:
            return False
        # 等待 Item 出現，並判斷是否存在

    def scrollTo(self, startX, endX, startY, endY):
        deviceSize = self.driver.get_window_size()
        screenWidth = deviceSize['width']
        screenHeight = deviceSize['height']
        startx = screenWidth / startX
        endx = screenWidth / endX
        starty = screenHeight / startY
        endy = screenHeight / endY

        actions = TouchAction(self.driver)
        actions.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()

    def quit(self):
        self.driver.quit()
