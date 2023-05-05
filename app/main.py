import asyncio
import unidecode
from pyppeteer import launch
import csv
from utils.constants import DGII_URL


async def main():
    browser = await launch({"headless": False, "args": ["--start-maximized", "--no-sandbox"]})
    page = await browser.newPage()

    rnc_list = []
    print("hi")

    with open("data/rn.csv", 'r') as csvfile:
        datareader = csv.reader(csvfile)
        header = next(datareader)
        if header != None:
            for row in datareader:
                print(row)
                rnc_list.append(row)
    while True:
        try:
            await page.goto(DGII_URL)
            break
        except pyppeteer.errors.TimeoutError as e:
            continue

    rnc = "1-32-42125-6"
    print(rnc)
    entry_box = await page.querySelector(
        "#ctl00_cphMain_txtRNCCedula"
    )

    await entry_box.type(rnc)

    await page.click('#ctl00_cphMain_btnBuscarPorRNC')

    await page.waitForSelector('#ctl00_cphMain_dvDatosContribuyentes > tbody > tr:nth-child(3) > td:nth-child(2)')

    nombre_comercial = await page.evaluate('''() => {
        const data = document.querySelector('#ctl00_cphMain_dvDatosContribuyentes > tbody > tr:nth-child(3) > td:nth-child(2)').innerText;
        return data;
    }''')

    regimen_pago = await page.evaluate('''() => {
        const data = document.querySelector('#ctl00_cphMain_dvDatosContribuyentes > tbody > tr:nth-child(5) > td:nth-child(2)').innerText;
        return data;
    }''')

    estado = await page.evaluate('''() => {
        const data = document.querySelector('#ctl00_cphMain_dvDatosContribuyentes > tbody > tr:nth-child(6) > td:nth-child(2)').innerText;
        return data;
    }''')

    actividad_economica = await page.evaluate('''() => {
        const data = document.querySelector('#ctl00_cphMain_dvDatosContribuyentes > tbody > tr:nth-child(7) > td:nth-child(2)').innerText;
        return data;
    }''')
    # print(nombre_comercial, regimen_pago, estado, actividad_economica)

    actividad_economica = unidecode.unidecode(actividad_economica)

    # headers = "rnc,nombre_comercial,regimen_pago,estado,actividad_economica \n"

    # csvfile = open("rnc.csv", "w")

    print(rnc_list)

    # csvfile.write(headers)
    # csvfile.write(rnc + "," + nombre_comercial + ", " + regimen_pago + ", " + estado + ", " + actividad_economica + "\n")

    #     Rnc
    # 1-32-42125-6
    # 1-31-75529-1

    await page.screenshot({"path": "python.png"})

    await browser.close()

print("Starting...")
asyncio.get_event_loop().run_until_complete(main())
print("Screenshot has been taken")
