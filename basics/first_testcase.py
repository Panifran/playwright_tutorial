# Primero instalamos playwright desde file -> settings
# Después desde el terminal (env) ejecutamos playwright install, vuelve a instalar
# los exploradores en /home/javier/.cache/ms-playwright
# para abrir Playwright inspector, desde el terminal ejecutar -> playwright codegen https://www.oddsportal.com/
# traceviewer -> debug con pantallazos -> abir zip con comando playwright show-trace trace.zip
# 'password': 'c21bd681'

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()

    # Start tracing before creating / navigating a page.
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

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

    # Stop tracing and export it into a zip archive.
    context.tracing.stop(path="trace.zip")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

