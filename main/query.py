# coding=utf-8
from main import utils
from sqlalchemy import create_engine, extract
from sqlalchemy.orm import sessionmaker
from main.models import *


class Query:
    """Query collection class"""

    def __init__(self, db_path: str):
        """Initialize connection to database
        :arg db_path: path to target database."""
        self.engine = create_engine(db_path, echo=True)
        self.SessionClass = sessionmaker(bind=self.engine)

    @classmethod
    def _call_in_transaction(cls, s, fn, obj) -> (bool, Exception):
        if obj is None:
            return False, ValueError()

        try:
            fn(obj)
            s.flush()
            s.commit()
            s.close()
        except Exception as e:
            return False, e
        return True,None

    def delete_general(self, obj: object) -> (bool, Exception):
        _s = self.SessionClass()
        return Query._call_in_transaction(_s, _s.delete, obj)

    def insert_general(self, obj: object) -> (bool, Exception):
        _s = self.SessionClass()
        return Query._call_in_transaction(_s, _s.add, obj)

    def insert_all(self, objects: object) -> (bool, Exception):
        """Insert 'objects' to database.
        :arg objects: expected target table instance object
        :return (True, None) is returned when success the insert, otherwise return (False, exception object)"""
        _s = self.SessionClass()
        return Query._call_in_transaction(_s, _s.add, objects)

    def get_salt(self, gid: int) -> str:
        """return the salt value of gid."""
        _s = self.SessionClass()
        salt = _s.query(Login_Information_Master.passwordsalt).filter(Login_Information_Master.groupid == gid).scalar()
        _s.close()
        return salt if salt is not None else ''

    def get_passwordhash(self, gid: int) -> str:
        """get password hash value from database."""
        _s = self.SessionClass()
        hs =_s.query(Login_Information_Master.passwordhash).filter(Login_Information_Master.groupid == gid).scalar()
        _s.close()
        return hs if hs is not None else utils.get_unique_str(self.get_column_length(Login_Information_Master.passwordhash))

    def get_groups_by_group_name(self, group_name: str) -> Group_Master:
        """get groups of match of group_name."""
        _s = self.SessionClass()
        g = _s.query(Group_Master).filter(Group_Master.groupname == group_name).all()
        _s.close()
        return g

    def get_group(self, group_code: str) -> Group_Master:
        """get group by unique code."""
        _s = self.SessionClass()
        g = _s.query(Group_Master).filter(Group_Master.groupcode == group_code).first()
        _s.close()
        return g

    def _login_registration(self, login_info):
        ret = self.insert_general(login_info)
        if not (ret[0]):
            # when insert failed be throw exception.
            raise ret[1]
        else:
            return True

    def get_login_information(self, gid: int) -> Login_Information_Master:
        _s = self.SessionClass()
        li = _s.query(Login_Information_Master).filter(Login_Information_Master.groupid == gid).first()
        _s.close()
        return li

    def group_login_registration(self, gid: int, passwd: str) -> bool:
        li = self.get_login_information(gid)
        if li is not None:
            # group is already exists
            return False
        else:
            salt = utils.get_unique_str(self.get_column_length(Login_Information_Master.passwordsalt))
            hash_code = utils.get_hashval(passwd, salt)
            info = Login_Information_Master(gid=gid, passwd_hs=hash_code, salt=salt)
            return self._login_registration(info)

    def get_zoo(self, zid: int) -> Zoo_Master:
        _s = self.SessionClass()
        z = _s.query(Zoo_Master).filter(Zoo_Master.id == zid).all()
        _s.close()
        return z

    def set_zoo_calendar(self, zid: int, opening: DateTime, closing: DateTime):
        if self.get_zoo(zid) is not None:
            c = Zoo_Calendar_Master(zid, opening, closing)
            return self.insert_general(c)[0]
        return False

    def get_zoo_calendar(self, calid):
        _s = self.SessionClass()
        cal = _s.query(Zoo_Calendar_Master).filter(Zoo_Calendar_Master.id == calid).all()
        _s.close()
        return cal

    def get_zoo_schedules(self, zooid, year, month):
        _s = self.SessionClass()
        sc = _s.query(Zoo_Calendar_Master).filter(Zoo_Calendar_Master.zoomasterid == zooid)\
               .filter(extract('year', Zoo_Calendar_Master.calendarday) == year)\
               .filter(extract('month', Zoo_Calendar_Master.calendarday) == month)\
               .order_by(Zoo_Calendar_Master.calendarday).all()
        _s.close()
        return sc

    def get_group_calendars(self, gid: int, calendarids: list):
        _s = self.SessionClass()
        cal = _s.query(Group_Calendar)\
                .filter(Group_Calendar.groupid == gid and Group_Calendar.zoocalendarid in calendarids).all()
        _s.close()
        return cal

    def get_group_calendar(self, gid: int, calendarid: int):
        _s = self.SessionClass()
        c = _s.query(Group_Calendar)\
              .filter(Group_Calendar.groupid == gid)\
              .filter(Group_Calendar.zoocalendarid == calendarid).first()
        _s.close()
        return c

    def delete_group_calendar(self, gc: Group_Calendar):
        return self.delete_general(gc)

    def insert_group_calendar(self, gc: Group_Calendar):
        return self.insert_general(gc)

    def set_group_calendar(self, calid: int, group_code: str):
        """insert date time of group activity to GROUP_CALENDAR table."""
        g = self.get_group(group_code)
        if (g is not None) and (self.get_zoo_calendar(calid) is not None):
            c = Group_Calendar(g.id, calid)
            return self.insert_general(c)[0]
        return False

    def get_zoocalendar_groupcalendar_joined(self, year, month):
        _s = self.SessionClass()
        r = _s.query(Zoo_Calendar_Master, Group_Calendar, Group_Master, Opening_Closing_Pattern_Master)\
              .join(Group_Calendar, Zoo_Calendar_Master.id == Group_Calendar.zoocalendarid) \
              .join(Group_Master, Group_Calendar.groupid == Group_Master.id) \
              .join(Opening_Closing_Pattern_Master, Opening_Closing_Pattern_Master.id == Zoo_Calendar_Master.openingclosingid) \
              .filter(extract('year', Zoo_Calendar_Master.calendarday) == year) \
              .filter(extract('month', Zoo_Calendar_Master.calendarday) == month) \
              .order_by(Zoo_Calendar_Master.calendarday).all()
        _s.close()
        return  r

    def get_exists_calendar(self, year: int, month: int, days: list) -> dict:
        ret = dict()
        for d in days:
            ret[d] = self.is_exits_in_calendar(year, month, d)
        return  ret

    def is_exits_in_calendar(self, year: int, month: int, day: int) -> bool:
        cal_data = self.get_zoocalendar_groupcalendar_joined(year, month)
        if day == 0:
            return False # GUARD for convert exception.
        for c in cal_data:
            if self._is_same_day(c.Zoo_Calendar_Master.calendarday, year, month, day):
                return True
        return False

    def _is_same_day(self, calendarday, year, month, day) -> bool:
        return calendarday.year == year and calendarday.month == month and calendarday.day == day

    def get_time_type(self, ocid: int) -> str:
        _s = self.SessionClass()
        c = _s.query(Opening_Closing_Pattern_Master).filter(Opening_Closing_Pattern_Master.id == ocid).first()
        _s.close()
        return c.timetype

    def get_all_zoo(self):
        """get all zoo from ZOO_MASTER table."""
        _s = self.SessionClass()
        z = _s.query(Zoo_Master).all()
        _s.close()
        return z

    def get_all_groups(self):
        """get all groups from GROUP_MASTER table."""
        _s = self.SessionClass()
        g = _s.query(Group_Master).all()
        _s.close()
        return g

    @classmethod
    def get_column_length(cls, column):
        return column.type.length