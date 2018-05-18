# coding=utf-8
from main import utils
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main.models import *


class Query:
    """Query collection class"""

    def __init__(self, db_path: str):
        """Initialize connection to database
        :arg db_path: path to target database."""
        self.engine = create_engine(db_path, echo=True)
        self.SessionClass = sessionmaker(bind=self.engine)

    def insert_general(self, obj: object) -> (bool, Exception):
        try:
            _s = self.SessionClass()
            _s.add(obj)
            _s.flush()
            _s.commit()
        except Exception as e:
            return False, e
        return True,None

    def insert_all(self, objects: object) -> (bool, Exception):
        """Insert 'objects' to database.
        :arg objects: expected target table instance object
        :return (True, None) is returned when success the insert, otherwise return (False, exception object)"""
        try:
            _s = self.SessionClass()
            _s.add_all(objects)
            _s.flush()
            _s.commit()
        except Exception as e:
            return False, e
        return True, None

    def get_salt(self, gid: int) -> str:
        """return the salt value of gid."""
        _s = self.SessionClass()
        return _s.query(Login_Information_Master.PasswordSalt).filter(Login_Information_Master.GroupId == gid).first()

    def get_passwordhash(self, gid: int) -> str:
        """get password hash value from database."""
        _s = self.SessionClass()
        return _s.query(Login_Information_Master.PasswordHash).filter(Login_Information_Master.GroupId == gid).first()

    def get_group(self, gid: int) -> Group_Master:
        """get a group of match of gid."""
        _s = self.SessionClass()
        return _s.query(Group_Master.id, Group_Master.groupname).filter(Group_Master.id == gid).first()

    def get_group_by_group_name(self, group_name: str) -> Group_Master:
        """get groups of match of group_name."""
        _s = self.SessionClass()
        return _s.query(Group_Master.id, Group_Master.groupname).filter(Group_Master.groupname == group_name).all()

    def _login_registration(self, login_info):
        ret = self.insert_general(login_info)
        if not (ret[0]):
            # when insert failed be throw exception.
            raise ret[1]
        else:
            return True

    def group_login_registration(self, gid: int, passwd: str) -> bool:
        g = self.get_group(gid)
        if g is not None:
            # group is already exists
            return False
        else:
            salt = utils.get_unique_str(len(Login_Information_Master.PasswordSalt))
            hash_code = utils.get_hashval(passwd, salt)
            info = Login_Information_Master(gid=gid, passwd_hs=hash_code, salt=salt)
            return self._login_registration(info)

    def get_zoo(self, zid: int) -> Zoo_Master:
        _s = self.SessionClass()
        return _s.query(Zoo_Master.id, Zoo_Master.ZooName).filter(Zoo_Master.id == zid).all()

    def set_zoo_calendar(self, zid: int, opening: DateTime, closing: DateTime):
        if self.get_zoo(zid) is not None:
            c = Zoo_Calendar_Master(zid, opening, closing)
            return self.insert_general(c)[0]
        return False

    def get_zoo_calendar(self, calid):
        _s = self.SessionClass()
        return _s.query(Zoo_Calendar_Master.id,
                        Zoo_Calendar_Master.ZooMasterId,
                        Zoo_Calendar_Master.OpeningDateTime,
                        Zoo_Calendar_Master.ClosingDateTime).filter(Zoo_Calendar_Master.id == calid).all()

    def get_group_calendar(self, gid: int, fromday, today):
        _s = self.SessionClass()
        return _s.query(Zoo_Calendar_Master.OpeningDateTime,
                        Zoo_Calendar_Master.ClosingDateTime)\
            .filter(Group_Calendar.ZooCalendarId == Zoo_Calendar_Master.id
                    and Group_Calendar.GroupId == gid)\
            .filter(Zoo_Calendar_Master.OpeningDateTime <= fromday
                    and today <= Zoo_Calendar_Master.ClosingDateTime)\
            .all()

    def set_group_calendar(self, calid: int, gid: int):
        """insert date time of group activity to GROUP_CALENDAR table."""
        if (self.get_group(gid) is not None) and (self.get_zoo_calendar(calid) is not None):
            c = Group_Calendar(gid, calid)
            return self.insert_general(c)[0]
        return False

    def get_all_zoo(self):
        """get all zoo from ZOO_MASTER table."""
        _s = self.SessionClass()
        return _s.query(Zoo_Master.id, Zoo_Master.ZooName).all()

    def get_all_groups(self):
        """get all groups from GROUP_MASTER table."""
        _s = self.SessionClass()
        return _s.query(Group_Master.id, Group_Master.groupname).all()

    def get_column_length(self, column):
        return column.type.length