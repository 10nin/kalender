# coding=utf-8
import os, configparser
from main import utils, models
from main.query import Query

class Controller:
    def __init__(self, config_filepath):
        cfg = configparser.ConfigParser()
        cfg.read(config_filepath, encoding="UTF-8")
        url = cfg["DATABASE"]["url"]
        self.db = Query(db_path=url)

    def call_get_all_groups(self):
        return self.db.get_all_groups()

    def password_success(self, gid: int, passwd: str) -> bool:
        """
        login hash value check for gid and password pair.
        :param gid: the target group id.
        :param passwd: target raw password string.
        :return: if login is success then True, otherwise False.
        """
        salt = self.db.get_salt(gid)
        current_hash = utils.get_hashval(passwd, salt)
        stored_hash = self.db.get_passwordhash(gid)
        return current_hash == stored_hash

    def group_registration(self, group_name):
        group_len = self.db.get_column_length(models.Group_Master.groupname)
        if len(group_name) > group_len:
            return False
        else:
            g = models.Group_Master(group_name=group_name)
            # ignore exception when insert.
            return self.db.insert_general(g,)[0]

if __name__ == "__main__":
    c = Controller("../setup.cfg")
    c.group_registration('TestGroup')
    print(c.call_get_all_groups())
