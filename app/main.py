import asyncio
from utils.constants import CSV_HEADERS
from utils.csv import extract_rncs_from_csv, write_row
from utils.automation import look_up_rnc, extract_required_data, open_look_up_page
from classes.browser_navigation import BrowserNavigation


async def main():
    rnc_list = extract_rncs_from_csv("data/rn.csv")

    rnc = "1-32-42125-6"

    page, browser = await open_look_up_page()
    await look_up_rnc(rnc, page)
    extracted_data = await extract_required_data(rnc, page)

    print(extracted_data)
    write_row(extracted_data, CSV_HEADERS)

    await browser.close()

print("Starting...")
asyncio.get_event_loop().run_until_complete(main())
print("Done ✅")
