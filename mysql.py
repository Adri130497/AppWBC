from flask import Flask, request,render_template
from flaskext.mysql import MySQL
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'wbc_final'
app.config['MYSQL_HOST'] = 'localhost'
mysql = MySQL(app)

@app.route('/')
def myform():
    return render_template('from_ex.html')

@app.route('/',methods=['POST'])
def Authenticate():
    username=request.form['u']
    password=request.form['p']
    cursor=mysql.connect.cursor()
    cursor.execute("SELECT * from usuarios where email='" + username + "'and contrasena='" + password + "'")
    data=cursor.fetchone()
    if data is None:
        return "Wrong username or password"
    else:
        return render_template('home.html')

if __name__=="__main__":
    app.run(debug=True)
