#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Jhonathan Davi A.K.A jh00nbr / jhoon@rtfm-ctf.org / jhonathandavi.com.br
# Twitter: @jh00nbr
# Insightl4b: lab.insightsecurity.com.br
# CTF-Team: rtfm-ctf.org

# Convert the passwords of the rockyou wordlist to md5

from hashlib import md5
import sys

banner = '''

           _     _
          ( |\  //|
           \|\\//\|
             /66\\			CTF-Tool - Convert the passwords of the rockyou wordlist to md5
            ((_v.)					    Team: rtfm-ctf.org
             > "<       

'''


def rock2md5(passwd):
    with open("./rockyou_md5.txt","a") as pwd_md5:
		    pwd_md5.write(passwd+"\n")
	  pwd_md5.close()
	  return True


if __name__ == '__main__':
    with open("/usr/share/wordlists/rockyou.txt","r") as pwd:
		    print banner,'\n'
		    for pw in pwd.readlines():
			      passwd = pw.strip()
			      sys.stdout.write(''.join('\r' + " [!] Hashando os passwords: " + md5(passwd).hexdigest(),))
			      rock2md5(md5(passwd).hexdigest()+":" + passwd)
			      sys.stdout.flush()
