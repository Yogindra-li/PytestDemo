# -*- coding: utf-8 -*-
# @Author  : Yingying
# @Time    : 2021/12/20 2:36 下午
# @Function:

import os
from selenium.webdriver.common.by import By

# 项目目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# chrome驱动器目录
CHORME_DRIVER_PATH = os.path.join('/Users/yogindra/Desktop/PycharmProject', 'chromedriver')

# 日志目录
LOG_PATH = os.path.join(BASE_DIR, 'Logs')
ALL_LOG_PATH = os.path.join(BASE_DIR, 'logs', 'all.log')
ERROR_LOG_PATH = os.path.join(BASE_DIR, 'logs', 'error.log')

# 报告目录
REPORT_PATH = os.path.join(BASE_DIR, 'Reports')

# config.yaml文件目录
# CONFIG_PATH = os.path.join(BASE_DIR, 'TestData', 'config.yaml')

# search_data.yaml 文件目录
SEARCH_DATA_PATH = os.path.join(BASE_DIR, 'TestData', 'search_data.yaml')

# url
BASE_URL = 'https://v.qq.com/'

SEARCH_INPUT = (By.ID, 'keywords')
SEARCH_BUTTON = (By.XPATH, '//*[@id="searchForm"]/button')
HOTSEARCH_BUTTON = (By.XPATH, '//*[@id="searchForm"]/a')

NO_RESULT = (By.XPATH, '//*[@id="search_container"]/div[2]/div[1]/div/div[1]')
No_RESULT_DESC = '腾讯视频建议您：缩短搜索词 或 更换搜索词'
No_RESULT_DESC_LOC = (By.XPATH, '//*[@id="search_container"]/div[2]/div[1]/div/div[2]')
FIRST_RESULT = (By.XPATH, '//*[@id="search_container"]/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/div/h2')
ALL_RESULT = (By.CLASS_NAME, 'result_item_h')
#热搜排行榜页面
banner_title_class=(By.CLASS_NAME,'banner_title')
hotsearch_page_title = '全网影视排行榜_腾讯视频'

# 点击搜索框后出现的下拉副框内的元素定位
sb_history_name = '历史记录'
# sb_history = (By.XPATH, '//*[@id="smartbox"]/div[1]/div[1]/div[1]')
sb_history = (By.CLASS_NAME, 'sb_title')
sb_history_clear_name = '清除记录'
sb_history_clear = (By.XPATH, '//*[@id="smartbox"]/div[1]/div[1]/div[2]/a')
# sb_history_clear = (By.CLASS_NAME, 'sb_del')
sb_history_first = (By.XPATH, '//*[@id="smartbox"]/div[1]/div[2]/div[1]')
# sb_history_first = (By.CLASS_NAME,'')
sb_hotsearch_name = '热门搜索'
sb_hotsearch = (By.XPATH, '//*[@id="smartbox"]/div[2]/div[1]/div[1]')
sb_hotsearch_2 = (By.CLASS_NAME, 'sb_title')
sb_hotsearch_more_name = '更多搜索'
sb_hotsearch_more = (By.XPATH, '//*[@id="smartbox"]/div[2]/div[1]/div[2]/a')

sb_hotsearch_more_2 = (By.XPATH, '//*[@id="smartbox"]/div/div[1]/div[2]/a/span')
    # (By.XPATH, '//*[@id="smartbox"]/div/div[1]/div[2]/a/span')
