def getDateSelected(page):
    pw.expect(page.locator("#date-carousel-item-2"))

def clickFirstflightOffered(page):
    page.locator('[aria-label="Ver opciones de tarifas de este vuelo"]').nth(0).click()

def clickBundleType(page, bundleType):
    page.get_by_test_id("bundle-detail-" + bundleType + "-flight-select").click()

def goToSelectSeats(page)
    page.get_by_text("Ir a asientos").click()