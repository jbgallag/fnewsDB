#!/usr/bin/python

import sys
import fnewsDBFunctions

with open(sys.argv[1]) as f:
   words = [word.strip() for word in f]



db = fnewsDBFunctions.connectDatabase();
cursor = db.cursor()
for x in words:
   sql = "INSERT INTO articleCategory (CATEGORY) VALUES ('%s')" % x
   cursor.execute(sql)
   db.commit()
   print sql

fnewsDBFunctions.disconnectDatabase(db)
