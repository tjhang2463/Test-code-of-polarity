#coding=utf-8

from snownlp import SnowNLP
from snownlp import seg
import MySQLdb

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='',
        db ='forum',
        )

cur = conn.cursor()
cur.execute("SET NAMES utf8mb4;")
SQL = "SELECT * FROM forum"
cur.execute(SQL)
results = cur.fetchall() # get all data

for row in results:
    text = row[6].encode("cp950", "ignore")
    s = SnowNLP(text)
    print (s.sentiments)

