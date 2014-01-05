#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 定义注常量
CONNECT = 'mysql+mysqldb://root:123456@localhost/?charset=utf8'
DB_NAME = "papa"

class DB:
	def __init__(self):
		engine = create_engine(CONNECT, echo=True)

		# 创建DB
		#conn = engine.connect()
		#conn.execute("commit")
		engine.execute("CREATE DATABASE IF NOT EXISTS " + DB_NAME + " DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;")
		engine.execute("use " + DB_NAME)
		#conn.close()

		# 建立Session
		Session = sessionmaker(bind=engine)
		self.session = Session()

	def getSession(self):
		return self.session

	def close(self):
		if(self.session) self.session.close()
