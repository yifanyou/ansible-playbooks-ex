from random import choice
import string,re
passwd_seed = string.digits + string.ascii_letters

def get_passwd(passwd_length=10):
	passwd = []
	while len(passwd) < passwd_length:
	    passwd.append(choice(passwd_seed))
	    password=''.join(passwd)
	password=password.replace("'","\\\'")
	password=password.replace('"','\\\"')
	return password

if __name__ == "__main__":
    print get_passwd()
