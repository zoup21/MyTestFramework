
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestLogin:

    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    baseUrl =  ReadConfig.getApplicationURL()

    logger = LogGen.loggen()

    def test_positiveLogin(self, setup):
        self.logger.info("**********Verify Title**********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLoginButton()
        title = self.driver.title
        if title == "Swag Labs":
            assert True
            self.driver.close()
            self.logger.info("**********Verify Title test is passed**********")
        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_positiveLogin.png")
            self.driver.close()
            self.logger.error("**********Verify Title test is failed**********")
            assert False

    def test_negativeLoginWrongPassword(self, setup):
        self.logger.info("**********Wrong password test**********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword("wrong password")
        self.lp.clickLoginButton()
        errorMessage = self.driver.find_element(By.XPATH, self.lp.error_messages_username_password_XPATH).text
        self.driver.close()
        assert "Epic sadface: Username and password do not match any user in this service" in errorMessage
        self.logger.info("**********Wrong password test passed**********")

    def test_negativeLoginWrongUsername(self , setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = Login(self.driver)
        self.lp.setUserName("wrong_username")
        self.lp.setPassword(self.password)
        self.lp.clickLoginButton()
        errorMessage = self.driver.find_element(By.XPATH, self.lp.error_messages_username_password_XPATH).text
        self.driver.close()
        assert "Epic sadface: Username and password do not match any user in this service" in errorMessage

    def test_negativeLoginEmptyUsername(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = Login(self.driver)
        self.lp.setPassword(self.password)
        self.lp.clickLoginButton()
        errorMessage = self.driver.find_element(By.XPATH, self.lp.error_messages_username_password_XPATH).text
        self.driver.close()
        assert "Epic sadface: Username is required" in errorMessage

    def test_negativeLoginEmptyPassword(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.clickLoginButton()
        errorMessage = self.driver.find_element(By.XPATH, self.lp.error_messages_username_password_XPATH).text
        self.driver.close()
        assert "Epic sadface: Password is required" in errorMessage
