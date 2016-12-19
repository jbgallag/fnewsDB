#!/usr/bin/python


import sys
import codecs
import fnewsDBFunctions


db = fnewsDBFunctions.connectDatabase()
cursor = db.cursor()
with codecs.open(sys.argv[1], 'r', 'utf8') as f:
   words = [word.strip() for word in f]

for line in words:
    fields = line.split("::");

    title = fields[0]
    auth = fields[1]
    date = fields[2]
    type = fields[3]
    cat = fields[4]
    url = fields[5]
    #print "%s,%s,%s,%s,%s,%s" % (title,auth,date,type,cat,url)
    cursor.execute("""INSERT INTO ArticleInfo (TITLE, AUTHOR, DATE, TYPE, CATEGORY, URL) VALUES (%s, %s, %s, %s, %s, %s)""",(title.encode('utf8'),auth.encode('utf8'),date.encode('utf8'),type.encode('utf8'),cat.encode('utf8'),url.encode('utf8')))
    db.commit()

fnewsDBFunctions.disconnectDatabase(db)

