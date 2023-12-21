def getHomeButton(page):
    return page.get_by_test_id("home-link-button")

def getUserTextField(page):
    return page.get_by_test_id("form-input--alias-textfield-input")

def getContinueButton(page):
    return page.get_by_test_id("primary-button-button")

def getCreateAccountButton(page):
    return page.get_by_test_id("secondary-button-button")

def getRecoveryAccessButton(page):
    return page.locator("#link--register")

def typeUser(page, user):
    getUserTextField(page).fill(user)

def typePassword(page, password):
    page.get_by_test_id("form-input--password-textfield-input").fill(password)

def clickContinueButton(page):
    getContinueButton(page).click()

def typeUserAndPassword(page, user, password):
    typeUser(page, user)
    clickContinueButton(page)
    typePassword(page, password)
    clickContinueButton(page)

def visit(page, url = "https://www.latamairlines.com/co/es/login"):
    page.goto(url)
    page.wait_for_load_state()