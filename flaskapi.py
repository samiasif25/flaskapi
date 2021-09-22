from flask import Flask, jsonify,render_template, request
from flask_mysqldb import MySQL
import pymysql

app= Flask(__name__)
app.secret_key= " "

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "samiasif@123"
app.config["MYSQL_DB"] =  "emoloyee"

db=MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/app/api/employee/all', methods=['GET'])
def show():
    cursor=db.connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM employee")
    info=cursor.fetchall()

    return jsonify(info)

if __name__=='__main__':
    app.run(debug=True)




