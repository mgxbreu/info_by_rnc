from pyppeteer import launch, errors


class BrowserNavigation():
    def __init__(self):
        self.url = None
        self.browser = None
        self.page = None

    async def setup_browser(self):
        self.browser = await launch({"headless": False, "args": ["--start-maximized", "--no-sandbox"]})

    async def open_new_page(self):
        self.page = await self.browser.newPage()

    async def goto(self, url):
        while True:
            try:
                await self.page.goto(url)
                break
            except errors.TimeoutError as e:
                continue

    async def close_browser(self):
        await self.browser.close()
