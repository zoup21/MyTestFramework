import time

from selenium.webdriver.common.by import By
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class TestLogin_ddt:
    baseUrl = ReadConfig.getApplicationURL()
    path = ".\\TestData\Mock-Testdata.xlsx"

    logger = LogGen.loggen()

    def test_Login_ddt(self, setup):
        self.logger.info("**********Verify Login DDT test**********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = Login(self.driver)

        self.rows = XLUtils.getRowCount(self.path, "Φύλλο1")
        lst_Status = []
        for r in range(3, self.rows + 1):
            self.user = XLUtils.readData(self.path, "Φύλλο1", r, 1)
            self.password = XLUtils.readData(self.path, "Φύλλο1", r, 2)
            self.exp = XLUtils.readData(self.path, "Φύλλο1", r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)

            self.lp.clickLoginButton()
            time.sleep(1)
            login = self.lp.isLogoutButtonPresent()
            if login:
                if self.exp == "Pass":
                    self.logger.info("**********passed**********")
                    lst_Status.append("Pass")
                    self.lp.clickLogoutButton()
                elif self.exp == "Fail":
                    self.logger.info("**********failed**********")
                    lst_Status.append("Fail")
                    self.lp.clickLogoutButton()
            elif not login:
                if self.exp == "Pass":
                    self.logger.info("**********failed**********")
                    lst_Status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("**********passed**********")
                    lst_Status.append("Pass")

        if "Fail" not in lst_Status:
            self.logger.info("Login DDT test passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login DDT test failed")
            self.driver.close()
            assert False
