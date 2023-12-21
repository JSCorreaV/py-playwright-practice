#pytest tests/test_login.py
#playwright show-trace test_search_a_flight_trace.zip

import json
import re
import playwright.sync_api as pw
from pages.IndexPage import IndexPageClass
from pages.FlightsOfferedPage import FlightOfferedClass

jsonFileLoginFlight= open('tests/fixtures/flightData.json')
flightData = json.load(jsonFileLoginFlight)

def test_search_a_flight(playwright: pw.Playwright):
    browser = playwright.chromium.launch(headless = False)
    context = browser.new_context()
    page = context.new_page()
    context.tracing.start(screenshots=True, snapshots=True)
    indexPage = IndexPageClass(page)

    indexPage.visit()

    indexPage.clickFlightOptionTabButton()
    indexPage.selectFlightType(flightData["tripType"], flightData["cabinType"], flightData["passengers"])
    indexPage.selectOrigin(flightData["origin"])
    indexPage.selectDestination(flightData["destination"])

    indexPage.selectDates(flightData["date"], flightData["tripType"])

    with context.expect_page() as newPageOpened:
        indexPage.clickSearchButton()
        flightsOfferedPageOpened = newPageOpened.value
        flightsOfferedPage = FlightOfferedClass(flightsOfferedPageOpened)
        
        pw.expect(flightsOfferedPage.getDateSelected()).to_have_class(re.compile(r"selected"))
        flightsOfferedPage.clickFirstflightOffered()
        flightsOfferedPage.clickBundleType(flightData["bundleType"])
        flightsOfferedPage.goToSelectSeats()
    
    context.tracing.stop(path = "test_search_a_flight_trace.zip")