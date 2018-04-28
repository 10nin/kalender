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

    def _get_salt(self, gid: str) -> Login_Information_Master:
        """"""
        _s = self.SessionClass()
        return _s.query(Login_Information_Master.PasswordSalt).filter(Login_Information_Master.GroupId == gid).all()

    def _get_passwordhash(self, gid: str) -> str:
        _s = self.SessionClass()
        return _s.query(Login_Information_Master.Password).filter(Login_Information_Master.GroupId == gid).first()

    def login(self, gid: str, passwd: str) -> bool:
        salt = self._get_salt(gid)
        current_hash = utils.get_hashval(passwd, salt)
        stored_hash = self._get_passwordhash(gid)
        return current_hash == stored_hash
