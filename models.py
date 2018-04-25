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

    # index columns
    Id = Column(Integer, primary_key=True, autoincrement=True)

    # who columns
    createdon = Column(DateTime, default=func.now(), nullable=False)
    createdby = Column(String, default='SYSTEM', nullable=False)
    lastupdateon = Column(DateTime, onupdate=func.now())
    lastupdateby = Column(String, default='SYSTEM')


# definition data tables.
class Zoo_Master(MixInBase, Base):
    """ZOO_MASTER table
    this table is define of zoos.
    Id: int: key(auto)
    ZooName: string: name of this zoo
    and who columns.
    """
    ZooName = Column(String)

    def __init__(self, zooname):
        self.ZooName = zooname


class Group_Calendar(MixInBase, Base):
    """GROUP_CALENDAR table
    this table is joining group schedule and zoo schedule.
    GroupId: int: link to GROUP.Id
    ZooCalendarId: int: link to ZOO_CALENDAR.Id
    and who columns.
    """
    GroupId = Column(Integer, ForeignKey("GROUP.Id"), nullable=False)
    ZooCalendarId = Column(Integer, ForeignKey("ZOO_CALENDAR.Id"), nullable=False)


class Group_Master(MixInBase, Base):
    """GROUP table
    this table is define of groups.
    Id: int: key(auto)
    GroupName: string: name of this group.
    and who columns.
    """
    GroupName = Column(String)

    def __init__(self, group_name):
        self.GroupName = group_name


class Login_Information_Master(MixInBase, Base):
    """LOGIN_INFORMATION_MASTER table
    this table is stored login information of any group.
    GroupId: int: link to GROUP.Id
    Password: string: hash of login password
    PasswordSalt: string: salt of password
    and who columns.
    * password stored hashed at SHA-512
    """
    GroupId = Column(Integer, ForeignKey("GROUP.Id"), nullable=False)
    Password = Column(String, nullable=False)
    PasswordSalt = Column(String)


class Zoo_Calendar_Master(MixInBase, Base):
    """ZOO_CALENDAR_MASTER table
    this table is define of activity on zoo.
    Id: int: key(aout)
    ZooMasterId: int: link to ZOO_MASTER.Id
    OpeningDateTime: timestamp: Opening date time of this zoo
    ClosingDateTime: timestamp: Closing date time of this zoo
    and who columns.
    """
    ZooMasterId = Column(Integer, ForeignKey("ZOO_MASTER.Id"), nullable=False)
    OpeningDateTime = Column(DateTime, nullable=False)
    ClosingDateTime = Column(DateTime, nullable=False)
