#!/usr/bin/python
print "Content-Type: text/html\n\n"

print "<html>"
print "<head>"
print "<title>FNews Magazine Article Database</title>"
print "<style>"
print "  .insert {"
print "     width:100%;"
print "     height:40%;"
print "   }"
print "   .Display {"
print "     width:100%;"
print "     height:60%;"
print "     overflow-x: auto;"
print "   }"
print "</style>"
print "</head>"
print "<body>"
print "<iframe class=\"insert\" src=\"/cgi-bin/fnewsDataConsole.py\" name=\"insert\"></iframe>"
print "<iframe class=\"Display\" src=about:blank name=\"Display\"></iframe>"
print "</body>"
print "</html>"
