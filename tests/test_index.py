import playwright.sync_api as pw

from pages.IndexPage import IndexPageClass

def test_index(playwright: pw.Playwright):
    browser = playwright.chromium.launch(headless = False)
    context = browser.new_context()
    page = context.new_page()
    context.tracing.start(screenshots=True, snapshots=True)

    indexPage = IndexPageClass(page)

    indexPage.visit()
    indexPage.clickLoginButton()
    pw.expect(page).not_to_have_url("https://www.latamairlines.com/co/es")

    context.tracing.stop(path = "test_login_trace.zip")

    browser.close()

