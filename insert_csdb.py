import ticket_data, pymysql

# Open database connection
db = pymysql.connect("localhost","testuser","test123","csdb" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO tickets(platform, player_id, location, ticket_id,
ticket_tags, group, ticket_created, last_update)
   VALUES("""+ticket_data.data+')'
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()
