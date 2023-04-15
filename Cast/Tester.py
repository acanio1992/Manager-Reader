from playwright.async_api import async_playwright

from PageObject.Page_Manager_Zone import PageManagerZone


class Tester:
    def __init__(self):
        self.page = None
        self.manager_zone = None
        self.context = None
        self.browser = None

    async def configure_browser(self,option):
        p = await async_playwright().start()
        self.browser = await p.chromium.launch(headless=option)
        self.context = await self.browser.new_context()

    async def launch_browser(self):
        self.page = await self.context.new_page()

    async def close_all(self):
        await self.context.close()
        await self.browser.close()

    async def go_to_mz(self):
        await self.page.goto('https://www.managerzone.com/?changesport=soccer')
        self.manager_zone = PageManagerZone(self.page)

    async def is_on_mz(self):
        return self.manager_zone
