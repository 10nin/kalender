# coding=utf-8
import os, configparser
from main.query import Query


class Controller:
    def __init__(self, config_filepath):
        cfg = configparser.ConfigParser()
        cfg.read(config_filepath, encoding="UTF-8")
        url = cfg["DATABASE"]["url"]
        self.db = Query(db_path=url)

    def call_get_all_groups(self):
        return self.db.get_all_groups()


if __name__ == "__main__":
    c = Controller("../setup.cfg")
    print(c.call_get_all_groups())
