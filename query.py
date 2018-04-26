# coding=utf-8
from sqlalchemy import create_engine, func, insert
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models import *


class Query:
    """Query collection class"""

    def __init__(self, db_path):
        """Initialize connection to database
        :arg db_path: path to target database."""
        self.engine = create_engine(db_path, echo=True)
        self.SessionClass = sessionmaker(bind=self.engine)

    def _insert_general(self, objects):
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
