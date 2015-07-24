#!/usr/bin/perl

use CGI qw( param header );
my $first_pass=param('gopon');
print "Content-type:text/html\r\n\r\n";
print "<html>";
print "<head>";
print "<title>This is your PERL IP allow Program</title>";
print "</head>";
print "<body>";

use CGI;
use warnings;
use strict;
use Crypt::CBC;
my $KEY = 'secrect_foo';

        my $readfile ="pass.txt";

        open my $passfile, '<', $readfile or die "could not open file";
        my $readpass = do{ local $/; <$passfile> };

#        print "Reading pass from file: $readpass\n";

        close ($readfile);


my $dec = decryptString($readpass);

	if($dec eq $first_pass)
		{
			print "<h2>Password Matched<h2>\n";
			my $q = new CGI;
#			print $q->remote_host();
			my $ip = $q->remote_host();
#			print "\n $ip \n";
	
			system("sudo /sbin/iptables -F");
			system("sudo /sbin/iptables -A INPUT -s $ip -j ACCEPT");
#			system("sudo /sbin/iptables -A INPUT -j DROP");  // uncomment this line if you want all IP block to access 
#									    the server acept your current public ip. Use it at your own risk.
	
			print "\n Your IP : $ip is allow in this system.\n";

		}
	else{
			print "Stored Pass mismatch\n";
		}


print "Change Password: ";
print '<a href="changepass.cgi">Click Here</a>';
print "</body>";
print "</html>";


sub decryptString {
        my $string = shift;
        my $cipher = Crypt::CBC->new(
                -key    => $KEY,
                -cipher => 'Blowfish',
                -padding => 'space',
                -add_header => 1
        );

        my $dec = $cipher->decrypt($string);
        return $dec;
}
