# -*- coding: utf-8 -*-
# @Author  : Yingying
# @Time    : 2021/12/21 4:27 下午
# @Function:
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Tests.test_base import BaseTest


class TEST_ABC(BaseTest):
    SEARCH_INPUT = (By.ID, 'keywords')
    SEARCH_BUTTON = (By.XPATH, '//*[@id="searchForm"]/button')
    HOTSEARCH_BUTTON = (By.XPATH, '//*[@id="searchForm"]/a')
    # 热搜排行榜页面
    banner_title_class = (By.CLASS_NAME, 'banner_title')
    banner_title = '全网影视排行榜'

    ALL_RESULT = (By.CLASS_NAME, 'result_item result_item_h _quickopen')

    @pytest.mark.skip('no')
    def test_1(self):
        self.driver.find_elements(*self.HOTSEARCH_BUTTON).click
        windows = self.driver.window_handles()
        self.driver.switch_to.window(windows[-1])
        # self.driver.finde_element(self.banner_title_class,self.banner_title)

        is_clear_history = WebDriverWait(self.driver, 3).until(
            EC.text_to_be_present_in_element(self.banner_title_class, self.banner_title))
        print(is_clear_history)
        assert is_clear_history

    def test_2(self):
        self.driver.find_element(*self.SEARCH_INPUT).send_keys('你好')
        self.driver.find_element(*self.SEARCH_BUTTON).click()
        e = self.driver.find_elements(*self.ALL_RESULT)
        print(e)


if __name__ == '__main__':
    pytest.main(['-sv', 'test.py'])
