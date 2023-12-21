#pytest tests/test_login.py
#playwright show-trace test_search_a_flight_trace.zip

import json
import re
import playwright.sync_api as pw
import pages.IndexPage as indexPage
import pages.FlightsOfferedPage as flightsOfferedPage

jsonFileLoginFlight= open('tests/fixtures/flightData.json')
flightData = json.load(jsonFileLoginFlight)

def test_search_a_flight(playwright: pw.Playwright):
    browser = playwright.chromium.launch(headless = False)
    context = browser.new_context()
    page = context.new_page()
    context.tracing.start(screenshots=True, snapshots=True)
    indexPage.visit(page)

    indexPage.clickFlightOptionTabButton(page)
    indexPage.selectFlightType(page, flightData["tripType"], flightData["cabinType"], flightData["passengers"])
    indexPage.selectOrigin(page, flightData["origin"])
    indexPage.selectDestination(page, flightData["destination"])

    indexPage.selectDates(page, flightData["date"], flightData["tripType"])

    with context.expect_page() as newPageOpened:
        indexPage.clickSearchButton(page)
        flightsOfferedPageOpened = newPageOpened.value
        flightsOfferedPage.getDateSelected(flightsOfferedPageOpened).to_have_class(re.compile(r"selected"))
        flightsOfferedPage.clickFirstflightOffered(flightsOfferedPageOpened)
        flightsOfferedPage.clickBundleType(flightsOfferedPageOpened, flightData["bundleType"])
        flightsOfferedPage.goToSelectSeats(flightsOfferedPageOpened)
    
    context.tracing.stop(path = "test_search_a_flight_trace.zip")