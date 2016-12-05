#!/usr/local/bin/python

import os
import MySQLdb
import cgi
#imports for matplotlib (plotting library, Agg is for off screen rendering)
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
matplotlib.rcParams.update({'font.size': 8})

os.environ['PYTHON_EGG_CACHE'] = '/tmp'
selectFields = ['Title','Author','Date','DateEnd','Type','Category','Url']
xaxisField = ''
host = "localhost"
dbuser = ""
dbpass = ""
dbase = ""
outputFile = ""

def PrintQueryResult (qdata):
   print "<table border=0 cellspacing=10>"
   print "<th align=left>Title:</th> <th align=left>Author:</th> <th align=left>Date:</th> <th align=left>Type:</th> <th align=left>Category:</th> <th align=left>Link:</th>"
   for row in qdata:
      print "<tr>"
      print "<td> %s </td>" % row['Title']
      print "<td> %s </td>" % row['Author']
      print "<td> %s </td>" % row['Date']
      print "<td> %s </td>" % row['Type']
      print "<td> %s </td>" % row['Category']
      print "<td> <a href=\"%s\">Article Link</a> </td>" % row['Url']
      print "</tr>"
   print "</table>"



def GetSqlQueryString():
   mc = 0
   useRange = 0;
   sql = "select * from ArticleInfo"

   if form.getvalue('DateEnd', '') != '':
	useRange = 1

   for field in selectFields:
	if useRange == 0:
		if form.getvalue(field, '') != "NONE" and form.getvalue(field, '') != '':
			if mc == 0:
				sql = sql + ' where ' + field + '=' + '\'' + form.getvalue(field, '') + '\''
			else:
				sql = sql + ' and ' + field + '=' + '\'' + form.getvalue(field, '') + '\''
			mc = mc + 1
        else:
		if field != "Date" and field != "DateEnd" and form.getvalue(field, '') != "NONE" and form.getvalue(field, '') != '':
			if mc == 0:
                                sql = sql + ' where ' + field + '=' + '\'' + form.getvalue(field, '') + '\'' 
                        else:
                                sql = sql + ' and ' + field + '=' + '\'' + form.getvalue(field, '') + '\'' 
                        mc = mc + 1

   if useRange == 1:
	if mc == 0:
		sql = sql + ' where ' + ' Date' + '>=' + '\'' + form.getvalue('Date', '') + '\'' + ' and ' + 'Date' + '<=' + '\'' + form.getvalue('DateEnd', '') + '\''
	else:
		sql = sql + ' and ' + 'Date' + '>=' + '\'' + form.getvalue('Date', '') + '\'' + ' and ' + 'Date' + '<=' + '\'' + form.getvalue('DateEnd', '') + '\'' 

   return sql

def GetQueryData(sqlin):

   db = connectDatabase() 
   cursor = db.cursor(MySQLdb.cursors.DictCursor) 
   cursor.execute(sqlin)
   db.commit()
   data = cursor.fetchall()
   disconnectDatabase(db)
   return data;

def GetArticleAuthorList():
   sql = "select * from articleAuthor"
   db = connectDatabase()
   cursor = db.cursor(MySQLdb.cursors.DictCursor)
   cursor.execute(sql)
   db.commit()
   data = cursor.fetchall()
   disconnectDatabase(db)
   return data

def GetArticleTypeList():
   sql = "select * from articleType"
   db = connectDatabase()
   cursor = db.cursor(MySQLdb.cursors.DictCursor)
   cursor.execute(sql)
   db.commit()
   data = cursor.fetchall()
   disconnectDatabase(db)
   return data

def GetArticleCategoryList():
   sql = "select * from articleCategory"
   db = connectDatabase()
   cursor = db.cursor(MySQLdb.cursors.DictCursor)
   cursor.execute(sql)
   db.commit()
   data = cursor.fetchall()
   disconnectDatabase(db)
   return data

