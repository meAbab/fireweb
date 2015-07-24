#!/usr/bin/perl
print "Content-type: text/html\n\n";
print "<html><head>\n";
print "<title>fireWEB Change Password</title>\n";
print '<body>';
print '<form action="pass_change.cgi" method="POST">';
print "Old Pass    : ".'<input type="password" name="oldpass">'."<br>";
print "New Pass    : ".'<input type="password" name="newpass1">'."<br>";
print "Confirm Pass: ".'<input type="password" name="newpass2">'."<br>";
print '<input type="submit" name="sub" value="Change Pass">';
print '</body>';
print '</head>';
print '</html>';
