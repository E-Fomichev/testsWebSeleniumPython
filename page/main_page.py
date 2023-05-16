import allure
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators as Locators
from page.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.arg1 = None

    def runSQL(self):
        with allure.step("Нажимаем на кнопку RUN SQL"):
            self.element_is_visible(Locators.RUN_BUTTON).click()


    def checkNameAndAddress(self):
        with allure.step("Проверяем что у данного пользователя имеется данный адрес"):
            state = self.element_is_visible(Locators.CONTACT_NAME_ADDRESS).is_displayed()
            if state != True:
                raise ValueError(f"The given ContactName does not contain such Address")

    def checkLondonCount(self):
        with allure.step("Проверяем количество значения 'Лондон' в выдаче"):
            count = self.driver.find_elements(By.XPATH, "//tr[td[contains(text(), 'London')]]")
            if len(count) != 6:
                raise ValueError(f"The number of selected item is not equal to 6")

    def updateCustomerScript(self):
        with allure.step("Запускаем скрипт на изменение данных Customer'а"):
            self.driver.execute_script('window.editor.setValue(\'UPDATE Customers SET CustomerName ="Vladimir Lenin", ContactName = "Iosif Stalin", Address = "Red Place 1",City = "Moscow", PostalCode = "666999", Country = "USSR" WHERE CustomerID = 1;\')')

    def reUpdateCustomerScript(self):
        with allure.step("Запускаем скрипт на возвращение исходных данных Customer'а"):
            self.driver.execute_script('window.editor.setValue(\'UPDATE Customers SET CustomerName ="Alfreds Futterkiste", ContactName = "Maria Anders", Address = "Obere Str. 57",City = "Berlin", PostalCode = "12209", Country = "Germany" WHERE CustomerID = 1;\')')

    def createCustomerScript(self):
        with allure.step("Запускаем скрипт на создание нового Customer'а"):
            self.driver.execute_script('window.editor.setValue(\'INSERT INTO Customers (CustomerName,ContactName,Address,City,PostalCode,Country) VALUES ("Ivan Ivanov","Petr Petrov","Polevay str. 2","Leningrad","188666","Russia")\')')

    def deleteCustomerScript(self):
        with allure.step("Запускаем скрипт на удаление Customer'а"):
            self.driver.execute_script('window.editor.setValue(\'DELETE FROM CUSTOMERS WHERE CustomerID = 92\')')

    def selectCityLondonScript(self):
        with allure.step("Запускаем скрипт на выдачу City = Лондон"):
            self.driver.execute_script("window.editor.setValue('SELECT * FROM Customers WHERE City = \"London\"')")

    def checkCreateCustomer(self):
        with allure.step("Проверяем что добавленный Customer отображается в таблице"):
            checkCustomer = ("92 Ivan Ivanov Petr Petrov Polevay str. 2 Leningrad 188666 Russia")
            numberOfLines = self.driver.find_elements(By.XPATH, "//table[@class= 'ws-table-all notranslate']/tbody/tr")
            lastNum = len(numberOfLines)
            new_customer = self.driver.find_elements(By.XPATH, f"//table[@class= 'ws-table-all notranslate']/tbody/tr[{lastNum}]")
            for i in new_customer:
                person = i.text
            if person != checkCustomer:
                raise ValueError(f"Customer is not found")

    def checkUpdateCustomer(self):
        with allure.step("Проверяем что отредактированный Customer отображается в таблице с новыми данными"):
            checkCustomer = ("1 Vladimir Lenin Iosif Stalin Red Place 1 Moscow 666999 USSR")
            new_customer = self.driver.find_elements(By.XPATH, f"//table[@class= 'ws-table-all notranslate']/tbody/tr[2]")
            for i in new_customer:
                person = i.text
            if person != checkCustomer:
                raise ValueError(f"Customer is not found")

    def checkNumOfColumns(self):
        with allure.step("Проверка что в талице 7 столбцов"):
            numOfColumns = self.driver.find_elements(By.XPATH, "//table[@class= 'ws-table-all notranslate']//tbody/tr[2]/td")
            if len(numOfColumns) != 7:
                raise ValueError(f"The number of selected item is not equal to 7")