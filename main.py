import asyncio
import subprocess
import ipdb
from playwright.async_api import async_playwright

from Cast import Cast
from Cast.player import Player


async def main():
    #    ipdb.set_trace()
    total = 50
    i = 0
    user = Cast.user()
    user.can_get_data()
    user.open_rival_scores()
    tester = Cast.tester()
    await tester.configure_browser(False)
    while i < total:
        await tester.launch_browser()
        #        page = await tester.page
        await tester.go_to_mz()
        #        await page.goto('https://www.managerzone.com/?changesport=soccer')
        if i == 0:
            manager = await tester.is_on_mz()
            if i == 0:
                await manager.login.allow_cookies
            await manager.login.complete_user_name("arcano19")
            await manager.login.complete_pass("9c7ca79c7ca7")
            await manager.login.ingresar()
            await manager.home_page
        #     await page.get_by_role("link", name="Club", exact=True).hover()
        #     await page.get_by_role("link", name="Plantilla Resumida").click()
        #     await page.wait_for_load_state('load')
        #     await page.wait_for_selector('#squad_summary')
        #     tabla = await page.query_selector('#squad_summary')
        #     all_rows = await tabla.query_selector_all("tr")
        #     all_rows.pop(0)
        #     players_total = []
        #     for py in all_rows:
        #         registro = await py.query_selector_all('xpath=child::*')
        #         player = Player(await registro[0].inner_text(), await registro[1].inner_text(),
        #                         await registro[2].inner_text(),
        #                         await registro[3].inner_text(), await registro[4].inner_text(),
        #                         await registro[5].inner_text())
        #         players_total.append(player)
        #
        #     user.calculate_my_team_score(players_total)
        #
        # await page.locator("#top_item_matches").get_by_role("link", name="Partidos").hover()
        # await page.locator("#sub_page_nav_fixtures").get_by_role("link", name="Próximos Partidos").click()
        # await page.wait_for_selector('.group')
        # await page.wait_for_load_state('load')
        # list_match = await page.query_selector_all('span.short-name')
        # item = list_match[i]
        # team_name = await item.inner_text()
        # if team_name != "BTM":
        #     await item.click()
        #     await page.wait_for_load_state('load')
        #     await page.get_by_role("cell", name="Jugadores").get_by_text("Jugadores").click()
        #     await page.get_by_role("link", name="Plantilla Resumida").click()
        #     await page.wait_for_load_state('load')
        #     await page.wait_for_selector('#squad_summary')
        #     tabla = await page.query_selector('#squad_summary')
        #     all_rows = await tabla.query_selector_all("tr")
        #     all_rows.pop(0)
        #     players_total = []
        #     for p in all_rows:
        #         registro = await p.query_selector_all('xpath=child::*')
        #         player = Player(await registro[0].inner_text(), await registro[1].inner_text(),
        #                         await registro[2].inner_text(),
        #                         await registro[3].inner_text(), await registro[4].inner_text(),
        #                         await registro[5].inner_text())
        #         players_total.append(player)
        #
        #     user.calculate_team_score(players_total, team_name)
        #     i = i + 1
        # else:
        #     i = i + 1
        #
        # await page.close()

    await tester.close_all()


asyncio.run(main())

processes = []
