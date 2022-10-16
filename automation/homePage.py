class HomePage:
    def __init__(self, driver):
        self.driver = driver

    # for first open Chrome to setup.
    def setupChrome(self):
        if self.driver.isExist("//android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.Button"):
            self.driver.clickElement("//android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.Button")
            self.driver.clickElement("// android.widget.Button[@text='No thanks']")

    # go to Cathay back website
    def goToWebsite(self):
        self.driver.inputID("com.android.chrome:id/search_box_text", "https://www.cathaybk.com.tw/cathaybk/")
        self.driver.pressEnter()
        self.driver.waitUntilAppear("//android.view.View[@content-desc='cathaybk']/android.widget.Image")

    # click Menu
    def clickMenu(self):
        self.driver.clickElement(
            '//android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]')

    # click "產品介紹"
    def clickProductIntroduction(self):
        self.driver.clickElement("//android.view.View//android.widget.TextView[@text='產品介紹']")

    # click "信用卡"
    def clickCreditCard(self):
        self.driver.clickElement("//android.view.View[1]/android.widget.TextView[@text='信用卡']")

    # culculate credit card list
    def getCredictCardListCount(self):
        self.driver.waitUntilAppear(
            "//android.widget.TextView[@text='信用卡']/../android.view.View[@resource-id='lnk_Link']")
        credict_card_count = self.driver.getElementCount(
            "//android.widget.TextView[@text='信用卡']/../android.view.View[@resource-id='lnk_Link']")
        print("信用卡列表項目數量:", credict_card_count)
        return credict_card_count

    # click "卡片介紹"
    def clickCardsIntroduction(self):
        self.driver.clickElement("//android.view.View[@content-desc='卡片介紹']")
