from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()

    page = context.new_page()
    page.goto("https://www.oddsportal.com/")
    page.get_by_role("button", name="I Accept").click()
    page.get_by_text("Login").first.click()
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("Pani")
    page.get_by_label("Password").click()
    page.get_by_label("Password").press("Tab")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("c21bd681")
    page.get_by_role("button", name="Login").click()

    urls = ['https://www.oddsportal.com/soccer/colombia/primera-a/deportes-tolima-america-de-cali-I7ef5yRM/',
            'https://www.oddsportal.com/soccer/costa-rica/primera-division/san-carlos-herediano-2RZ73WDf/',
            'https://www.oddsportal.com/soccer/colombia/primera-a/atl-nacional-once-caldas-dbfb4etT/',
            'https://www.oddsportal.com/soccer/mexico/liga-mx/atlas-santos-laguna-0ji5VBIN/',
            'https://www.oddsportal.com/soccer/mexico/liga-mx/atlas-santos-laguna-0ji5VBIN/']

    # urls_ou25 = [
    #     'https://www.oddsportal.com/soccer/colombia/primera-a/deportes-tolima-america-de-cali-I7ef5yRM/',
    #     'https://www.oddsportal.com/soccer/costa-rica/primera-division/san-carlos-herediano-2RZ73WDf/#over-under;2',
    #     'https://www.oddsportal.com/soccer/colombia/primera-a/atl-nacional-once-caldas-dbfb4etT/#over-under;2',
    #     'https://www.oddsportal.com/soccer/mexico/liga-mx/atlas-santos-laguna-0ji5VBIN/#over-under;2',
    #     'https://www.oddsportal.com/soccer/mexico/liga-mx/atlas-santos-laguna-0ji5VBIN/#over-under;2']

    for url in urls:
        print(url)
        page.goto(url)

        rows = page.locator("xpath=//div[@class='flex text-xs max-sm:h-[60px] h-9 border-b']").all()

        for row in rows:
            bookmaker = row.locator("xpath=//div/child::a[2]").text_content()

            if bookmaker == "bet365":
                odd_cells = row.locator(
                    "xpath=div[@class='flex flex-col items-center justify-center gap-1 border-r min-w-[60px] max-sm:min-w-[55px] border-[#E0E0E0]'] | div[@class='flex flex-col items-center justify-center gap-1 border-r min-w-[60px] max-sm:min-w-[55px] bg-[#ffcf0d] border-[#E0E0E0]']").all()

                bet365_cl1FT = odd_cells[0].text_content()
                print(f"bet365_cl1FT: {bet365_cl1FT}")
                bet365_clXFT = odd_cells[1].text_content()
                print(f"bet365_clXFT: {bet365_clXFT}")
                bet365_cl2FT = odd_cells[2].text_content()
                print(f"bet365_cl2FT: {bet365_cl2FT}")

                odd_cells[0].hover()

                tooltip = page.locator(".tooltip")
                text = tooltip.inner_text().split("\n")
                bet365_op1FT = text[-1]
                print(f"bet365_op1FT: {bet365_op1FT}")

                odd_cells[1].hover()
                tooltip = page.locator(".tooltip")
                text = tooltip.inner_text().split("\n")
                bet365_opXFT = text[-1]
                print(f"bet365_opXFT: {bet365_opXFT}")

                odd_cells[2].hover()
                tooltip = page.locator(".tooltip")
                text = tooltip.inner_text().split("\n")
                bet365_op2FT = text[-1]
                print(f"bet365_op2FT: {bet365_op2FT}")

            if bookmaker == "Pinnacle":
                odd_cells = row.locator(
                    "xpath=div[@class='flex flex-col items-center justify-center gap-1 border-r min-w-[60px] max-sm:min-w-[55px] border-[#E0E0E0]'] | div[@class='flex flex-col items-center justify-center gap-1 border-r min-w-[60px] max-sm:min-w-[55px] bg-[#ffcf0d] border-[#E0E0E0]']").all()

                pinn_cl1FT = odd_cells[0].text_content()
                print(f"pinn_cl1FT: {pinn_cl1FT}")
                pinn_clXFT = odd_cells[1].text_content()
                print(f"pinn_clXFT: {pinn_clXFT}")
                pinn_cl2FT = odd_cells[2].text_content()
                print(f"pinn_cl2FT: {pinn_cl2FT}")

                odd_cells[0].hover()
                tooltip = page.locator(".tooltip")
                text = tooltip.inner_text().split("\n")
                pinn_op1FT = text[-1]
                print(f"pinn_op1FT: {pinn_op1FT}")

                odd_cells[1].hover()
                tooltip = page.locator(".tooltip")
                text = tooltip.inner_text().split("\n")
                pinn_opXFT = text[-1]
                print(f"pinn_opXFT: {pinn_opXFT}")

                odd_cells[2].hover()
                tooltip = page.locator(".tooltip")
                text = tooltip.inner_text().split("\n")
                pinn_op2FT = text[-1]
                print(f"pinn_op2FT: {pinn_op2FT}")

        url25 = f"{url}#over-under;2"
        print(url25)
        page.goto(url25)
        page.reload()
        table_containers = page.locator("//div[@class='relative flex flex-col']").all()

        for table_container in table_containers:
            if "Over/Under +2.5" in table_container.text_content():
                page.get_by_text("Over/Under +2.5").click()
                odds_250_rows = table_container.locator(
                    "xpath=div/div[@class='flex text-xs max-sm:h-[60px] h-9 border-b bg-gray-med_light border-bottom-solid']").all()
                for elem in odds_250_rows:
                    if len(elem.locator("xpath=div/a").all()) > 0:
                        bookmaker = elem.locator("xpath=div/child::a[2]").text_content()
                        if bookmaker == "bet365":
                            odd_cells = elem.locator(
                                "xpath=div[@class='flex flex-col items-center justify-center gap-1 border-r min-w-[60px] max-sm:min-w-[55px] border-black-borders'] |" +
                                "div[@class='flex flex-col items-center justify-center gap-1 border-r min-w-[60px] max-sm:min-w-[55px] border-black-borders max-sm:border-l'] |" +
                                "div[@class='flex flex-col items-center justify-center gap-1 border-r min-w-[60px] max-sm:min-w-[55px] bg-[#ffcf0d] border-black-borders'] | " +
                                "div[@class='flex flex-col items-center justify-center gap-1 border-r min-w-[60px] max-sm:min-w-[55px] bg-[#ffcf0d] border-black-borders max-sm:border-l']").all()
                            if len(odd_cells) >= 2:
                                bet365_clO25FT = odd_cells[0].text_content()
                                bet365_clU25FT = odd_cells[1].text_content()

                                odd_cells[0].hover()
                                tooltip = page.locator(".tooltip")
                                text = tooltip.inner_text().split("\n")
                                bet365_opO25FT = text[-1]

                                odd_cells[1].hover()
                                tooltip = page.locator(".tooltip")
                                text = tooltip.inner_text().split("\n")
                                bet365_opU25FT = text[-1]

                                print(f"bet365_clO25FT: {bet365_clO25FT}")
                                print(f"bet365_clU25FT: {bet365_clU25FT}")
                                print(f"bet365_opO25FT: {bet365_opO25FT}")
                                print(f"bet365_opU25FT: {bet365_opU25FT}")

                        if bookmaker == "Pinnacle":
                            odd_cells = elem.locator(
                                "xpath=div[@class='flex flex-col items-center justify-center gap-1 border-r min-w-[60px] max-sm:min-w-[55px] border-black-borders'] |" +
                                "div[@class='flex flex-col items-center justify-center gap-1 border-r min-w-[60px] max-sm:min-w-[55px] border-black-borders max-sm:border-l'] |" +
                                "div[@class='flex flex-col items-center justify-center gap-1 border-r min-w-[60px] max-sm:min-w-[55px] bg-[#ffcf0d] border-black-borders'] | " +
                                "div[@class='flex flex-col items-center justify-center gap-1 border-r min-w-[60px] max-sm:min-w-[55px] bg-[#ffcf0d] border-black-borders max-sm:border-l']").all()
                            if len(odd_cells) >= 2:
                                pinn_clO25FT = odd_cells[0].text_content()
                                pinn_clU25FT = odd_cells[1].text_content()

                                odd_cells[0].hover()
                                tooltip = page.locator(".tooltip")
                                text = tooltip.inner_text().split("\n")
                                pinn_opO25FT = text[-1]

                                odd_cells[1].hover()
                                tooltip = page.locator(".tooltip")
                                text = tooltip.inner_text().split("\n")
                                pinn_opU25FT = text[-1]

                                print(f"pinn_clO25FT: {pinn_clO25FT}")
                                print(f"pinn_clU25FT: {pinn_clU25FT}")
                                print(f"pinn_opO25FT: {pinn_opO25FT}")
                                print(f"pinn_opU25FT: {pinn_opU25FT}")
                                break


    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
