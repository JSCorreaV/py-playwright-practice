
class FlightOfferedClass:

    def __init__(self, page):
        self.page = page

    def getDateSelected(self):
        return self.page.locator("#date-carousel-item-2")

    def clickFirstflightOffered(self):
        self.page.locator('[aria-label="Ver opciones de tarifas de este vuelo"]').nth(0).click()

    def clickBundleType(self, bundleType):
        self.page.get_by_test_id("bundle-detail-" + bundleType + "-flight-select").click()

    def goToSelectSeats(self):
        self.page.get_by_text("Ir a asientos").click()