from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
import pytest

@pytest.fixture()
def setup():
    path = "C:\chromedriver.exe"
    service = Service(path)
    driver = webdriver.Chrome(service=service)
    return driver
