#!/usr/bin/perl

use CGI qw( param header );
my $old_pass=param('oldpass');
my $new_pass=param('newpass1');
my $new_pass2=param('newpass2');
print header({-type=>'text/html'});
use CGI;
use warnings;
use strict;
use Crypt::CBC;
my $KEY = 'secrect_foo';
        
	my $readfile ="pass.txt";

        open (my $passfile, '<', $readfile) or die "could not open file";
        my $readpass = do{ local $/; <$passfile> };

#        print "Reading pass from file: $readpass\n";

        close ($passfile);


my $dec = decryptString($readpass);

	if($dec eq $old_pass)
		{
		print "<h2>Password Matched<h2>\n";
	
		if($new_pass eq $new_pass2)
		{
			my $enc = encrypString($new_pass);

#			print "encrypted binary: $enc\n";
			
			my $storedpassfile = 'pass.txt';
			open(my $fh, '>', $storedpassfile) or die "Could not open the pass file";
			print $fh "$enc";
			close $fh;

			print "New Password Updated\n";
			}
		else {
			print "New pass & Confirm Pass is not same";
			}

	}
	else{
			print "Old Pass & Stored Pass mismatch\n";
	}


sub encrypString {
        my $string = shift;
        my $cipher = Crypt::CBC->new(
                -key    => $KEY,
                -cipher => 'Blowfish',
                -padding => 'space',
                -add_header => 1
        );

        my $enc = $cipher->encrypt($string);
        return $enc;
}


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
