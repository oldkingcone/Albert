#Still In Dev 

from pwn import *

host = str(input("[ + ] Please input Host [ + ]\n->"))
user = str(input("[ + ] Please input User [ + ]\n->"))
password = str(input("[ + ] Please input Password [ + ]\n->"))

shell = ssh(host='host', user='user', password='password')

# Show basic command syntax
log.info("username: %s" % shell.whoami())
log.info("pwd: %s" % shell.pwd())

# Show automatic working directories
shell.set_working_directory()
log.info("pwd: %r" % shell.pwd())

shell.upload_data(<INSERT PAYLOAD>)

shell.gcc([<GCC COMPLIATION OF C FILE])

print(shell['./<NAME>'])

# Show off the interactive shell
shell.interactive()

