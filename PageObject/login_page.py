class LoginPage:

    def __init__(self, page):
        self.page = page

    async def allow_cookies(self):
        await self.page.get_by_role("link", name="Allow all cookies").click()

    async def complete_user_name(self, user):
        await self.page.get_by_role("textbox", name="Usuario").fill(user)

    async def complete_pass(self, password):
        await self.page.get_by_role("textbox", name="Contraseña").fill(password)

    async def ingresar(self):
        await self.page.get_by_role("link", name="Ingresar", exact=True).click()
