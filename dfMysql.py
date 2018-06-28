import pandas as pd
from sqlalchemy import create_engine
import pymysql.cursors

# MySQL Connector using pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

engine = create_engine("mysql+mysqldb://root:"+"wnsgml159"+"@junhee.czmeph7testl.ap-northeast-2.rds.amazonaws.com/crawlingtest", encoding='utf-8')
conn = engine.connect()