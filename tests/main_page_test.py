import time

from page.main_page import MainPage


class TestMainPage:

    def test1_check_contactname_and_address(self, driver):
        main_page = MainPage(driver, 'https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all')
        main_page.open()
        main_page.runSQL()
        main_page.checkNameAndAddress()

    def test2_check_cityLondon(self, driver):
        main_page = MainPage(driver, 'https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all')
        main_page.open()
        main_page.selectCityLondonScript()
        main_page.runSQL()
        time.sleep(1)
        main_page.checkLondonCount()

    def test3_create_customer(self, driver):
        main_page = MainPage(driver, 'https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all')
        main_page.open()
        main_page.createCustomerScript()
        main_page.runSQL()
        time.sleep(2)
        driver.refresh()
        main_page.runSQL()
        time.sleep(1)
        main_page.checkCreateCustomer()
        main_page.deleteCustomerScript()
        main_page.runSQL()

    def test4_update_customer(self, driver):
        main_page = MainPage(driver, 'https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all')
        main_page.open()
        main_page.updateCustomerScript()
        main_page.runSQL()
        time.sleep(2)
        driver.refresh()
        main_page.runSQL()
        time.sleep(1)
        main_page.checkUpdateCustomer()
        driver.refresh()
        main_page.reUpdateCustomerScript()
        main_page.runSQL()

    def test_num_columns(self, driver):
        main_page = MainPage(driver, 'https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all')
        main_page.open()
        main_page.runSQL()
        time.sleep(1)
        main_page.checkNumOfColumns()