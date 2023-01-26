# 'password': 'c21bd681'

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    bet365_cl1FT = -1
    bet365_clXFT = -1
    bet365_cl2FT = -1
    pinn_cl1FT = -1
    pinn_clXFT = -1
    pinn_cl2FT = -1
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()

    # Start tracing before creating / navigating a page.
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    page.goto("https://www.oddsportal.com/soccer/argentina/liga-profesional/defensa-y-justicia-huracan-CpDH4ZdO/")

    filas = page.locator("xpath=//div[@class='flex text-xs max-sm:h-[60px] h-9 border-b']").all()
    rows = page.locator("xpath=//div[@class='flex text-xs max-sm:h-[60px] h-9 border-b']").all_inner_texts()
    #rows = page.locator('xpath=//*[@id="app"]/div/div[1]/div/main/div[2]/div[5]/div[1]/div/div[2]').text_content()
    for row in rows:
        if "bet365" in row:
            new_row = row.replace('BONUS', '').replace('\n'," ")
            new_rows = new_row.split(" ")
            odds = [x for x in new_rows if x]
            bet365_cl1FT = odds[1]
            bet365_clXFT = odds[2]
            bet365_cl2FT = odds[3]

        if "Pinnacle" in row:
            new_row = row.replace('BONUS', '').replace('\n'," ")
            new_rows = new_row.split(" ")
            odds = [x for x in new_rows if x]
            pinn_cl1FT = odds[1]
            pinn_clXFT = odds[2]
            pinn_cl2FT = odds[3]


    # Stop tracing and export it into a zip archive.
    context.tracing.stop(path="trace.zip")

    # ---------------------
    context.close()
    browser.close()

    print(f"bet365_cl1FT: {bet365_cl1FT}")
    print(f"bet365_clXFT: {bet365_clXFT}")
    print(f"bet365_cl2FT: {bet365_cl2FT}")
    print(f"pinn_cl1FT: {pinn_cl1FT}")
    print(f"pinn_clXFT: {pinn_clXFT}")
    print(f"pinn_cl2FT: {pinn_cl2FT}")




with sync_playwright() as playwright:
    run(playwright)

