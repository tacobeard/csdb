import ticket_data, pymysql

# Open database connection
db = pymysql.connect(host='localhost',
                       user='testuser',
                       passwd='test123',
                       db='csdb',
                       charset='utf8')

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """SET SESSION sql_mode = ""; INSERT INTO tickets(player_id, platform, location, ticket_id,ticket_tags, group_id, ticket_created, last_update) VALUES"""+ticket_data.data+';'
try:
   # Execute the SQL command
   cursor.execute(sql)
   db.commit()
   print('Database updated')
except pymysql.ProgrammingError as p:
   db.rollback()   
   print ("Caught a Programming Error:")
   print (p)
except pymysql.DataError as d:
   db.rollback() 
   print ("Caught a Data Error:")
   print (d)
except pymysql.IntegrityError as i:
   db.rollback() 
   print ("Caught an Integrity Error:")
   print (i)
except pymysql.NotSupportedError as n:
   db.rollback() 
   print ("Caught a NotSupported Error:")
   print (n)
except pymysql.OperationalError as o:
   db.rollback() 
   print ("Caught an Operational Error:")
   print (o)
except pymysql.InternalError as n:
   db.rollback() 
   print ("Caught an Internal Error:")
   print (n)
    
    
# disconnect from server
db.close()
