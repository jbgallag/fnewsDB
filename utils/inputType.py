#!/usr/bin/python


import fnewsDBFunctions

with open('type.dat') as f:
   words = [word.strip() for word in f]



db = fnewsDBFunctions.connectDatabase();
cursor = db.cursor()
for x in words:
   sql = "INSERT INTO articleType (TYPE) VALUES ('%s')" % x
   cursor.execute(sql)
   db.commit()
   print sql

fnewsDBFunctions.disconnectDatabase(db)
