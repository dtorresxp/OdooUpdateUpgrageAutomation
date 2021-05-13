import subprocess
import time

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestUpdate:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.logGen()

    def test_upgrade(self, setup):
        cmd = '"F:\\Odoo 12.0\\python\\python.exe" "F:\\Odoo 12.0\\server\\odoo-bin" --conf "F:\\Odoo 12.0\\server\\odoo.conf"'
        p = subprocess.Popen(cmd)

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

        p.kill()
        print('process killed')

        self.driver.close()
