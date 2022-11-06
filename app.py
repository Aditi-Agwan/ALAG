
from flask import Flask, render_template, request
from sqlalchemy import true
from flask_mysqldb import MySQL
import yaml
app= Flask(__name__)

#Configure db
db = yaml.load(open('C:\\Users\\agwan\\Downloads\\Project\\Project\db.yaml'),Loader=yaml.Loader)
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/student')
def student():
  return render_template('student.html')

@app.route('/sign-up')
def signup():
    if request.method == 'POST':
        #fetch details from form
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO USERS(name,email) VALUES(%s,%s) ",(name,email))
        mysql.connection.commit()
        cur.close()
        return 'Success'
    return render_template('sign up.html')  

@app.route('/login')
def login():
    return render_template('login.html')  
if __name__ == '__main__': 
    app.run(debug=true)

    