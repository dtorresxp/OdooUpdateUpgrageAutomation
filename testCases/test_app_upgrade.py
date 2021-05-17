import subprocess
import time
import os
import subprocess

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestUpdate:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.logGen()

    def test_upgrade(self, setup):
        subprocess.call(['runas', '/user:Administrator', 'NET STOP odoo-server-12.0'])
        time.sleep(5)
        subprocess.call(['runas', '/user:Administrator', 'NET START odoo-server-12.0'])

        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)

        self.lp.enterUserName(self.username)
        self.lp.enterPassword(self.password)
        self.alp = self.lp.login()

        time.sleep(10)

        self.alp.clickMenu()
        self.alp.selectApps()
        time.sleep(10)
        self.alp.upgrade_app("Library_Management")

        self.alp.logout()

        self.driver.close()
