# dhcp-checker
This script logs into a host via ssh and runs a command to show the dhcp
table. It then stores the table into two text files, one for a base and one
as a current table, and compares them. If there are clients on the current
table that are not on the base table, it well send a pushbullet notification
and print it on the terminal.

Dependencies:
  -Paramiko Library (for ssh)
  -Pushbullet Library (to send notification)

--- Before running, edit the host info in both main and update scripts ---

--- You must run the update_table.py script before running the main script ---
