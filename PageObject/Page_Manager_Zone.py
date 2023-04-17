from PageObject.login_page import LoginPage


class PageManagerZone:

    def __init__(self, page):
        self.page = page
        self.login = LoginPage(self.page)

    async def log_in_with_user(self, user):
        await self.login.allow_cookies()
        await self.login.complete_user_name(user)
        return self

    async def and_pass(self, password):
        await self.login.complete_pass(password)
        await self.login.ingresar()