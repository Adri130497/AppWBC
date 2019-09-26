from flask import Flask, request,render_template, url_for, flash, redirect
from flaskext.mysql import MySQL
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'wbc_final'
app.config['MYSQL_HOST'] = 'localhost'
app.config['SECRET_KEY'] = '6023611b18e90c93803a8dd783540183'

mysql = MySQL(app)

@app.route('/login')
def myform():
    return render_template('login.html')

@app.route("/home")
def home():
    return render_template('home.html')


@app.route('/login',methods=['POST'])
def login():
    username=request.form['user']
    password=request.form['pass']
    cursor=mysql.connect.cursor()
    cursor.execute("SELECT * from usuarios where email='" + username + "'and contrasena='" + password + "'")
    data=cursor.fetchone()
    if data is None:
        flash("Usuario o Contraseña Incorrectos")
    else:
        return redirect(url_for('home'))


@app.route('/register',methods=['GET', 'POST'])
def register():
     return render_template('register.html',title='Registro')
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         if form.email.data == 'u' and form.password.data== 'p':
#             return redirect(url_for('home'))
#     return render_template('login.html',title='Login', form=form)



if __name__=="__main__":
    app.run(debug=True)
