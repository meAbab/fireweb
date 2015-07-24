# fireweb

One of my long time client, often taking different solution if many different projects and paying me with very good money,
is often travelling here and there. Thus required for him to login from different source IP from different network type.

That's let me to inspire learn perl and program this package. 

I must say, that its not properly secure - as you need to put ssl and encryption technique also not upto par.
As program Source code contain the key. So better use ssl and use random value and updated hash algorithm.

In mean time, if I'm able to a save time dispite hunting food and cloths, I'll update it.


REQUIREMENT
--------------------
1. You need perl and perl-cgi enabled in your machine and apache.
2. Need Crypt:CBC - use CPAN to install it

          # perl -MCPAN -e shell
          > install Crypt::CBC

3. Default Pass is - khubGopon
4. You need to change your sudoers file [or use visudo] to allow apache user to run iptables.

          ## Allow root to run any commands anywhere
          root    ALL=(ALL)       ALL
          user-foo        ALL= NOPASSWD: /sbin/iptables

5. And follow all other settings that need to run a perl script, i.e. let file executable, giving right owner/group(ship) etc.
