from flask import Flask, request,render_template, url_for, flash, redirect
from flaskext.mysql import MySQL
from flask_mysqldb import MySQL
import re

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'wbc_final'
app.config['MYSQL_HOST'] = 'localhost'
app.config['SECRET_KEY'] = '6023611b18e90c93803a8dd783540183'

mysql = MySQL(app)

@app.route('/register/boxeador',methods=['GET','POST'])
def boxeador():
        msg=''
        cursor=mysql.connection.cursor()

        if request.method == 'GET':
            return render_template('register_boxer.html',title='Registro')
            flagBox=request.form.get('flagB')

            cursor.execute("SELECT * from usuarios where email='" + email+ "'")
            data=cursor.fetchone()
            if data is None:
                pass
            else:
                msg='Ya existe el usuario!'
                return render_template('register.html',msg=msg)

        else:
            #USUARIOS
            agregar_usuario=("INSERT INTO usuarios (nombre,apellido_paterno,apellido_materno,email,"\
            "contrasena,fecha_nacimiento,telefono_casa,celular,sexo,calle,numero,colonia,fecha_registro,"\
            "municipio,estado)"\
            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

            agregar_boxeador=("INSERT INTO boxeadores (id_boxeador,tipo_sangre,guardia,estatura,peso,alias,num_peleas)"\
            "VALUES (%s,%s,%s,%s,%s,%s,%s)")

            userDetails= request.form
            nombre=userDetails['nombre']
            apellidoPat=userDetails['apellidoPat']
            apellidoMat=userDetails['apellidoMat']
            email=userDetails['email']
            password=userDetails['password']
            confirmPassword=userDetails['confirmPassword']
            nacimiento=userDetails['birthDate']
            telCasa=userDetails['telCasa']
            celular=userDetails['celular']
            sexo=userDetails['sexo']
            inicio=userDetails['inicio']
            calle=userDetails['calle']
            numeroCalle=userDetails['numeroCalle']
            colonia=userDetails['colonia']
            municipio=userDetails['municipio']
            estado=userDetails['estado']
            tipoSangre=userDetails['tipoSangre']
            guardia=userDetails['guardia']
            estatura=userDetails['estatura']
            peso=userDetails['peso']
            alias=userDetails['alias']
            numPeleas=userDetails['peleas']

            user_data=(nombre,apellidoPat,apellidoMat,email,password,nacimiento,telCasa,celular,sexo,calle,numeroCalle,colonia,inicio,municipio,estado)

            if (not nombre or not apellidoMat or not apellidoPat or not email
            or not password or not confirmPassword or not nacimiento or not telCasa
            or not sexo or not inicio or not calle or not numeroCalle or not colonia
            or not municipio or not estado or not tipoSangre or not guardia or not estatura
            or not peso or not numPeleas):
                msg='Favor de llenar todos los campos!'
                return render_template('register.html',msg=msg)
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                msg='correo no válido'
                return render_template('register.html',msg=msg)
            elif len(password)<8:
                 msg='La contraseña debe tener mínimo 8 caracteres'
                 return render_template('register.html',msg=msg)
            elif password != confirmPassword:
                msg='Las contraseñas no coinciden'
                return render_template('register.html',msg=msg)
            else:

                    cursor.execute(agregar_usuario,user_data)

                    #BOXEADORES

                    id_user=cursor.execute("SELECT id_usuario FROM usuarios WHERE email ='"+ email + "'")
                    boxeador_data=(id_user,tipoSangre,guardia,estatura,peso,alias,numPeleas)


                    cursor.execute(agregar_boxeador,boxeador_data)
                    mysql.connection.commit()
                    cursor.close()
                    return redirect(url_for('home'))

@app.route('/register/entrenador')
def entrenador():
    return render_template('register_trainer.html',title='Registro')

@app.route('/register/referee')
def referee():
    return render_template('register_referee.html',title='Registro')

@app.route('/register/dueno')
def dueno():
    return render_template('register_owner.html',title='Registro')

@app.route('/login')
def myform():
    return render_template('login.html')

@app.route("/home")
def home():
    return render_template('home.html')


@app.route('/login',methods=['POST'])
def login():
    msg='Usuario o Contraseña Incorrecta!'
    username=request.form['user']
    password=request.form['pass']
    cursor=mysql.connect.cursor()
    cursor.execute("SELECT * from usuarios where email='" + username + "'and contrasena='" + password + "'")
    data=cursor.fetchone()
    if data is None:
        return render_template('login.html',msg=msg)
    else:
        return redirect(url_for('home'))


@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html',title='Registro')




if __name__=="__main__":
    app.run(debug=True)
