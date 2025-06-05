import pytest
import allure
from utils import take_screenshot
from pages.dashboard_page import DashboardPage
from pages.board_page import BoardPage




@pytest.mark.usefixtures("setup", "load_test_data")
class TestUIAssessment:


    @pytest.fixture(scope="class", autouse=True)

    def setup_class(self, request, setup, load_test_data):
        """Class-scoped fixture to initialize shared test data"""
        request.cls.context= setup                                                                      # Assign `setup` to `self.context`
        request.cls.page = setup.new_page()                                                             # Assign `setup` to `self.page`
        request.cls.test_data = load_test_data                                                          # Assign `load_test_data` to `self.test_data`






    @allure.description("TC001: Navigate to Dashboard")
    @pytest.mark.dependency(name="Navigate_dashboard")
    @pytest.mark.parametrize("environment", ["env"])
    @allure.severity(allure.severity_level.CRITICAL)


    def test_navigate_to_Dashboard(self, environment):
        try:
            page_instance = DashboardPage(self.page)                                                     # Create an instance of DashboardPage
            status = page_instance.navigate_to_dashboard(self.test_data[environment]["base_url"])        # Go to Dashboard
            take_screenshot(self.page,"Navigated to Dashboard Page")                           # Take a screenshot of the Dashboard

            assert status, "Navigation to Dashboard Failed"                                              # Assert that the navigation was successful

        except Exception as e:
            take_screenshot(self.page, "Failed to navigate to Dashboard")                      # take screenshot if exception found
            assert False





    @allure.description("TC002: Create new Board")
    @pytest.mark.dependency(name="create_board", depends=["Navigate_dashboard"])
    @pytest.mark.parametrize("testing_data", ["testing_parameters"])
    @allure.severity(allure.severity_level.CRITICAL)


    def test_create_board(self, testing_data):
        try:
            board_name = self.test_data[testing_data]["board_name"]                                    # Get the board name from the test data
            page_instance = DashboardPage(self.page)                                                   # Create an instance of DashboardPage
            status = page_instance.create_new_board(board_name)                                        # Create a new board
            assert status, "Failed to create Board"                                                    # Assert that the board creation was successful
            take_screenshot(self.page, "Created Board")                                      # Take a screenshot of the created board

            page_instance = BoardPage(self.page)                                                       # Create an instance of BoardPage
            assert (page_instance.
                    verify_board_created(board_name)), "Failed to verify created Board"                # Assert that the created board is verified

        except Exception as e:
            take_screenshot(self.page, "Failed to create Board")                             # take screenshot if exception found
            assert False





    @allure.description("TC003: Create new Lists")
    @pytest.mark.dependency(name="create_lists", depends=["create_board"])
    @pytest.mark.parametrize("testing_data", ["testing_parameters"])
    @allure.severity(allure.severity_level.CRITICAL)


    def test_create_lists(self, testing_data):
        try:
            lists_name = self.test_data[testing_data]["list_name"]                                    # Get the list names from the test data

            page_instance = BoardPage(self.page)                                                      # Create an instance of BoardPage
            for name in lists_name:                                                                   # Loop through the list names
                status = page_instance.create_new_list(name)                                          # Create a new list
                assert status, "Failed to create List"                                                # Assert that the list creation was successful

            take_screenshot(self.page, "Created Lists")                                     # Take a screenshot of the created lists

            assert (page_instance.
                    verify_list_created(lists_name)), "Failed to verify created Lists"                # Assert that the created lists are verified

        except Exception as e:
            take_screenshot(self.page, "Failed to create Lists")                            # take screenshot if exception found
            assert False





    @allure.description("TC00: Delete a List")
    @pytest.mark.dependency(name="delete_list", depends=["create_lists"])
    @pytest.mark.parametrize("testing_data", ["testing_parameters"])
    @allure.severity(allure.severity_level.CRITICAL)


    def test_delete_list(self, testing_data):
        try:
            list_name = self.test_data[testing_data]["list_name"][1]                                   # Pick the second list name from the test data

            page_instance = BoardPage(self.page)                                                       # Create an instance of BoardPage

            status = page_instance.delete_list(list_name)                                              # Delete the list
            assert status, "Failed to delete List"                                                     # Assert that the list deletion was successful

            take_screenshot(self.page, "Delete List")                                        # Take a screenshot of the deleted list

            assert (page_instance.
                    verify_list_deleted(list_name)), "Failed to verify deleted List"                   # Assert that the deleted list is verified

        except Exception as e:
            take_screenshot(self.page, "Failed to delete Lists")                             # take screenshot if exception found
            assert False