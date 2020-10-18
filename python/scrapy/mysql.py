from pymysql import Date
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://yiqing:yiqing@39.98.49.111:3306/yiqing')
DBsession = sessionmaker(bind=engine)
session = DBsession()

Base = declarative_base()


connection=engine.connect()

class tmpUrls(Base):
    __tablename__ = 'tmp_urls'
    id = Column(Integer, primary_key=True)
    url = Column(String(255))

class tmpUrlsJL(Base):
    __tablename__ = 'tmp_urlsjl'
    id = Column(Integer, primary_key=True)
    url = Column(String(255))

class traditionalOffice(Base):
    __tablename__ = 'traditional_office'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    city = Column(String(255))
    area = Column(String(255))
    address = Column(String(255))


metadata = MetaData()

traditional_office = Table('traditional_office', metadata,
                Column('id', Integer(), primary_key=True),
                Column('name', String(255)),
                Column('city', String(255)),
                Column('area', String(255)),
                Column('address', String(255)),
                Column('completion_time', String(255)),
                Column('floor_number', Integer()),
                Column('floor_height', Float()),
                Column('office_owner', String(255)),
                Column('property_company', String(255)),
                Column('peoelv_number', Integer()),
                Column('freelv_number', Integer())
                )

sign_building = Table('sign_building', metadata,
                Column('id', Integer(), primary_key=True),
                Column('name', String(255)),
                Column('address', String(255)),
                Column('height', String(255)),
                Column('wall_type', Text),
                Column('wall_area', String(255)),
                Column('href', String(255))
                )

future_room = Table('future_room', metadata,
                Column('id', Integer(), primary_key=True),
                Column('name', String(255)),
                Column('tags', Text),
                Column('address', String(255)),
                Column('opening_date', String(255)),
                Column('city', String(255)),
                Column('url', String(255))
                )

tmp_uniscid = Table('tmp_uniscid', metadata,
                    Column('id', Integer(), primary_key=True),
                    Column('uniscid', String(255)),
                    Column('entname', String(255))
                    )

bidding_ggzy = Table('bidding_ggzy', metadata,
                    Column('id', Integer(), primary_key=True),
                    Column('bidding_people', String(255)),
                    Column('name', String(255)),
                    Column('field', String(255)),
                    Column('begin_date', String(255)),
                    Column('money', Float()),
                    Column('company', String(255))
                    )