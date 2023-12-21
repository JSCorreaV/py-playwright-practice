#pytest tests/test_login.py --headed
import json
import playwright.sync_api as pw

import pages.BasePage as basePage
import pages.IndexPage as indexPage
import pages.LoginPage as loginPage

jsonFileLogin= open('tests/fixtures/loginData.json')
loginData = json.load(jsonFileLogin)

def test_login_default_view(page: pw.Page):
    loginPage.visit(page)

    pw.expect(loginPage.getHomeButton(page)).to_be_visible()

    pw.expect(loginPage.getUserTextField(page)).to_be_visible()
    pw.expect(loginPage.getUserTextField(page)).to_be_empty()

    pw.expect(loginPage.getContinueButton(page)).to_be_enabled()
    pw.expect(loginPage.getContinueButton(page)).to_contain_text(loginData["textButtons"]["continue"])
    
    pw.expect(loginPage.getCreateAccountButton(page)).to_be_enabled()
    pw.expect(loginPage.getCreateAccountButton(page)).to_contain_text(loginData["textButtons"]["createAccount"])

    pw.expect(loginPage.getRecoveryAccessButton(page)).to_be_enabled()

def test_login(page: pw.Page):
    indexPage.visit(page)
    indexPage.clickLoginButton(page)
    pw.expect(page).not_to_have_url("https://www.latamairlines.com/co/es")
    loginPage.typeUserAndPassword(page, loginData["user"], loginData["password"])