##################################################################
#This is the main script for this program. Running this
#assumes that you have run the update_table script already.
#
#If you have not run the update_table script this will not work
#as it is dependent on that script.
##################################################################

from ssh_function import login
from compare_function import compare

#pushbullet api key
api = 'pushbullet api key goes here'

#login info
host = 'host address'
user = 'username'
password = 'password'
command = 'command \n'

#save command output to variable
current_dhcp = login(host,user,password,command)

#writes output to text file
file = open("current.txt","w")
file.write(str(current_dhcp))
file.close()

#initialize the text file variable
to_compare = "current.txt"

#call the compare funcion to compare to current table
#and send the pushbullet notification
compare(to_compare, api)
