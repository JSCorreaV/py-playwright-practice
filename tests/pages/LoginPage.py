from pages.BasePage import BasePageClass

class LoginPageClass(BasePageClass):

    url = "https://www.latamairlines.com/co/es/login"

    def __init__(self, page):
        super()
        self.page = page
    
    def visit(self):
        super().visit(self.url)

    def getHomeButton(self):
        return self.page.get_by_test_id("home-link-button")

    def getUserTextField(self):
        return self.page.get_by_test_id("form-input--alias-textfield-input")

    def getContinueButton(self):
        return self.page.get_by_test_id("primary-button-button")

    def getCreateAccountButton(self):
        return self.page.get_by_test_id("secondary-button-button")

    def getRecoveryAccessButton(self):
        return self.page.locator("#link--register")

    def typeUser(self, user):
        self.getUserTextField().fill(user)

    def typePassword(self, password):
        self.page.get_by_test_id("form-input--password-textfield-input").fill(password)

    def clickContinueButton(self):
        self.page.getContinueButton().click()

    def typeUserAndPassword(self, user, password):
        self.typeUser(user)
        self.clickContinueButton()
        self.typePassword(password)
        self.clickContinueButton()