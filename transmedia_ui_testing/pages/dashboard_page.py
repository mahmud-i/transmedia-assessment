from playwright.sync_api import Page
import allure

class DashboardPage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Navigated to dashboard page")
    def navigate_to_dashboard(self, url):
        try:
            response = self.page.goto(url)
            if response.status == 200:
                return True
            else:
                return False

        except Exception as e:
            return False


    @allure.step("Create a new Board")
    def create_new_board(self, board_name):
        try:
            self.page.locator("div.create-board").click()
            self.page.locator("input.new-board-input").fill(board_name)
            self.page.locator("button[data-cy='new-board-create']").click()
            self.page.wait_for_timeout(3000)
            return True
        except Exception as e:
            return False