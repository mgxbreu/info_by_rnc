import unidecode
from utils.constants import DGII_URL, TRADE_NAME_VALUE, PAYMENT_REGIME_VALUE, STATUS_VALUE, ECONOMIC_ACTIVITY_VALUE, RNC_INPUT, SEARCH_BUTTON
from classes.browser_navigation import BrowserNavigation


async def open_look_up_page():
    browser_navigation = BrowserNavigation()
    await browser_navigation.setup_browser()
    await browser_navigation.open_new_page()
    await browser_navigation.goto(DGII_URL)
    page = browser_navigation.page
    browser = browser_navigation.browser
    return page, browser


async def look_up_rnc(rnc, page):
    entry_box = await page.querySelector(RNC_INPUT)
    await entry_box.type(rnc)
    await page.click(SEARCH_BUTTON)
    await page.waitForSelector("#ctl00_cphMain_dvDatosContribuyentes > tbody > tr:nth-child(3) > td:nth-child(2)")


async def extract_required_data(rnc, page):
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

    return extracted_data
