import asyncio
from playwright.async_api import async_playwright


async def test_main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://latamairlines.com/co/es")

        title = await page.title()
        assert title == 'Cotiza Vuelos, Paquetes, Hoteles y Carros | LATAM en Colombia'

        await page.locator("input#txtInputOrigin_field").type('Medellín')
        await page.locator("button#btnItemAutoComplete_0").click()
        await page.locator("input#txtInputDestination_field").type('Amsterdam')
        await page.locator("button#btnItemAutoComplete_0").click()
        await page.locator("input#departureDate").click()

        await page.locator("[aria-label*=', 7 de enero de 2024']").click()
        await page.locator("[aria-label*=', 29 de febrero de 2024']").click()

        await page.locator("button#btnSearchCTA").click()

        await browser.close()

asyncio.run(test_main())
