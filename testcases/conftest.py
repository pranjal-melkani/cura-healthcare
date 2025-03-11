import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options


@pytest.fixture(scope='session', autouse=True)
def driver():
    URL = "https://katalon-demo-cura.herokuapp.com/"
    opt = Options()
    opt.add_argument('--headless')
    driver = webdriver.Edge(opt)
    driver.get(URL)
    driver.maximize_window()
    yield driver
    driver.quit()