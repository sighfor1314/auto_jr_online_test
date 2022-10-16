from utils import Actions
from homePage import HomePage
from creditCardIntroduction import CreditCardIntroduction

def main():
    driver = Actions()
    # for execute home page case
    cathaybk_home_page = HomePage(driver)
    cathaybk_home_page.setupChrome()
    cathaybk_home_page.goToWebsite()
    driver.executeScreenshot("cathaybk_home_page")
    cathaybk_home_page.clickMenu()
    cathaybk_home_page.clickProductIntroduction()
    cathaybk_home_page.clickCreditCard()
    cathaybk_home_page.getCredictCardListCount()
    driver.executeScreenshot("cathaybk_creditcard_list")
    cathaybk_home_page.clickCardsIntroduction()

    # for execute credit card page case
    cathaybk_credit_card_page = CreditCardIntroduction(driver)
    cathaybk_credit_card_page.scrollCardsList()
    cathaybk_credit_card_page.clickDiscontinuedCard()
    cathaybk_credit_card_page.getDiscontinuedCardList()

    driver.quit

if __name__ == '__main__':
    main()
