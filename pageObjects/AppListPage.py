from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage


class AppListPage(BasePage):
    MENU = (By.XPATH, "//a[@class='full']")
    APPS = (By.LINK_TEXT, "Apps")
    SEARCH_TAG = (By.XPATH, "//div[@class='o_searchview_facet']")
    UPDATE_APP_LIST = (By.XPATH, "//ul[@class='o_menu_sections']//span[contains(text(),'Update Apps List')]")
    UPDATE_MODULE = (By.NAME, "update_module")
    USER_MENU = (By.CLASS_NAME, "o_user_menu")
    LOGOUT = (By.LINK_TEXT, "Log out")

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def clickMenu(self):
        self.click(self.MENU)

    def selectApps(self):
        self.click(self.APPS)

    def clickUpdateAppList(self):
        self.click(self.UPDATE_APP_LIST)

    def clickUpdateModuleBtn(self):
        self.click(self.UPDATE_MODULE)

    def logout(self):
        self.click(self.USER_MENU)
        self.click(self.LOGOUT)

    # def remove_search_tags(self):

