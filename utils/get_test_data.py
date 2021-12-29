# -*- coding: utf-8 -*-
# @Author  : Yingying
# @Time    : 2021/12/20 3:56 下午
# @Function:
from Config.config import SEARCH_DATA_PATH
import yaml
import numpy as np


def get_search_notes():
    test_data_file = open(SEARCH_DATA_PATH)
    data_dict = yaml.load(test_data_file, Loader=yaml.FullLoader)
    test_notes = data_dict.keys()
    return test_notes


def get_search_data():
    test_data_file = open(SEARCH_DATA_PATH)
    data_dict = yaml.load(test_data_file, Loader=yaml.FullLoader)
    keyword = data_dict.values()
    test_notes = data_dict.keys()

    search_data = np.empty(shape=[0, 2])
    for a, b in zip(keyword, test_notes):
        search_data = np.append(search_data, [[a, b]], axis=0)  # 添加整行数据
    return search_data
