# -*- coding: utf-8 -*-
# @Author  : Yingying
# @Time    : 2021/12/20 12:13 下午
# @Function:
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def send_key(self, text, *by_loactor):
        '''在页面元素中输入值（输入之前先清空）'''
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(*by_loactor)).clear()
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(*by_loactor)).send_keys(text)

    def click_btn(self, *by_loactor):
        '''按下键盘上的某个按键'''
        e = EC.visibility_of_element_located(*by_loactor)
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(*by_loactor)).click()

    def is_contains_title(self, title):
        is_contain = WebDriverWait(self.driver, 2).until(EC.title_contains(title))
        return is_contain

    def is_contains_text(self, text, *by_loactor):
        '''页面body中是否包含text'''
        try:
            is_contain = WebDriverWait(self.driver, 2).until(EC.text_to_be_present_in_element(*by_loactor, text))
        except TimeoutException:
            is_contain = False
        return is_contain

    def get_elements_size(self, *by_loactor):
        '''返回页面中元素的数量'''
        elements = self.driver.find_elements(*by_loactor)
        return len(elements)

    def get_element_text(self, *by_loactor):
        '''返回元素的text'''
        text = self.driver.find_element(*by_loactor).text()
        return text

    def go_to_url(self, url):
        self.driver.get(url)

    def refresh(self):
        self.driver.refresh()

    def get_title(self):
        title = self.driver.title
        return title
