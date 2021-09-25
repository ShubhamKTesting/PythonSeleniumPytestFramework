from selenium.webdriver.common.by import By


class CheckoutPage():
    def __init__(self, driver):
        self.driver = driver

    cards = (By.CSS_SELECTOR, ".card.h-100")
    cardFooter = (By.CLASS_NAME, "nav-link.btn.btn-primary")
    cardName = (By.XPATH, "div/h4/a")
    cardFooterButton = (By.XPATH, "div[@class='card-footer']/button")

    def getCards(self):
        return self.driver.find_elements(*CheckoutPage.cards)

    def getCardFooter(self):
        return self.driver.find_element(*CheckoutPage.cardFooter)

    def getCardName(self, mob):
        return mob.find_element(*CheckoutPage.cardName)

    def getCardFooterButton(self, mob):
        return mob.find_element(*CheckoutPage.cardFooterButton)