def InsertArticleAuthor():
    aAuth = form.getvalue('newAuthor', '')
    db = connectDatabase()
    #get db cursor and submit sql
    cursor = db.cursor()
    sql = "INSERT INTO articleAuthor (AUTHOR) VALUES ('%s')" % aAuth
    cursor.execute(sql)
    db.commit()
    #disconnect from db
    disconnectDatabase(db)

def InsertArticleType():
    aType = form.getvalue('newType', '')
    db = connectDatabase()
    #get db cursor and submit sql
    cursor = db.cursor()
    sql = "INSERT INTO articleType (TYPE) VALUES ('%s')" % aType
    cursor.execute(sql);
    db.commit()
    #disconnect from db
    disconnectDatabase(db)

def InsertArticleCategory():
    aCat = form.getvalue('newCategory', '')
    db = connectDatabase()
    #get db cursor and submit sql
    cursor = db.cursor()
    sql = "INSERT INTO articleCategory (CATEGORY) VALUES ('%s')" % aCat
    cursor.execute(sql)
    db.commit()
    #disconnect from db
    disconnectDatabase(db)

def DeleteArticleAuthor():
    aAuth = form.getvalue('authors', '')
    db = connectDatabase()
    #get db cursor and submit sql
    cursor = db.cursor()
    sql = "DELETE FROM articleAuthor where Author='%s'" % aAuth
    cursor.execute(sql);
    db.commit()
    #disconnect from db
    disconnectDatabase(db)

def DeleteArticleType():
    aType = form.getvalue('types', '')
    db = connectDatabase()
    #get db cursor and submit sql
    cursor = db.cursor()
    sql = "DELETE FROM articleAuthor where Type='%s'" % aType
    cursor.execute(sql);
    db.commit()
    #disconnect from db
    disconnectDatabase(db)

def DeleteArticleCategory():
    aCat = form.getvalue('categories', '')
    db = connectDatabase()
    #get db cursor and submit sql
    cursor = db.cursor()
    sql = "DELETE FROM articleAuthor where Category='%s'" % aCat
    cursor.execute(sql);
    db.commit()
    #disconnect from db
    disconnectDatabase(db)

def InsertDataFromFormInput():
   #get html form data and copy data into corresponding variables
   aTitle = form.getvalue('Title', '')
   aAuth = form.getvalue('Author', '')
   aDate = form.getvalue('Date', '')
   aType = form.getvalue('Type', '')
   aCat = form.getvalue('Category', '')
   aUrl = form.getvalue('Url', '')
   #get data base handle and insert data
   db = connectDatabase()
   #get db cursor and submit sql
   cursor = db.cursor()
   cursor.execute("""INSERT INTO ArticleInfo (TITLE, AUTHOR, DATE, TYPE, CATEGORY, URL) VALUES (%s, %s, %s, %s, %s, %s)""",(aTitle, aAuth, aDate, aType, aCat, aUrl))
   db.commit()
   #disconnect from db
   disconnectDatabase(db)
   

def GraphOutput (qdata):
   grData = {}
   for row in qdata:
        grKey = row[xaxisField]
        grData[grKey] = 0;
   for row in qdata:
        grKey = row[xaxisField]
        grData[grKey] = grData[grKey] + 1;

   plotKeys = grData.keys();
   plotValues = grData.values();

   fig = plt.figure(figsize=(8,4))
   x_pos = np.arange(len(plotKeys))
   plt.bar(x_pos,plotValues,xerr=0,align='center',alpha=0.75, facecolor='g')
   plt.xticks(x_pos, plotKeys)
   plt.ylabel('Number of Articles')
   fig.savefig(outputFile)

   print "<div align=center><img src=\"http://localhost/dbTest/graph.png\"></div>"

def getXlabel():
  return form.getvalue('xaxis', '')

def connectDatabase():
    db = MySQLdb.connect(host=host, user=dbuser, passwd=dbpass, db=dbase)
    return db 

def disconnectDatabase(db):
    db.close()

#global vars
form = cgi.FieldStorage()
xaxisField = getXlabel()

