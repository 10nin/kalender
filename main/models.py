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
    zooname = Column(String(200))

    def __init__(self, zooname):
        self.zooname = zooname


class Group_Calendar(MixInBase, Base):
    """GROUP_CALENDAR table
    this table is joining group schedule and zoo schedule.
    GroupId: int: link to GROUP.Id
    ZooCalendarId: int: link to ZOO_CALENDAR.Id
    and who columns.
    """
    groupid = Column(Integer, ForeignKey("group_master.id"), nullable=False)
    zoocalendarid = Column(Integer, ForeignKey("zoo_calendar.id"), nullable=False)

    def __init__(self, gid, zoocalendarid):
        self.groupid = gid
        self.zoocalendarid = zoocalendarid


class Group_Master(MixInBase, Base):
    """GROUP table
    this table is define of groups.
    Id: int: key(auto)
    GroupCode: string: login code of this group
    GroupName: string: name of this group.
    and who columns.
    """
    groupcode = Column(String(10), unique=True)
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
    groupid = Column(Integer, ForeignKey("group_master.id"), unique=True, nullable=False)
    passwordhash = Column(String(200), nullable=False)
    passwordsalt = Column(String(200))

    def __init__(self, gid, passwd_hs, salt):
        self.groupid = gid
        self.passwordhash = passwd_hs
        self.passwordsalt = salt


class Opening_Closing_Pattern_Master(MixInBase, Base):
    """OPENING_CLOSING_PATTERN_MASTER table
    this table is define of opening and closing time set.
    Id: int: key(auto)
    Opening: from time
    Closing: to time
    and who columns.
    """
    opening = Column(Time, nullable=False)
    closing = Column(Time, nullable=False)

    def __init__(self, openingtime, closingtime):
        self.opening = openingtime
        self.closing = closingtime


class Zoo_Calendar_Master(MixInBase, Base):
    """ZOO_CALENDAR_MASTER table
    this table is define of activity on zoo.
    Id: int: key(aout)
    ZooMasterId: int: link to ZOO_MASTER.Id
    OpeningClosingId: int: link to OPENING_CLOSING_PATTERN_MASTER.Id
    and who columns.
    """
    zoomasterid = Column(Integer, ForeignKey("zoo_master.Id"), nullable=False)
    openingclosingid = Column(Integer, ForeignKey("opening_closing_pattern_master.id"), nullable=False)

    def __init__(self, zooid, openingclosingid):
        self.zoomasterid = zooid
        self.openingclosingid = openingclosingid
