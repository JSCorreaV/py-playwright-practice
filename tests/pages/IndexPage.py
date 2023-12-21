from datetime import date, timedelta
from pages.BasePage import BasePageClass

class IndexPageClass(BasePageClass):
    
    url = "https://www.latamairlines.com/co/es"

    def __init__(self, page):
        super()
        self.page = page
    
    def visit(self):
        super().visit(self.url)

    def clickLoginButton(self):
        self.page.locator("#header__profile__lnk-sign-in").click()

    def clickFlightOptionTabButton(self):
        self.page.get_by_test_id("id-tab-flight-tab").click()

    def selectTripType(self, tripType):
        self.page.locator("[aria-owns=lstSearchBoxTripType]").click()
        self.page.get_by_role("button", name = tripType).click()

    def selectCabinType(self, cabinType):
        self.page.locator("[aria-owns=lstSearchBoxCabinType]").click()
        self.page.get_by_role("button", name = cabinType).click()

    def selectAmountOfPassengers(self, passengers):
        self.page.locator("[aria-owns=lstSearchBoxPassenger]").click()
        for adults in range(passengers["adults"]):
            self.page.locator("[data-test=add-passenger-body-adult-section-plus-button]").click()
        for children in range(passengers["children"]):
            self.page.locator("[data-test=add-passenger-body-children-section-plus-button]").click()
        for infant in range(passengers["infant"]):
            self.page.locator("[data-test=add-passenger-body-infant-section-plus-button]").click()

    def selectFlightType(self, tripType, cabinType, passengers, LatamPass = 0):
        self.selectTripType(tripType)
        self.selectCabinType(cabinType)
        self.selectAmountOfPassengers(passengers)
        if LatamPass:
            self.page.get_by_test_id("get-redemption-checkbox").click()

    def selectOrigin(self, origin):
        self.page.get_by_placeholder("Origen").click()
        self.page.get_by_placeholder("Origen").fill(origin)
        self.page.get_by_placeholder("Destino").click()
        self.page.get_by_placeholder("Origen").click()
        self.page.get_by_role("option", name = origin).click()

    def selectDestination(self, destination):
        self.page.get_by_placeholder("Destino").fill(destination)
        self.page.get_by_role("option", name = destination).click()

    def goToDate(self, objectiveDate):
        actualDate = date.today()
        [futureYear, futureMonth, futureDay] = objectiveDate
        futureDate = date(futureYear, futureMonth, futureDay)
        futureDays = (futureDate - actualDate).days
        futureMonths = (actualDate + timedelta(days = futureDays)).month
        for x in range(futureMonths):
            self.page.locator('[aria-label="Avanza al mes de"]').click()

    def selectDates(self, dates, tripType):
        departureDate = dates["departure"]["dateUnformated"]

        self.page.locator("#departureDate").click()
        self.goToDate(departureDate)
        self.page.locator('[aria-label="' + dates["departure"]["label"]+ '"]').click()
        if tripType == "Ida y Vuelta":
            arrivalDate = dates["arrival"]["dateUnformated"]
            self.goToDate(arrivalDate)
            self.page.locator('[aria-label="Seleccionado como fecha de ida. ' + dates["departure"]["label"] + '"]').click()
            self.page.locator('[aria-label="Seleccionado como fecha vuelta. ' + dates["arrival"]["label"] + '"]').click()

    def clickSearchButton(self):
        self.page.locator("#btnSearchCTA").click()