from flask import Flask, jsonify,render_template, request 
from flask_mysqldb import MySQL
import sys
 
app = Flask(__name__, template_folder='template')
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'hitesh'
app.config['MYSQL_PASSWORD'] = 'Hitesh@008'
app.config['MYSQL_DB'] = 'employee'
 
mysql = MySQL(app)
mysql.init_app(app)


 
@app.route('/')
def HomePage():
    return render_template('Test.html')

@app.route('/hi')
def Function():
  
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Persons")
    data = cur.fetchall()
    cur.close()
    data1 = jsonify(data)
    print(data)
    print(data1)


    return render_template('Test.html')
 
app.run(debug=True, host='localhost', port=5000)