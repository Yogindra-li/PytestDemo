# -*- coding: utf-8 -*-
# @Author  : Yingying
# @Time    : 2021/12/20 3:27 下午
# @Function:
from Pages.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Config.config import *


class SearchPage(BasePage):

    def __int__(self, driver):
        super.__init__(driver)

    def input_text(self, keyword):
        self.send_key(keyword, SEARCH_INPUT)

    def click_search_button(self):
        self.click_btn(SEARCH_BUTTON)

    def click_search_input(self):
        self.click_btn(SEARCH_INPUT)

    def click_hotsearch_button(self):
        self.click_btn(HOTSEARCH_BUTTON)

    def no_search_results(self):
        is_contains = self.is_contains_text(No_RESULT_DESC, No_RESULT_DESC_LOC)
        return is_contains

    def elements_size(self):
        number = self.get_elements_size(*ALL_RESULT)
        return number

    def is_page_tile(self):
        title =self.get_title()
        if title==hotsearch_page_title:
            return True
        else:
            return False
        # is_contains = self.is_contains_text(banner_title, banner_title_class)

    def back_to_homepage(self):
        self.go_to_url(BASE_URL)

    def switch_to_newest_window(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

