# -*- coding: utf-8 -*-
# @Author  : Yingying
# @Time    : 2021/12/20 3:28 下午
# @Function:
import pytest


@pytest.mark.usefixtures('init_driver')
class BaseTest:
    pass
