from playwright.sync_api import Page
import allure



class BoardPage:

    def __init__(self, page: Page):
        self.page = page



    @allure.step("Verify created Board")

    def verify_board_created(self,expected_board_name):
        try:
            sibling_locator = self.page.locator("input[name='board-title']")                                    # sibling locator to get the board name
            board_name_locator = sibling_locator.locator("xpath=../div[1]")                                     # locator to get the board name
            board_name = board_name_locator.text_content()                                                      # getting the board name
            if board_name == expected_board_name:                                                               # checking the board name with expected board name
                return True
            else:
                return False

        except Exception as e:
            return False




    @allure.step("Create new List")

    def create_new_list(self, list_name):
        try:
            add_list_modal_locator = self.page.locator('div[data-cy="create-list"]')                            # locator to get the add list modal
            if add_list_modal_locator.count() > 0:                                                              # checking if the add list modal is present
                add_list_modal_locator.click()                                                                  # clicking the add list modal if present

            list_name_input_locator = self.page.locator('input[data-cy="add-list-input"]')                      # locator to get the list name input
            list_name_input_locator.fill(list_name)                                                             # filling the list name
            list_name_input_locator.locator("xpath=../div[1]/button").click()                                   # clicking the create list button
            self.page.wait_for_timeout(3000)                                                                    # waiting for 3 seconds

            return True

        except Exception as e:
            return False




    def verify_list(self, expected_list_item):
        try:
            list_name_locator = self.page.locator("input[data-cy='list-name']")                                 # locator to get the list name
            found_list_name = []

            for item_locator in list_name_locator.all():                                                        # iterating through the list name locators
                list_name = item_locator.input_value()                                                          # getting the list name
                found_list_name.append(list_name)                                                               # adding the list name to the list

            is_subset = set(expected_list_item).issubset(set(found_list_name))                                  # checking if the expected list item is a subset of the found list name
            return is_subset

        except Exception as e:
            return False




    @allure.step("Verify created List")

    def verify_list_created(self,expected_list_item):
        return self.verify_list(expected_list_item)                                                             # calling the verify_list method




    @allure.step("Delete List")

    def delete_list(self, list_name):
        try:
            list_name_locator = self.page.locator("input[data-cy='list-name']")                                 # locator to get the list name

            for item_locator in list_name_locator.all():                                                        # iterating through the list name locators
                item_name = item_locator.input_value()                                                          # getting the list name
                if item_name == list_name:                                                                      # checking if the list name is equal to the expected list name
                    item_locator.locator("xpath=../button").click()                                             # clicking the list three dots button
                    delete_locator = item_locator.locator('xpath=../div[1]//div[@data-cy="delete-list"]')       # locator to get the delete list CTA
                    delete_locator.click()                                                                      # clicking the delete list CTA
                    self.page.wait_for_timeout(3000)                                                            # waiting for 3 seconds
                    return True                                                                                 # returning True and breaking the loop

            return False                                                                                        # returning False if the list name is not found

        except Exception as e:
            return False




    @allure.step("Verify List Deleted")

    def verify_list_deleted(self, list_name):
        return not self.verify_list(list_name)                                                                  # calling the verify_list method and returning the opposite to check if the list is deleted