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

    def group_registration(self, group_code, group_name):
        group_name_len = self.db.get_column_length(models.Group_Master.groupname)
        group_code_len = self.db.get_column_length(models.Group_Master.groupcode)

        if ((len(group_code) != group_code_len) or
                len(group_name) > group_name_len):
            # required group_code length is constant length,
            # and group_name length is less than field length.
            return None
        else:
            g = models.Group_Master(group_code=group_code, group_name=group_name)
            ret = self.db.insert_general(g)
            if ret[0]:
                return g
            else:
                return ret

    def group_unregistration(self, group_code):
        group_code_len = self.db.get_column_length(models.Group_Master.groupcode)

        if len(group_code) != group_code_len:
            return  None

        g = self.db.get_group(group_code=group_code)
        ret = self.db.delete_general(g)
        if ret[0]:
            return g
        else:
            return ret

    def get_group_calendar(self, group_code):
        g = self.db.get_group(group_code=group_code)
        ret = self.db.get_group_calendar(g.id)
        return ret


if __name__ == "__main__":
    c = Controller("../setup.cfg")
    gcode = '02-0000-01'
    cal = c.get_group_calendar(gcode)
    for i in cal:
        print("OP: " + str(i.openingdatetime))
        print("CL: " + str(i.closingdatetime))

