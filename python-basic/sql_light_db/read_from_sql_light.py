import sqlite3
import json


with sqlite3.connect('db.sqlite3') as conn:
	command = "select * from movies"
	cursor=conn.execute(command)
	# for row in cursor:
	# 	print(row)
	movies_list =(cursor.fetchall())
	print(movies_list)



