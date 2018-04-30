# coding=utf-8
import utils
from sqlalchemy import create_engine, func, insert
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models import *



class Query:
    """Query collection class"""

    def __init__(self, db_path: str):
        """Initialize connection to database
        :arg db_path: path to target database."""
        self.engine = create_engine(db_path, echo=True)
        self.SessionClass = sessionmaker(bind=self.engine)

    def _insert_general(self, objects: object) -> (bool, Exception):
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

    def _get_salt(self, gid: int) -> str:
        """"""
        _s = self.SessionClass()
        return _s.query(Login_Information_Master.PasswordSalt).filter(Login_Information_Master.GroupId == gid).first()

    def _get_passwordhash(self, gid: int) -> str:
        _s = self.SessionClass()
        return _s.query(Login_Information_Master.PasswordHash).filter(Login_Information_Master.GroupId == gid).first()

    def get_group(self, gid: int) -> Group_Master:
        _s = self.SessionClass()
        _s.query(Group_Master.Id, Group_Master.GroupName).filter(Group_Master.Id == gid).first()

    def login(self, gid: int, passwd: str) -> bool:
        salt = self._get_salt(gid)
        current_hash = utils.get_hashval(passwd, salt)
        stored_hash = self._get_passwordhash(gid)
        return current_hash == stored_hash

    def _group_registration(self, login_info):
        ret = self._insert_general(login_info)
        if not (ret[0]):
            # when insert failed be throw exception.
            raise ret[1]
        else:
            return True

    def group_registration(self, gid: int, passwd: str) -> bool:
        g = self.get_group(gid)
        if g is not None:
            # group is already exists
            return False
        else:
            salt = utils.get_unique_str(len(Login_Information_Master.PasswordSalt))
            hash_code = utils.get_hashval(passwd, salt)
            info = Login_Information_Master(gid=gid, passwd_hs=hash_code, salt=salt)
            return self._group_registration(info)

    def get_all_zoo(self):
        _s = self.SessionClass()
        return _s.query(Zoo_Master.Id, Zoo_Master.ZooName).all()
