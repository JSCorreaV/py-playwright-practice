from datetime import date, timedelta

def clickLoginButton(page):
    page.locator("#header__profile__lnk-sign-in").click()

def clickFlightOptionTabButton(page):
    page.get_by_test_id("id-tab-flight-tab").click()

def selectTripType(page, tripType):
    page.locator("[aria-owns=lstSearchBoxTripType]").click()
    page.get_by_role("button", name = tripType).click()

def selectCabinType(page, cabinType):
    page.locator("[aria-owns=lstSearchBoxCabinType]").click()
    page.get_by_role("button", name = cabinType).click()

def selectAmountOfPassengers(page, passengers):
    page.locator("[aria-owns=lstSearchBoxPassenger]").click()
    for adults in range(passengers["adults"]):
        page.locator("[data-test=add-passenger-body-adult-section-plus-button]").click()
    for children in range(passengers["children"]):
        page.locator("[data-test=add-passenger-body-children-section-plus-button]").click()
    for infant in range(passengers["infant"]):
        page.locator("[data-test=add-passenger-body-infant-section-plus-button]").click()

def selectFlightType(page, tripType, cabinType, passengers, LatamPass = 0):
    selectTripType(page, tripType)
    selectCabinType(page, cabinType)
    selectAmountOfPassengers(page, passengers)
    if LatamPass:
        page.get_by_test_id("get-redemption-checkbox").click()

def selectOrigin(page, origin):
    page.get_by_placeholder("Origen").click()
    page.get_by_placeholder("Origen").fill(origin)
    page.get_by_placeholder("Destino").click()
    page.get_by_placeholder("Origen").click()
    page.get_by_role("option", name = origin).click()

def selectDestination(page, destination):
    page.get_by_placeholder("Destino").fill(destination)
    page.get_by_role("option", name = destination).click()

def goToDate(page, objectiveDate):
    actualDate = date.today()
    [futureYear, futureMonth, futureDay] = objectiveDate
    futureDate = date(futureYear, futureMonth, futureDay)
    futureDays = (futureDate - actualDate).days
    futureMonths = (actualDate + timedelta(days = futureDays)).month
    for x in range(futureMonths):
        page.locator('[aria-label="Avanza al mes de"]').click()

def selectDates(page, dates, tripType):
    departureDate = dates["departure"]["dateUnformated"]

    page.locator("#departureDate").click()
    goToDate(page, departureDate)
    page.locator('[aria-label="' + dates["departure"]["label"]+ '"]').click()
    if tripType == "Ida y Vuelta":
        arrivalDate = dates["arrival"]["dateUnformated"]
        goToDate(page, arrivalDate)
        page.locator('[aria-label="Seleccionado como fecha de ida. ' + dates["departure"]["label"] + '"]').click()
        page.locator('[aria-label="Seleccionado como fecha vuelta. ' + dates["arrival"]["label"] + '"]').click()

def clickSearchButton(page):
    page.locator("#btnSearchCTA").click()

def visit(page, url="https://www.latamairlines.com/co/es"):
    page.goto(url)
    page.wait_for_load_state()
