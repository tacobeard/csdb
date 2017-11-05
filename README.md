# csdb
A Python driven MySQL database that queries and stores data from the Zendesk API

As of 06/21/2017 the project needs ticket_data.py and insert_csdb.py in the same directory to work.  The files also require a file containing a single Unix timestamp, 'export_time.txt'.  This file is used to store the time of last export, which is used as the beginning time that is queried the next time the script runs, thus ensuring accurate data.  Finally, 'zdcreds.py' is needed and should contain login credentials as prescribed in the Zenpy documentation.
