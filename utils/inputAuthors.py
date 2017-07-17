#!/usr/bin/python

import sys
import codecs
import fnewsDBFunctions

with codecs.open(sys.argv[1], 'r', 'utf8') as f:
   words = [word.strip() for word in f]



db = fnewsDBFunctions.connectDatabase();
cursor = db.cursor()

for x in words:
   sql = "select author from articleAuthor where Author=\"%s\"" % x.encode('utf8')
   rows_count = cursor.execute(sql)
   if rows_count == 0:
      sql = "INSERT INTO articleAuthor (AUTHOR) VALUES ('%s')" % x.encode('utf8')
      cursor.execute(sql)
      print "Inserted new Author: %s" % sql
   db.commit()
   #print sql

fnewsDBFunctions.disconnectDatabase(db)
