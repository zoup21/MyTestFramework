import time

from selenium.webdriver.common.by import By


class Login:
    text_box_username_id = "user-name"
    text_box_password_id = "password"
    button_login_id = "login-button"
    title_After_Login_XPATH = "//div/span[@class='title']"
    error_messages_username_password_XPATH = "//h3[@data-test='error']"
    button_logout_id = "logout_sidebar_link"
    button_openBurger_menu_id= "react-burger-menu-btn"




    def __init__(self , driver):
        self.driver=driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.text_box_username_id).clear()
        self.driver.find_element(By.ID, self.text_box_username_id).send_keys(username)

    def setPassword(self , password):
        self.driver.find_element(By.ID, self.text_box_password_id).clear()
        self.driver.find_element(By.ID, self.text_box_password_id).send_keys(password)

    def clickLoginButton(self):
        self.driver.find_element(By.ID, self.button_login_id).click()

    def clickLogoutButton(self):
        self.driver.find_element(By.ID, self.button_openBurger_menu_id).click()
        time.sleep(1)
        self.driver.find_element(By.ID, self.button_logout_id).click()

    def confirmedLogin(self):
        msg = self.driver.find_element(By.XPATH, self.title_After_Login_XPATH).text
        return msg

    def isLogoutButtonPresent(self):
        try:
            self.driver.find_element(By.ID, self.button_openBurger_menu_id)
            return True
        except:
            return False