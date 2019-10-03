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

#Registro de Boxeador
@app.route('/register/boxeador',methods=['GET','POST'])
def boxeador():
        msg=''
        cursor=mysql.connection.cursor()

        if request.method == 'GET':
            return render_template('register_boxer.html',title='Registro')

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

            if(sexo=='Masculino'):
                if(peso>'0' and peso<='47.63'):
                    division='1'
                elif (peso>='47.64' and peso<='48.99'):
                    division='2'
                elif (peso>='49.00' and peso<='50.35'):
                    division='3'
                elif (peso>='50.36' and peso<='51.71'):
                    division='4'
                elif (peso>='51.72' and peso<='53.52'):
                    division='5'
                elif (peso>='53.53' and peso<='55.34'):
                    division='6'
                elif (peso>='55.35' and peso<='57.15'):
                    division='7'
                elif (peso>='57.16' and peso<='58.97'):
                    division='8'
                elif (peso>='58.98' and peso<='61.23'):
                    division='9'
                elif (peso>='61.24' and peso<='63.50'):
                    division='10'
                elif (peso>='63.51' and peso<='66.68'):
                    division='11'
                elif (peso>='66.69' and peso<='69.85'):
                    division='12'
                elif (peso>='69.86' and peso<='73.03'):
                    division='13'
                elif (peso>='73.04' and peso<='76.20'):
                    division='14'
                elif (peso>='76.21' and peso<='79.38'):
                    division='15'
                elif (peso>='79.39' and peso<='90.72'):
                    division='16'
                elif (peso>='90.73' and peso<='300'):
                    division='17'
            else:
                if(peso>'0' and peso<='46.26'):
                    division='18'
                elif (peso>='46.27' and peso<='47.62'):
                    division='19'
                elif (peso>='47.63' and peso<='49.98'):
                    division='20'
                elif (peso>='49.99' and peso<='50.80'):
                    division='21'
                elif (peso>='50.81' and peso<='52.16'):
                    division='22'
                elif (peso>='52.17' and peso<='53.52'):
                    division='23'
                elif (peso>='53.53' and peso<='55.33'):
                    division='24'
                elif (peso>='53.34' and peso<='57.15'):
                    division='25'
                elif (peso>='57.16' and peso<='58.96'):
                    division='26'
                elif (peso>='58.97' and peso<='61.23'):
                    division='27'
                elif (peso>='61.24' and peso<='63.50'):
                    division='28'
                elif (peso>='63.51' and peso<='66.67'):
                    division='29'
                elif (peso>='66.68' and peso<='69.80'):
                    division='30'
                elif (peso>='69.81' and peso<='72.57'):
                    division='31'
                elif (peso>='72.58' and peso<='76.20'):
                    division='32'
                elif (peso>='76.21' and peso<='200'):
                    division='33'

            if (not nombre or not apellidoMat or not apellidoPat or not email
            or not password or not confirmPassword or not nacimiento or not telCasa
            or not sexo or not inicio or not calle or not numeroCalle or not colonia
            or not municipio or not estado or not tipoSangre or not guardia or not estatura
            or not peso or not numPeleas):
                msg='Favor de llenar todos los campos!'
                return render_template('register_boxer.html',msg=msg)
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                msg='correo no válido'
                return render_template('register_boxer.html',msg=msg)
            elif len(password)<8:
                 msg='La contraseña debe tener mínimo 8 caracteres'
                 return render_template('register_boxer.html',msg=msg)
            elif password != confirmPassword:
                msg='Las contraseñas no coinciden'
                return render_template('register_boxer.html',msg=msg)
            else:

                    cursor.execute(agregar_usuario,user_data)

                    #BOXEADORES

                    id_user=cursor.lastrowid
                    boxeador_data=(id_user,tipoSangre,guardia,estatura,peso,alias,numPeleas)
                    cursor.execute(agregar_boxeador,boxeador_data)
                    mysql.connection.commit()
                    cursor.close()
                    return redirect(url_for('home'))

#Registro de Entrenador
@app.route('/register/entrenador',methods=['GET','POST'])
def entrenador():
    msg=''
    cursor=mysql.connection.cursor()

    if request.method == 'GET':
        return render_template('register_trainer.html',title='Registro')

        cursor.execute("SELECT * from usuarios where email='" + email+ "'")
        data=cursor.fetchone()
        if data is None:
            pass
        else:
            msg='Ya existe el usuario!'
            return render_template('register_trainer.html',msg=msg)

    else:
        #USUARIOS
        agregar_usuario=("INSERT INTO usuarios (nombre,apellido_paterno,apellido_materno,email,"\
        "contrasena,fecha_nacimiento,telefono_casa,celular,sexo,calle,numero,colonia,fecha_registro,"\
        "municipio,estado)"\
        "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

        agregar_entrenador=("INSERT INTO entrenado (id_entrenador,no_peleas) VALUES (%s,%s)")

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
        numPeleas=userDetails['peleas']

        user_data=(nombre,apellidoPat,apellidoMat,email,password,nacimiento,telCasa,celular,sexo,calle,numeroCalle,colonia,inicio,municipio,estado)

        if (not nombre or not apellidoMat or not apellidoPat or not email
        or not password or not confirmPassword or not nacimiento or not telCasa
        or not sexo or not inicio or not calle or not numeroCalle or not colonia
        or not municipio or not estado or not numPeleas):
            msg='Favor de llenar todos los campos!'
            return render_template('register_trainer.html',msg=msg)
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg='correo no válido'
            return render_template('register_trainer.html',msg=msg)
        elif len(password)<8:
             msg='La contraseña debe tener mínimo 8 caracteres'
             return render_template('register_trainer.html',msg=msg)
        elif password != confirmPassword:
            msg='Las contraseñas no coinciden'
            return render_template('register_trainer.html',msg=msg)
        else:

                cursor.execute(agregar_usuario,user_data)
                #Entrenador
                id_entrenador=cursor.lastrowid
                print(id_entrenador)
                entrenador_data=(id_entrenador,numPeleas)
                cursor.execute(agregar_entrenador,entrenador_data)
                mysql.connection.commit()
                cursor.close()
                return redirect(url_for('home'))


#Registro de Referee=
@app.route('/register/referee')
def referee():
    return render_template('register_referee.html',title='Registro')

#Regstro de Dueño
@app.route('/register/dueno')
def dueno():
    return render_template('register_owner.html',title='Registro')



@app.route("/home")
def home():
    return render_template('home.html')


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html',title='Login')
    else:
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
