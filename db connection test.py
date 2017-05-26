import pymysql, logging, datetime

now = datetime.datetime.now()
log = r'test_log.txt'

try:
    # Open database connection
    db = pymysql.connect("localhost","testuser","test123","TESTDB" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
 
    # execute SQL query using execute() method.
    cursor.execute("SELECT VERSION()")

    # Fetch a single row using fetchone() method.
    data = cursor.fetchone()

    print ("Database version : %s " % data)

    # disconnect from server
    db.close()

except:
    # Establish error log file, set logging level
    logging.basicConfig(filename=log,level=logging.WARNING)

    # Define log message
    logging.warning(now.strftime("%c ")+'Failure to connect to database')

    # Print error log to console
    print ('The following message has been written to the error log:'+'\n'+now.strftime("%c ")+'Failure to connect to database')
