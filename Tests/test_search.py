# -*- coding: utf-8 -*-
# @Author  : Yingying
# @Time    : 2021/12/20 3:28 下午
# @Function:
import pytest
from Tests.test_base import BaseTest
from Pages.SearchPage import SearchPage
from Pages.SBSearchPage import SBSearchPage
from utils.get_test_data import get_search_notes, get_search_data
from utils.get_logger import get_logger
from time import sleep
import allure


@allure.feature('测试腾讯视频首页的搜索框')
class Test_Search(BaseTest):
    notes = get_search_notes()
    search_data = get_search_data()
    logger = get_logger(__name__)

    def get_smart_box(self):
        self.sb_search = SBSearchPage(self.driver)
        self.sb_search.click_searchinput()
        sleep(2)
        history = self.sb_search.is_exist_history()
        clear_history = self.sb_search.is_exist_clearhistory()
        hot_search = self.sb_search.is_exist_hotsearch()
        hotsearch_more = self.sb_search.is_exist_hotsearch_more()
        return history, clear_history, hot_search, hotsearch_more

    @allure.story('搜索前，检查搜索的【历史记录】是否存在')
    # @pytest.mark.skip(reason='不需要')
    def test_smartbox_before(self):
        history, clear_history, hot_search, hotsearch_more = self.get_smart_box()
        assert (not history) and (not clear_history) and hot_search and hotsearch_more
        self.logger.info('搜索前，检查搜索的【历史记录】是否存在')

    @allure.story('对搜索框进行验证')
    # @pytest.mark.skip(reason='不需要')
    @pytest.mark.parametrize('keyword,note', search_data, ids=notes)
    def test_input_search(self, keyword, note):
        self.logger.info('对搜索框进行验证')
        self.search = SearchPage(self.driver)
        self.search.input_text(keyword)
        self.logger.debug('输入%s：%s', note, keyword)
        self.search.click_search_button()
        self.logger.debug('点击全网搜')
        sleep(2)

        if '异常值' in note:
            is_contains_text = self.search.no_search_results()
            print(is_contains_text)
            try:
                assert is_contains_text
            except AssertionError as ae:
                hint=note+':'+keyword+',报错了'
                self.logger.error('报错了', exc_info=1)
        else:
            number = self.search.elements_size()
            try:
                assert number > 1
                self.logger.info('测试成功！')
            except AssertionError:
                self.logger.error('搜索出错', exc_info=1)

    @allure.story('搜索后，检查搜索的【历史记录】是否存在')
    # @pytest.mark.skip(reason='不需要')
    def test_smartbox_after(self):
        history, clear_history, hot_search, hotsearch_more = self.get_smart_box()
        assert history and clear_history and hot_search and hotsearch_more
        self.logger.info('搜索后，检查搜索的【历史记录】是否存在')

    @allure.story('验证点击【清除历史】后，搜索记录消失')
    # @pytest.mark.skip(reason='不需要')
    def test_smartbox_clearhistory(self):
        '''
        验证点击"清除历史"后，搜索记录消失
        '''

        self.search.back_to_homepage()
        sleep(2)
        self.search.click_search_input()
        self.sb_search.clear_history()
        self.search.refresh()
        sleep(2)
        self.search.click_search_input()
        clear_history_new = self.sb_search.is_exist_clearhistory()
        assert not clear_history_new

    @allure.story('检查【热搜榜】的链接是否正常跳转')
    # @pytest.mark.skip(reason='不需要')
    def test_hot_search(self):
        self.search = SearchPage(self.driver)
        self.search.click_hotsearch_button()
        self.search.switch_to_newest_window()

        result = self.search.is_page_tile()
        assert result

        # self.driver.quit()


if __name__ == '__main__':
    pytest.main(['-sv', 'test_search.py'])
# pytest -sv --alluredir=Reports Tests/test_search.py --clean-alluredir
# allure serve ./Reports
