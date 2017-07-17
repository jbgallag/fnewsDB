#!/usr/bin/python


import fnewsDBFunctions


print "Content-type: text/html\n\n"

sql = fnewsDBFunctions.GetSqlQueryString()
data = fnewsDBFunctions.GetQueryData(sql)
fnewsDBFunctions.GraphOutput(data,sql)
