from playwright.sync_api import Page, expect, sync_playwright
import pytest


def test_main(p):
    browser = p.chromium.launch(headless=False, slow_mo=700)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://latamairlines.com/co/es")

    assert page.title() == 'Cotiza Vuelos, Paquetes, Hoteles y Carros | LATAM en Colombia'

    page.locator("input#txtInputOrigin_field").type('Medellín')
    page.locator("button#btnItemAutoComplete_0").click()
    page.locator("input#txtInputDestination_field").type('Amsterdam')
    page.locator("button#btnItemAutoComplete_0").click()
    page.locator("input#departureDate").click()

    page.locator("[aria-label*=', 7 de enero de 2024']").click()
    page.locator("[aria-label*=', 29 de febrero de 2024']").click()

    with context.expect_page() as new_opened_page:
        page.locator("button#btnSearchCTA").click()

    offered_flights_page = new_opened_page.value

    offered_flights_page.locator("[class^=cardFlightstyle__CardExpander]").first.click()
    offered_flights_page.locator("[data-testid=bundle-detail-0-flight-select]").click()

    page.wait_for_timeout(2000)
    offered_flights_page.locator("[class^=cardFlightstyle__CardExpander]").first.click()
    offered_flights_page.locator("[data-testid=bundle-detail-0-flight-select]").click()

    offered_flights_page.locator("[data-testid=button9--button]").click()

    page.wait_for_timeout(10000)
    offered_flights_page.locator("[data-seat-number=3A]").click()

    print(offered_flights_page.locator("[data-testid=card-list]").text_content())
    expect(offered_flights_page.locator("[data-testid=card-list]")).to_contain_text('3A')
    expect(offered_flights_page.locator("[data-testid=card-list]")).to_contain_text('Adulto 1')
    expect(offered_flights_page.locator("[data-testid=card-list]")).to_contain_text('Más adelante - Ventana')

    page.pause()
    context.close()
    browser.close()


with sync_playwright() as p:
    test_main(p)
