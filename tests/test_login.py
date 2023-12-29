#pytest tests/test_login.py --headed
import json
import playwright.sync_api as pw

import pages.IndexPage as indexPage
from pages.LoginPage import LoginPageClass

jsonFileLogin= open('tests/fixtures/loginData.json')
loginData = json.load(jsonFileLogin)

def test_login_default_view(playwright: pw.Playwright):
    browser = playwright.chromium.launch(headless = False)
    context = browser.new_context()
    page = context.new_page()
    context.tracing.start(screenshots=True, snapshots=True)
    loginPage = LoginPageClass(page)

    loginPage.visit()

    pw.expect(loginPage.getHomeButton()).to_be_visible()

    pw.expect(loginPage.getUserTextField()).to_be_visible()
    pw.expect(loginPage.getUserTextField()).to_be_empty()

    pw.expect(loginPage.getContinueButton()).to_be_enabled()
    pw.expect(loginPage.getContinueButton()).to_contain_text(loginData["textButtons"]["continue"])
    
    pw.expect(loginPage.getCreateAccountButton()).to_be_enabled()
    pw.expect(loginPage.getCreateAccountButton()).to_contain_text(loginData["textButtons"]["createAccount"])

    pw.expect(loginPage.getRecoveryAccessButton()).to_be_enabled()

    context.tracing.stop(path = "test_login_trace.zip")

    browser.close()

# def test_login(playwright: pw.Playwright):
#     browser = playwright.chromium.launch(headless = False)
#     context = browser.new_context()
#     page = context.new_page()
#     context.tracing.start(screenshots=True, snapshots=True)
#     loginPage = LoginPageClass(page)

#     indexPage.visit()
#     indexPage.clickLoginButton()
#     pw.expect(page).not_to_have_url("https://www.latamairlines.com/co/es")
#     loginPage.typeUserAndPassword(loginData["user"], loginData["password"])

#     context.tracing.stop(path = "test_login_trace.zip")
    
#     browser.close()