# coding=utf-8
# coding=utf-8
from sqlalchemy import Column, Integer, Date, DateTime, Time, String, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base, declared_attr

Base = declarative_base()


class MixInBase(object):
    __table_args__ = {'sqlite_autoincrement': True}

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

#    # index columns
#    id = Column(Integer, primary_key=True, autoincrement=True)

    # who columns
    created_on = Column(DateTime, default=func.now())
    created_by = Column(String, default='SYSTEM')
    last_update_on = Column(DateTime, onupdate=func.now())
    last_update_by = Column(String, default='SYSTEM')
    row_count = Column(Integer, nullable=False)
    __mapper_args__ = {
        "version_id_col": row_count
    }


# definition data tables.
class Group_Calendar(MixInBase, Base):
    """GROUP_CALENDAR table
    GroupId: int: link to GROUP.Id
    ZooCalendarId: int: link to ZOO_CALENDAR.Id
    and who columns.
    """
    GroupId = Column(Integer, ForeignKey("GROUP.Id"), nullable=False)
    ZooCalendarId = Column(Integer, ForeignKey("ZOO_CALENDAR.Id"), nullable=False)


class Group_Master(MixInBase, Base):
    """GROUP table
    Id: int: key(auto)
    GroupName: string: name of this group.
    and who columns.
    """
    Id = Column(Integer, primary_key=True, autoincrement=True)
    GroupName = Column(String)

    def __init__(self, group_name):
        self.GroupName = group_name


class Login_Information_Master(MixInBase, Base):
    """LOGIN_INFORMATION_MASTER table
    GroupId: int: link to GROUP.Id
    PasswordHash: string: hash of login password
    and who columns.
    """
    GroupId = Column(Integer, ForeignKey("GROUP.Id"), nullable=False)
    PasswordHash = Column(String, nullable=False)

# class Zoo(MixInBase, Base):
#     """zoo table
#     id: int: key (auto)
#     zoo_name: string
#     """
#     zoo_name = Column(String)
#
#     def __init__(self, zoo_name):
#         self.zoo_name = zoo_name
#
#
# class User_(MixInBase, Base):
#     """user table
#     id: int: key (auto)
#     user_code: string: => 44xx
#     """
#     user_code = Column(String, unique=True)
#
#     def __init__(self, user_code):
#         self.user_code = user_code
#
#
# class Group_(MixInBase, Base):
#     """group_ table
#     id: int: key (auto)
#     group_name: string
#     zoo_id: int => link to Zoo.id
#     """
#     group_name = Column(String)
#     zoo_id = Column(Integer, ForeignKey("zoo.id"), nullable=False)
#
#     def __init__(self, group_name, zoo_id):
#         self.group_name = group_name
#         self.zoo_id = zoo_id
#
#
# class GroupActiveDay(MixInBase, Base):
#     """groupactiveday table
#     id: int: key (auto)
#     activity_date: date
#     activity_group_id: int => link to Group.id
#     """
#     active_day = Column(Date, nullable=False)
#     active_time_from = Column(String)
#     active_time_to = Column(String)
#     active_group_id = Column(Integer, ForeignKey("group_.id"), nullable=False)
#
#     def __init__(self, active_day, active_group_id):
#         self.active_day = active_day
#         self.active_group_id = active_group_id
#
#
# class UserActiveDay(MixInBase, Base):
#     """useractiveday table
#     activity_id: int => link to GroupActiveDay.id
#     user_id: int => link to User.user_id
#     """
#     active_id = Column(Integer, ForeignKey("groupactiveday.id"), nullable=False)
#     user_id = Column(Integer, ForeignKey("user_.id"), nullable=False)
#
#     def __init__(self, active_id, user_id):
#         self.active_id = active_id
#         self.user_id = user_id
