from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
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

class traditionalOffice(Base):
    __tablename__ = 'traditional_office'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    city = Column(String(255))
    area = Column(String(255))
    address = Column(String(255))

kv = {'大楼名称':'name', '城市':'city', '区域':'area', '地址':'address'}

infos = [['大楼名称','a'],['城市','b'],['地址','d']]

l = {}

for info in infos:
    col = kv[info[0]]
    l[col] = info[1]

metadata = MetaData()

traditional_office = Table('traditional_office', metadata,
                Column('id', Integer(), primary_key=True),
                Column('name', String(255)),
                Column('city', String(255)),
                Column('area', String(255)),
                Column('address', String(255))
                )
