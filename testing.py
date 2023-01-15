import mysql.connector

# Connect to the database
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="employee"
)

# Create a cursor
cursor = cnx.cursor()

# Execute a SELECT command
cursor.execute("SELECT 1")

# Fetch the result
result = cursor.fetchone()

# Close the connection
cnx.close()

# Print the result
print(result)

