# coding=utf-8
# coding=utf-8
from sqlalchemy import Column, Integer, Date, DateTime, Time, String, ForeignKey, func, MetaData
from sqlalchemy.ext.declarative import declarative_base, declared_attr

meta = MetaData(schema="kalendar")
Base = declarative_base(metadata=meta)


class MixInBase(object):
    __table_args__ = {'sqlite_autoincrement': True}

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    # index columns
    id = Column(Integer, primary_key=True, autoincrement=True)

    # who columns
    createdon = Column(DateTime, default=func.now(), nullable=False)
    createdby = Column(String(50), default='SYSTEM', nullable=False)
    lastupdateon = Column(DateTime, onupdate=func.now())
    lastupdateby = Column(String(50), default='SYSTEM')


# definition data tables.
class Zoo_Master(MixInBase, Base):
    """ZOO_MASTER table
    this table is define of zoos.
    Id: int: key(auto)
    ZooName: string: name of this zoo
    and who columns.
    """
    ZooName = Column(String(200))

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

    def __init__(self, gid, zoocalendarid):
        self.GroupId = gid
        self.ZooCalendarId = zoocalendarid


class Group_Master(MixInBase, Base):
    """GROUP table
    this table is define of groups.
    Id: int: key(auto)
    GroupCode: string: login code of this group
    GroupName: string: name of this group.
    and who columns.
    """
    groupcode = Column(String(10))
    groupname = Column(String(200))

    def __init__(self, group_code,group_name):
        self.groupcode = group_code
        self.groupname = group_name


class Login_Information_Master(MixInBase, Base):
    """LOGIN_INFORMATION_MASTER table
    this table is stored login information of any group.
    GroupId: int: link to GROUP.Id
    Password: string: hash of login password
    PasswordSalt: string: salt of password
    and who columns.
    * password stored hashed at SHA3-512
    """
    GroupId = Column(Integer, ForeignKey("GROUP.Id"), nullable=False)
    PasswordHash = Column(String(200), nullable=False)
    PasswordSalt = Column(String(200))

    def __init__(self, gid, passwd_hs, salt):
        self.GroupId = gid
        self.PasswordHash = passwd_hs
        self.PasswordSalt = salt



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

    def __init__(self, zooid, opening_date, closing_date):
        self.ZooMasterId = zooid
        self.OpeningDateTime = opening_date
        self.ClosingDateTime = closing_date
