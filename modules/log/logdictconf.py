#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   logLoadConfig.py
@Time    :   2019/09/27 14:49:38
@Author  :   baoy.bao 
@Version :   1.0
@Contact :   zeroleavebaoy@163.com
@License :   (C)Copyright 2019-2021
@Desc    :   None
'''

# here put the import lib
import json
import logging.config
import os


def setup_logging(default_path="logging.json", default_level=logging.INFO, env_key="LOG_CFG"):
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, "r") as f:
            config = json.load(f)
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


def func():
    logging.info("start func")

    logging.info("exec func")

    logging.info("end func")


if __name__ == "__main__":
    setup_logging(default_path="logging.json")
    func()
