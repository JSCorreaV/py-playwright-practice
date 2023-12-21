#pytest tests/test_login.py --headed
import json
import playwright.sync_api as pw

import pages.IndexPage as indexPage
from pages.LoginPage import LoginPageClass

jsonFileLogin= open('tests/fixtures/loginData.json')
loginData = json.load(jsonFileLogin)

def test_login_default_view(page: pw.Page):
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

# def test_login(page: pw.Page):
#     indexPage.visit(page)
#     indexPage.clickLoginButton(page)
#     pw.expect(page).not_to_have_url("https://www.latamairlines.com/co/es")
#     loginPage.typeUserAndPassword(page, loginData["user"], loginData["password"])