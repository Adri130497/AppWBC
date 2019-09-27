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

@app.route('/login',methods=['POST'])
def add_boxer():
    nombre=request.form['nombre-boxeador']
    apellido_pat=request.form['apellido-pat-boxeador']
    apellido_mat=request.form['apellido-mat-boxeador']
    email=request.form['email']
    password=request.form['password']
    birthDate=request.form['birthDate']
    tel_casa=request.form['tel-casa']
    tel_celular=request.form['tel-celular']
    fecha_regis=request.form['fecha-regis']
    calle=request.form['calle-boxeador']
    calle_num=request.form['calle-num-boxeador']
    colonia=request.form['colonia-boxeador']
    municipio=request.form['municipio-boxeador']
    cp=request.form['cp-boxeador']
    estado=request.form['estado-boxeador']
    foto=request.form['foto-boxeador']
    guardia=request.form['guardia-boxeador']
    sangre=request.form['sangre-boxeador']
    estatura=request.form['estatura-boxeador']
    peso=request.form['peso-boxeador']
    alias=request.form['alias-boxeador']
    peleas=request.form['peleas-boxeador']
    cursor=mysql.connect.cursor()
    cursor.execute("INSERT INTO users (nombre,apellido_paterno,apellido_materno,fecha_nacimiento,telefono_casa,celular,email,contrasena,fecha_registro,calle,numero,colonia,municipio,cp,estado,foto) values ("nombre,apellido_pat,apellido_mat,birthDate,tel_casa,tel_celularemail,password,fecha_regis,calle,calle_num,colonia,municipio,cp,estado,foto")")
    cursor.execute("INSERT INTO boxeadores (guardia,tipo_sangre,estatura,peso,alias,num_peleas) values ("guardia,sangre,estatura,peso,alias,peleas")")
    data=cursor.fetchone()
    if data is None:
        flash("Llene los campos obligatorios")
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
