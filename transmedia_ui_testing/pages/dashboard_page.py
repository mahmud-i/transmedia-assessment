from playwright.sync_api import Page
import allure



class DashboardPage:

    def __init__(self, page: Page):
        self.page = page



    @allure.step("Navigated to dashboard page")

    def navigate_to_dashboard(self, url):
        try:
            response = self.page.goto(url)                                              # navigate to url
            if response.status == 200:                                                  # Check if the response status code is 200
                return True
            else:
                return False

        except Exception as e:
            return False




    @allure.step("Create a new Board")

    def create_new_board(self, board_name):
        try:
            self.page.locator("div.create-board").click()                               # click on create board
            self.page.locator("input.new-board-input").fill(board_name)                 # enter board name
            self.page.locator("button[data-cy='new-board-create']").click()             # click on create
            self.page.wait_for_timeout(3000)                                            # wait for 3 seconds

            return True

        except Exception as e:
            return False