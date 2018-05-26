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

    def get_all_groups(self):
        return self.db.get_all_groups()

    def is_login_success(self, groupcode: str, passwd: str) -> bool:
        g = self.db.get_group(group_code=groupcode)
        if g is None:
            return False # group not found
        return self._password_success(g.id, passwd=passwd)

    def _password_success(self, gid: int, passwd: str) -> bool:
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

    def group_registration(self, group_code, group_name, passwd):
        group_name_len = self.db.get_column_length(models.Group_Master.groupname)
        group_code_len = self.db.get_column_length(models.Group_Master.groupcode)

        if ((len(group_code) != group_code_len) or
                len(group_name) > group_name_len):
            # required group_code length is constant length,
            # and group_name length is less than field length.
            return None
        else:
            _g = models.Group_Master(group_code=group_code, group_name=group_name)
            ret = self.db.insert_general(_g)
            if ret[0]:
                _g = self.db.get_group(group_code=group_code)
                return self.db.group_login_registration(gid=_g.id, passwd=passwd)
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

    def get_schedule(self, group_code, year, month):
        g = self.db.get_group(group_code=group_code)
        sched = self.db.get_zoo_schedules(g.zooid, year, month)
        calendarids = [i.id for i in sched]
        _gcal = self.db.get_group_calendar(g.id, calendarids)
        ingcal = [i.zoocalendarid for i in _gcal]
        ret = list()
        for s in sched:
            r = dict()
            r['day'] = s.calendarday
            r['time'] = self.db.get_time_type(s.openingclosingid)
            r['ox'] = 1 if s.id in ingcal else 0
            ret.append(r)
        return ret

    def get_group_name(self, group_code):
        g = self.db.get_group(group_code=group_code)
        if g is None:
            return ""
        else:
            return g.groupname


if __name__ == "__main__":
    c = Controller("../setup.cfg")
    gcode = '00-0000-00'
    passwd = 'abcdefg'
    #c.group_registration(group_code=gcode, group_name='testgroup', passwd=passwd)
    print(c.is_login_success(groupcode=gcode, passwd=passwd))

