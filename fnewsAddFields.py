#!/usr/bin/python

import fnewsDBFunctions

adata = fnewsDBFunctions.GetArticleAuthorList()
tdata = fnewsDBFunctions.GetArticleTypeList()
cdata = fnewsDBFunctions.GetArticleCategoryList()

print "Content-type: text/html\n\n"

print "<html>"
print "<body bgcolor=#ffffff>"
print "<table>"

print "<td>"

print "<font size=3><b>Insert New Author:</b></font><br>"
print "<table>"
print "<tr>"
print "<form action=\"/cgi-bin/fnewsInsertAuthorMain.py\" method=\"post\">"
print "<td>New Author:<br>"
print "<input type=text name=\"newAuthor\" size=30>"
print "</td>"
print "</tr>"
print "<tr>"
print "<td><input type=submit value=\"Add Author\"></td>"
print "</form>"
print "</tr>"
print "<tr>"
print "<form action=\"/cgi-bin/fnewsDeleteAuthorMain.py\" method=\"post\">"
print "<td>Existing Authors:<br>"
print "<select name=\"authors\">"
for row in adata:
   print "<option>%s" % row['author']
print "</select></td>"
print "</tr>"
print "<tr>"
print "<td><input type=\"submit\" value=\"Delete Author\"></td>"
print "</tr>"
print "</form>"
print "</table>"

print "</td>"

print "<td>"

print "<font size=3><b>Insert New Type:</b></font><br>"
print "<table>"
print "<tr>"
print "<form action=\"/cgi-bin/fnewsInsertTypeMain.py\" method=\"post\">"
print "<td>New Type:<br>"
print "<input type=text name=\"newType\" size=30>"
print "</td>"
print "</tr>"
print "<tr>"
print "<td><input type=submit value=\"Add Type\"></td>"
print "</form>"
print "</tr>"
print "<tr>"
print "<form action=\"/cgi-bin/fnewsDeleteTypeMain.py\" method=\"post\">"
print "<td>Existing Types:<br>"
print "<select name=\"types\">"
for row in tdata:
   print "<option>%s" % row['type']
print "</select></td>"
print "</tr>"
print "<tr>"
print "<td><input type=\"submit\" value=\"Delete Type\"></td>"
print "</tr>"
print "</form>"
print "</table>"

print "</td>"

print "<td>"
print "<font size=3><b>Insert New Category:</b></font><br>"
print "<table>"
print "<tr>"
print "<form action=\"/cgi-bin/fnewsInsertCategoryMain.py\" method=\"post\">"
print "<td>New Category:<br>"
print "<input type=text name=\"newCategory\" size=30>"
print "</td>"
print "</tr>"
print "<tr>"
print "<td><input type=submit value=\"Add Category\"></td>"
print "</form>"
print "</tr>"
print "<tr>"
print "<form action=\"/cgi-bin/fnewsDeleteCategoryMain.py\" method=\"post\">"
print "<td>Existing Categories:<br>"
print "<select name=\"categories\">"
for row in cdata:
   print "<option>%s" % row['category']
print "</select></td>"
print "</tr>"
print "<tr>"
print "<td><input type=\"submit\" value=\"Delete Category\"></td>"
print "</tr>"
print "</form>"
print "</table>"

print "</td>"

print "</table>"
print "</body>"
print "</html>"





