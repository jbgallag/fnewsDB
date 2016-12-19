#!/usr/bin/python

import fnewsDBFunctions

adata = fnewsDBFunctions.GetArticleAuthorList()
edata = fnewsDBFunctions.GetArticleEditorList()
tdata = fnewsDBFunctions.GetArticleTypeList()
cdata = fnewsDBFunctions.GetArticleCategoryList()

print "Content-type: text/html\n\n"

print "<html>"
print "<body bgcolor=#ffffff>"
print "<hr noshade>"
print "<font size = 4><b>fnews Article Database</b></font>"
print "<hr noshade>"
print "<font size=3><b>Insert New Data:</b></font><br>"
print "<table>"
print "<tr>"
print "<form action=\"/cgi-bin/fnewsInsertMain.py\" method=\"post\" target=\"Display\">"
print "<td>Article Title:<br>"
print "<input type=text name=\"Title\" size=30>"
print "</td>"
print "<td>Article Author:<br>"
print "<select name=\"Author\">"
for row in adata:
    print "<option>%s" % row['author']
print "</select> </td>"
print "<td>Article Editor:<br>"
print "<select name=\"Editor\">"
for row in edata:
    print "<option>%s" % row['editor']
print "</select> </td>"

print "<td>Date:<br>"
print "<input type=date name=\"Date\" size=30>"
print "</td>"
print "<td> Article Type:<br>"
print "<select name=\"Type\">"
for row in tdata:
    print "<option>%s" % row['type']
print "</select>"
print "</td>"
print "<td> Article Category:<br>"
print "<select name=\"Category\">"
for row in cdata:
    print "<option>%s" % row['category']
print "</select>"
print "</td>"
print "<td>URL:<br>"
print "<input type=text name=\"Url\" size=30>"
print "</td>"
print "</tr>"
print "<tr>"
print "<td><input type=submit value=\"Submit\"></td>"
print "</form>"
print "</tr>"
print "</table>"
print "<font size=3><b>Query Data:</b></font><br>"
print "<table>"
print "<tr>"
print "<form action=\"/cgi-bin/fnewsQueryMain.py\" method=\"post\" target=\"Display\">"
print "<td>Article Title:<br>"
print "<input type=text name=\"Title\" value=\"NONE\" size=30>"
print "</td>"
print "<td>Article Author:<br>"
print "<select name=\"Author\">"
print "<option>NONE"
for row in adata:
    print "<option>%s" % row['author']
print "</select></td>"
print "<td>Article Editor:<br>"
print "<select name=\"Editor\">"
print "<option>NONE"
for row in edata:
    print "<option>%s" % row['editor']
print "</select> </td>"
print "<td>Date:<br>"
print "<input type=date name=\"Date\" size=30>"
print "</td>"
print "<td>Date (End Range):<br>"
print "<input type=date name=\"DateEnd\" size=30>"
print "</td>"
print "<td> Article Type:<br>"
print "<select name=\"Type\">"
print "<option>NONE"
for row in tdata:
    print "<option>%s" % row['type']
print "</select>"
print "</td>"
print "<td> Article Category:<br>"
print "<select name=\"Category\">"
print "<option>NONE"
for row in cdata:
    print "<option>%s" % row['category']
print "</select>"
print "</td>"
print "<td> URL: <br>"
print "<input type=text name=\"Url\" size=30>"
print "</td>"
print "</tr>"
print "<tr>"
print "<td><input type=submit value=\"Query\"></td>"
print "</tr>"
print "</form>"
print "</table>"
print "<font size=3><b>Graph Data:</b></font><br>"
print "<table>"
print "<form action=\"/cgi-bin/fnewsGraphMain.py\" method=\"post\" target=\"Display\">"
print "<td>X-Axis Field:<br>"
print "<select name=\"xaxis\">"
print "<option>Author"
print "<option>Type"
print "<option>Category"
print "</select>"
print "<td>Article Author:<br>"
print "<select name=\"Author\">"
print "<option>NONE"
for row in adata:
    print "<option>%s" % row['author']
print "</select></td>"
print "<td>Article Editor:<br>"
print "<select name=\"Editor\">"
print "<option>NONE"
for row in edata:
    print "<option>%s" % row['editor']
print "</select> </td>"
print "<td>Date:<br>"
print "<input type=date name=\"Date\" size=30>"
print "</td>"
print "<td>Date (End Range):<br>"
print "<input type=date name=\"DateEnd\" size=30>"
print "</td>"
print "<td> Article Type:<br>"
print "<select name=\"Type\">"
print "<option>NONE"
for row in tdata:
    print "<option>%s" % row['type']
print "</select>"
print "</td>"
print "<td> Article Category:<br>"
print "<select name=\"Category\">"
print "<option>NONE"
for row in cdata:
    print "<option>%s" % row['category']
print "</select>"
print "</td>"
print "</tr>"
print "<tr>"
print "<td><input type=submit value=\"Graph\"></td>"
print "</tr>"
print "</form>"
print "</table>"
print "<a href=\"/cgi-bin/fnewsAddFields.py\">Add Categories, Types and Editors</a>"
print "</body>"
print "</html>"

