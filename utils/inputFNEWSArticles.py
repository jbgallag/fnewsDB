#!/usr/bin/python


import sys
import codecs
import fnewsDBFunctions


db = fnewsDBFunctions.connectDatabase()
cursor = db.cursor()
with codecs.open(sys.argv[1], 'r', 'utf8') as f:
   words = [word.strip() for word in f]

for line in words:
    fields = line.split("	");

    title = fields[0]
    auth = fields[1]
    date = fields[2]
    type = fields[3]
    cat = fields[4]
    url = fields[5]
    img = fields[6]
    imgAuth = fields[7]
   
    #make sure data isn;t already in database 
    sql = "select Url from ArticleInfo where URL=\"%s\"" % url.encode('utf8')
    rows_count=cursor.execute(sql)
    if rows_count == 0:
    	cursor.execute("""INSERT INTO ArticleInfo (TITLE, AUTHOR, DATE, TYPE, CATEGORY, URL, ILLUSTRATION, ILLUSTRATION_AUTHOR) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",(title.encode('utf8'),auth.encode('utf8'),date.encode('utf8'),type.encode('utf8'),cat.encode('utf8'),url.encode('utf8'),img.encode('utf8'),imgAuth.encode('utf8')))
    db.commit()

    #check if illustrations have been updated (this is a fix for the one time update, otherwise will be handled above for new data) 
    rows_count=cursor.execute("""select Illustration from ArticleInfo where Url=%s AND Illustration=%s""",(url.encode('utf8'),img.encode('utf8')))
    if rows_count == 0:
	cursor.execute("""update ArticleInfo SET ILLUSTRATION=%s, ILLUSTRATION_AUTHOR=%s WHERE Url=%s""",(img.encode('utf8'),imgAuth.encode('utf8'),url.encode('utf8')))

    db.commit()

fnewsDBFunctions.disconnectDatabase(db)

