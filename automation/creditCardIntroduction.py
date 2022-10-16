class CreditCardIntroduction:
    def __init__(self, driver):
        self.driver = driver

    # scroll cards list util "停發卡"
    def scrollCardsList(self):
        # self.driver.moveTo("//android.view.View[@content-desc='百貨購物']/android.widget.TextView")
        while (not self.driver.isExist("//android.view.View[@content-desc='停發卡']/android.widget.TextView")):
            self.driver.scrollTo(1.75, 9, 2.1, 2.1)

    # click "停發卡" and go to "停發卡"
    def clickDiscontinuedCard(self):
        self.driver.clickElement("//android.view.View[@content-desc='停發卡']/android.widget.TextView")

    # can't locate amdroid elements,so only scroll 6 times.
    def getDiscontinuedCardList(self):
        count = 1
        for i in range(1, 7):
            self.driver.executeScreenshot("discontinued_card_" + str(i))
            self.driver.scrollTo(1.2, 10, 2.1, 2.1)
            count += 1
        self.driver.executeScreenshot("discontinued_card_" + str(count))
        print("停發卡總數為 " + str(count))
        return count
