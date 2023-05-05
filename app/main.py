import asyncio
import unidecode
from pyppeteer import launch, errors
import csv
from utils.constants import CSV_HEADERS, DGII_URL, RNC_INPUT, TRADE_NAME_VALUE, PAYMENT_REGIME_VALUE, STATUS_VALUE, ECONOMIC_ACTIVITY_VALUE, SEARCH_BUTTON
from utils.csv import extract_rncs_from_csv, write_row
from classes.browser_navigation import BrowserNavigation


async def main():
    browser_navigation = BrowserNavigation()
    await browser_navigation.setup_browser()
    await browser_navigation.open_new_page()
    await browser_navigation.goto(DGII_URL)
    page = browser_navigation.page

    rnc_list = extract_rncs_from_csv("data/rn.csv")

    rnc = "1-32-42125-6"

    entry_box = await page.querySelector(RNC_INPUT)

    await entry_box.type(rnc)

    await page.click(SEARCH_BUTTON)

    await page.waitForSelector("#ctl00_cphMain_dvDatosContribuyentes > tbody > tr:nth-child(3) > td:nth-child(2)")

    nombre_comercial = await page.evaluate(TRADE_NAME_VALUE)

    regimen_pago = await page.evaluate(PAYMENT_REGIME_VALUE)

    estado = await page.evaluate(STATUS_VALUE)

    actividad_economica = await page.evaluate(ECONOMIC_ACTIVITY_VALUE)

    actividad_economica = unidecode.unidecode(actividad_economica)

    extracted_data = {
        "rnc": rnc,
        "nombre_comercial": nombre_comercial,
        "regimen_pago": regimen_pago,
        "estado": estado,
        "actividad_economica": actividad_economica
    }

    print(extracted_data)
    write_row(extracted_data, CSV_HEADERS)

    await browser.close()

print("Starting...")
asyncio.get_event_loop().run_until_complete(main())
print("Done ✅")
