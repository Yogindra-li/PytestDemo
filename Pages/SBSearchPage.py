# -*- coding: utf-8 -*-
# @Author  : Yingying
# @Time    : 2021/12/22 11:12 上午
# @Function:
from selenium.common.exceptions import TimeoutException

from Pages.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Config.config import *


class SBSearchPage(BasePage):
    def __int__(self, driver):
        super.__init__(driver)

    def click_searchinput(self):
        self.click_btn(SEARCH_INPUT)

    def clear_history(self):
        self.driver.find_element(*sb_history_clear).click()

    def is_exist_history(self):
        element = self.is_contains_text(sb_history_name, sb_history)
        return element

    def is_exist_clearhistory(self):
        element = self.is_contains_text(sb_history_clear_name, sb_history_clear)
        return element

    def is_exist_hotsearch(self):
        element = self.is_contains_text(sb_hotsearch_name, sb_hotsearch)
        if not element:
            element = self.is_contains_text(sb_hotsearch_name, sb_hotsearch_2)
        return element

    def is_exist_hotsearch_more(self):
        # element = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(sb_hotsearch_more))
        element = self.is_contains_text(sb_hotsearch_more_name, sb_hotsearch_more)
        if not element:
            try:
                element = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located(sb_hotsearch_more_2))
            except TimeoutException:
                element = False
        return element

    def click_clearhistory(self):
        self.click_btn(sb_history_clear)

    def click_hotsearch_more(self):
        self.click_btn(sb_hotsearch_more)
