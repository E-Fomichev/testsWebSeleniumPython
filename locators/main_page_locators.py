from selenium.webdriver.common.by import By

class MainPageLocators:
    ENTRY_FIELD = (By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/form/div")
    RUN_BUTTON = (By.XPATH, '//div[@class="ws-grey"]//button')
    CONTACT_NAME_ADDRESS = (By.XPATH, "//tr[td[contains(text(), 'Giovanni Rovelli')]]//td[contains(text(), 'Via Ludovico il Moro 22')]")
    CITY_LONDON = (By.XPATH, "//tr[td[contains(text(), 'London')]]")
    NEW_PERSON = (By.XPATH, "//tr[td[contains(text(), 'Ivan Ivanov')]]//td[contains(text(), 'Petr Petrov')]")




