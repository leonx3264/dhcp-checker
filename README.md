# dhcp-checker
This script logs into a host via ssh and runs a command to show the dhcp
table. It then stores the table into two text files, one for a base and one
as a current table, and compares them. If there are clients on the current
table that are not on the base table, it well send a pushbullet notification
and print it on the terminal.

--- You must run the update_table.py script before running the main script ---
