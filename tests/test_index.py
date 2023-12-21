import playwright.sync_api as pw

import pages.IndexPage as indexPage

def test_index(page: pw.Page):

    indexPage.visit(page)
    indexPage.clickLoginButton(page)
    pw.expect(page).not_to_have_url("https://www.latamairlines.com/co/es")
    #browser.close()

    #playwright.stop()

