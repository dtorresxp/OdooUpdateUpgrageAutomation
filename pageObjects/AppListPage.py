import time

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

    search_apps_tb = (By.XPATH, "//input[@accesskey='Q']")
    drop_down = (By.XPATH, "//a[@aria-label='Dropdown menu']")
    upgrade = (By.LINK_TEXT, "Upgrade")

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

    def upgrade_app(self, app_name):
        self.type_and_enter(self.search_apps_tb, app_name)
        time.sleep(5)
        self.click(self.drop_down)
        self.click(self.upgrade)
        time.sleep(60)

    def logout(self):
        self.click(self.USER_MENU)
        self.click(self.LOGOUT)

    # def remove_search_tags(self):

