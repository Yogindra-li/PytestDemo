# -*- coding: utf-8 -*-
# @Author  : Yingying
# @Time    : 2021/12/20 2:36 下午
# @Function:
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Config.config import CHORME_DRIVER_PATH, BASE_URL
from Pages.SearchPage import SearchPage
from Pages.SBSearchPage import SBSearchPage

driver = None


@pytest.fixture(scope='class', autouse=True)
def init_driver(request):
    global driver
    s = Service('/Users/yogindra/Desktop/PycharmProject/TecentVideo_pytest/chromedriver')
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.get(BASE_URL)
    request.cls.driver = driver
    request.cls.search = SearchPage(driver)
    request.cls.sb_search = SBSearchPage(driver)
    driver.implicitly_wait(5)
    driver.title
    yield
    driver.close()
        # quit()
