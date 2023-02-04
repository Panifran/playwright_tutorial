from playwright.sync_api import Playwright, sync_playwright, expect
import re


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=200)
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

    url_leagues = ['https://www.oddsportal.com/matches/my-matches/20230203/']
    for url_league in url_leagues:
        # CONSEGUIR LOS LINKS DE TODOS LOS PARTIDOS
        # page.goto(url_league)
        # url_games = page.eval_on_selector_all(
        #     "xpath=//div[@class='flex hover:bg-[#f9e9cc] group border-l border-r border-black-borders']//a[contains(@href,'')]",
        #     "elements => elements.map(element => element.href)")
        # print(url_games)
        page.goto(url_league)
        games_detail = []
        game_rows = page.locator("xpath=//div[@class='flex hover:bg-[#f9e9cc] group border-l border-r border-black-borders']").all()
        for row in game_rows:
            url_game = row.locator(".next-m\:pt-0").get_attribute('href')
            status = row.locator('.justify-center.min-w-\[60px\]').text_content()
            games_detail.append([url_game, status])

        for game in games_detail:
            url = f"https://www.oddsportal.com{game[0]}"
            status = game[1]
            print(url)

            if status == "postp." or status == "award.":

                page.goto(url)
                page.reload()
                teams = page.locator(".h-7").all_text_contents()
                home_team = teams[-2]
                away_team = teams[-1]
                start_time = page.locator(".bg-event-start-time+ div").text_content()
                day = re.findall("[0-9]{2}", start_time)[0]
                year = re.findall("[0-9]{4}", start_time)[0]
                time = re.findall("\d\d:\d\d", start_time)[0]
                month_text = re.findall("[0-9]{2}\W([A-Z][a-z]+)", start_time)[0]
                month = ""

                if month_text == 'Jan':
                    month = '01'
                elif month_text == 'Feb':
                    month = '02'
                elif month_text == 'Mar':
                    month = '03'
                elif month_text == 'Apr':
                    month = '04'
                elif month_text == 'May':
                    month = '05'
                elif month_text == 'Jun':
                    month = '06'
                elif month_text == 'Jul':
                    month = '07'
                elif month_text == 'Aug':
                    month = '08'
                elif month_text == 'Sep':
                    month = '09'
                elif month_text == 'Oct':
                    month = '10'
                elif month_text == 'Nov':
                    month = '11'
                elif month_text == 'Dec':
                    month = '12'

                match_date = f"{year}-{month}-{day} {time}:00"


                home_team_score = -1
                away_team_score = -1
                ft_home_team_goals = -1
                ht_home_team_goals = -1
                ft_away_team_goals = -1
                ht_away_team_goals = -1

                print(f"status: {status}")
                print(f"ft_home_team_goals: {ft_home_team_goals}")
                print(f"ft_away_team_goals: {ft_away_team_goals}")
                print(f"ht_home_team_goals: {ht_home_team_goals}")
                print(f"ht_away_team_goals: {ht_away_team_goals}")

                #2023-01-31 22:00:00
                print(f"home_team: {home_team}")
                print(f"away_team: {away_team}")
                print(f"start_time: {match_date}")
                print(f"status: {status}")

            else:

                page.goto(url)
                page.reload()
                teams = page.locator(".h-7").all_text_contents()
                home_team = teams[-2]
                away_team = teams[-1]
                start_time = page.locator(".bg-event-start-time+ div").text_content()
                day = re.findall("[0-9]{2}", start_time)[0]
                year = re.findall("[0-9]{4}", start_time)[0]
                time = re.findall("\d\d:\d\d", start_time)[0]
                month_text = re.findall("[0-9]{2}\W([A-Z][a-z]+)", start_time)[0]
                month = ""

                if month_text == 'Jan':
                    month = '01'
                elif month_text == 'Feb':
                    month = '02'
                elif month_text == 'Mar':
                    month = '03'
                elif month_text == 'Apr':
                    month = '04'
                elif month_text == 'May':
                    month = '05'
                elif month_text == 'Jun':
                    month = '06'
                elif month_text == 'Jul':
                    month = '07'
                elif month_text == 'Aug':
                    month = '08'
                elif month_text == 'Sep':
                    month = '09'
                elif month_text == 'Oct':
                    month = '10'
                elif month_text == 'Nov':
                    month = '11'
                elif month_text == 'Dec':
                    month = '12'

                match_date = f"{year}-{month}-{day} {time}:00"

                result = page.locator('.max-sm\:\!mb-5 .flex-wrap').text_content()
                status = re.findall("[A-za-z]+", result)[0]
                home_team_score = re.findall("([0-9]?[0-9])+:", result)
                away_team_score = re.findall(":([0-9]?[0-9])", result)
                ft_home_team_goals = home_team_score[0]
                ht_home_team_goals = home_team_score[1]
                ft_away_team_goals = away_team_score[0]
                ht_away_team_goals = away_team_score[1]

                print(f"status: {status}")
                print(f"ft_home_team_goals: {ft_home_team_goals}")
                print(f"ft_away_team_goals: {ft_away_team_goals}")
                print(f"ht_home_team_goals: {ht_home_team_goals}")
                print(f"ht_away_team_goals: {ht_away_team_goals}")

                # 2023-01-31 22:00:00
                print(f"home_team: {home_team}")
                print(f"away_team: {away_team}")
                print(f"start_time: {match_date}")
                print(f"status: {status}")



with sync_playwright() as playwright:
    run(playwright)
