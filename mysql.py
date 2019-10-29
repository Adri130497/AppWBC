from flask import Flask, request,render_template, url_for, flash, redirect, session, g
from flaskext.mysql import MySQL
from flask_mysqldb import MySQL
from os import urandom
import re

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'wbc_final2'
app.config['MYSQL_HOST'] = 'localhost'
app.secret_key = urandom(24)



mysql = MySQL(app)

#Registro de Boxeador
@app.route('/register/boxeador',methods=['GET','POST'])
def boxeador():
        msg=''
        cursor=mysql.connection.cursor()

        if request.method == 'GET':
            return render_template('register_boxer.html', title='Registro')

        else:
            #USUARIOS
            agregar_usuario=("INSERT INTO usuarios (nombre,apellido_paterno,apellido_materno,email,"\
            "contrasena,fecha_nacimiento,telefono_casa,celular,sexo,calle,numero,colonia,fecha_registro,"\
            "municipio,cp,estado)"\
            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

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
            cp=userDetails['CP']
            estado=userDetails['estado']
            tipoSangre=userDetails['tipoSangre']
            guardia=userDetails['guardia']
            estatura=userDetails['estatura']
            peso=userDetails['peso']
            alias=userDetails['alias']
            numPeleas=userDetails['peleas']

            cursor.execute("SELECT * from usuarios where email='" + email+ "'")
            data=cursor.fetchone()
            if data is None:
                pass
            else:
                msg='Ya existe el usuario!'
                return render_template('register_referee.html',title='Registro',msg=msg)


            user_data=(nombre,apellidoPat,apellidoMat,email,password,nacimiento,telCasa,celular,sexo,calle,numeroCalle,colonia,inicio,municipio,cp,estado)

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
            or not municipio or not cp or not estado or not tipoSangre or not guardia or not estatura
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

    else:
        #USUARIOS
        agregar_usuario=("INSERT INTO usuarios (nombre,apellido_paterno,apellido_materno,email,"\
        "contrasena,fecha_nacimiento,telefono_casa,celular,sexo,calle,numero,colonia,fecha_registro,"\
        "municipio,cp,estado)"\
        "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

        agregar_entrenador=("INSERT INTO entrenado (id_entrenador,no_peleas,bandera_entrenador_manager) VALUES (%s,%s,%s)")

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
        cp=userDetails['CP']
        estado=userDetails['estado']
        numPeleas=userDetails['peleas']
        tipoEntrenador=userDetails['tipoEntrenador']

        cursor.execute("SELECT * from usuarios where email='" + email+ "'")
        data=cursor.fetchone()
        if data is None:
            pass
        else:
            msg='Ya existe el usuario!'
            return render_template('register_referee.html',title='Registro',msg=msg)

        user_data=(nombre,apellidoPat,apellidoMat,email,password,nacimiento,telCasa,celular,sexo,calle,numeroCalle,colonia,inicio,municipio,cp,estado)

        if (not nombre or not apellidoMat or not apellidoPat or not email
        or not password or not confirmPassword or not nacimiento or not telCasa
        or not sexo or not inicio or not calle or not numeroCalle or not colonia
        or not municipio or not cp or not estado or not numPeleas):
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
                entrenador_data=(id_entrenador,numPeleas,tipoEntrenador)
                cursor.execute(agregar_entrenador,entrenador_data)
                mysql.connection.commit()
                cursor.close()
                return redirect(url_for('home'))


#Registro de Referee=
@app.route('/register/referee',methods=['GET','POST'])
def referee():
    msg=''
    cursor=mysql.connection.cursor()

    if request.method == 'GET':
        return render_template('register_referee.html',title='Registro')


    else:
        #USUARIOS
        agregar_usuario=("INSERT INTO usuarios (nombre,apellido_paterno,apellido_materno,email,"\
        "contrasena,fecha_nacimiento,telefono_casa,celular,sexo,calle,numero,colonia,fecha_registro,"\
        "municipio,cp,estado)"\
        "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

        agregar_referi=("INSERT INTO referi_juez (id_referi_juez, bandera_referi_juez, estado_civil,"\
        "ocupacion, escolaridad, id_licencia, quien_expide, notas_licencia, fecha_expiracion_licencia, anios_experiencia)"\
        "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

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
        cp=userDetails['CP']
        estado=userDetails['estado']

        tipoReferee=userDetails['tipoReferee']
        estadoCivil=userDetails['edoCivil']
        ocupacion=userDetails['ocupacion']
        escolaridad=userDetails['escolaridad']
        idLicencia=userDetails['licencia']
        personaLicencia=userDetails['expedLicencia']
        notasSobreLicencia=userDetails['notasLicencia']
        fechaExpiracion=userDetails['expeditionDate']
        añosExperiencia=userDetails['experiencia']

        cursor.execute("SELECT * from usuarios where email='" + email+ "'")
        data=cursor.fetchone()
        if data is None:
            pass
        else:
            msg='Ya existe el usuario!'
            return render_template('register_referee.html',title='Registro',msg=msg)




        user_data=(nombre,apellidoPat,apellidoMat,email,password,nacimiento,telCasa,celular,sexo,calle,numeroCalle,colonia,inicio,municipio,cp,estado)

        if (not nombre or not apellidoMat or not apellidoPat or not email
        or not password or not confirmPassword or not nacimiento or not telCasa
        or not sexo or not inicio or not calle or not numeroCalle or not colonia
        or not municipio or not cp or not estado or not estadoCivil or not ocupacion or not escolaridad
        or not añosExperiencia):
            msg='Favor de llenar todos los campos!'
            return render_template('register_referee.html',title='Registro',msg=msg)
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg='correo no válido'
            return render_template('register_referee.html',title='Registro',msg=msg)
        elif len(password)<8:
             msg='La contraseña debe tener mínimo 8 caracteres'
             return render_template('register_referee.html',title='Registro',msg=msg)
        elif password != confirmPassword:
            msg='Las contraseñas no coinciden'
            return render_template('register_referee.html',title='Registro',msg=msg)
        else:
                cursor.execute(agregar_usuario,user_data)
                #Entrenador
                id_referi=cursor.lastrowid
                referi_data=(id_referi,tipoReferee,estadoCivil,ocupacion,escolaridad,idLicencia,personaLicencia,notasSobreLicencia,fechaExpiracion,añosExperiencia)
                cursor.execute(agregar_referi,referi_data)
                mysql.connection.commit()
                cursor.close()
                return redirect(url_for('home'))

#Registro dueños de Gimnasio
@app.route('/register/dueno',methods=['GET','POST'])
def dueno():
    msg=''
    cursor=mysql.connection.cursor()

    if request.method == 'GET':
        return render_template('register_owner.html',title='Registro')

    else:
        #USUARIOS
        agregar_usuario=("INSERT INTO usuarios (nombre,apellido_paterno,apellido_materno,email,"\
        "contrasena,fecha_nacimiento,telefono_casa,celular,sexo,calle,numero,colonia,fecha_registro,"\
        "municipio,cp, estado)"\
        "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

        agregar_gym=("INSERT INTO gyms (id_propietario, nombre, direccion,"\
        "ciudad, estado, alcaldia_municipio, cp, horario, telefono, email)"\
        "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

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
        cp=userDetails['CP']
        estado=userDetails['estado']

        nombreGym=userDetails['gymNombre']
        direccionGym=userDetails['gymDireccion']
        ciudadGym=userDetails['gymCiudad']
        estadoGym=userDetails['gymEstado']
        municipioGym=userDetails['gymAlcaldia']
        cpGym=userDetails['gymCP']
        horario=userDetails['gymHorario']
        telefono=userDetails['gymTelefono']
        emailGym=userDetails['gymEmail']

        cursor.execute("SELECT * from usuarios where email='" + email+ "'")
        data=cursor.fetchone()
        if data is None:
            pass
        else:
            msg='Ya existe el usuario!'
            return render_template('register_referee.html',title='Registro',msg=msg)


        user_data=(nombre,apellidoPat,apellidoMat,email,password,nacimiento,telCasa,celular,sexo,calle,numeroCalle,colonia,inicio,municipio,cp,estado)

        if (not nombre or not apellidoMat or not apellidoPat or not email
        or not password or not confirmPassword or not nacimiento or not telCasa
        or not sexo or not inicio or not calle or not numeroCalle or not colonia
        or not municipio or not cp or not estado or not nombreGym or not direccionGym or not ciudadGym
        or not estadoGym or not emailGym):
            msg='Favor de llenar todos los campos!'
            return render_template('register_owner.html',title='Registro')
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg='correo no válido'
            return render_template('register_owner.html',title='Registro')
        elif len(password)<8:
             msg='La contraseña debe tener mínimo 8 caracteres'
             return render_template('register_owner.html',title='Registro')
        elif password != confirmPassword:
            msg='Las contraseñas no coinciden'
            return render_template('register_owner.html',title='Registro')
        else:

                cursor.execute(agregar_usuario,user_data)
                #Entrenador
                id_gym=cursor.lastrowid
                gym_data=(id_gym,nombreGym,direccionGym,ciudadGym,estadoGym,municipioGym,cpGym,horario,telefono,emailGym)
                cursor.execute(agregar_gym,gym_data)
                mysql.connection.commit()
                cursor.close()
                return redirect(url_for('home'))

#Pantalla de Inicio
@app.route("/home")
def home():
    #return render_template('home.html',title='Home')
    if 'user' in session:
        name = request.args.get('name')
        id = request.args.get('id')
        return render_template('home.html',title='Home',name=name,id=id)
    else:
        return redirect(url_for('login'))

#Informacion Entrenadores
@app.route("/home/Entrenadores/<name>/<int:id>")
def Entrenadores(name,id):
    id = str(id)
    cur = mysql.connection.cursor()
    curr = mysql.connection.cursor()

    cur.execute("SELECT usuarios.id_usuario, usuarios.nombre, usuarios.apellido_paterno, usuarios.apellido_materno, entrenado.no_peleas, usuarios.celular FROM usuarios , entrenado where usuarios.id_usuario = entrenado.id")
    curr.execute("SELECT usuarios.id_usuario, usuarios.nombre, usuarios.apellido_paterno, usuarios.apellido_materno, entrenado.no_peleas, usuarios.celular FROM usuarios , entrenado where usuarios.id_usuario = entrenado.id_entrenador AND usuarios.id_usuario = '" + id + "' AND entrenado.id_entrenador = '" + id + "' ")

    data = cur.fetchall()
    data2 = curr.fetchall()

    cur.close()
    return render_template('entrenadores.html',entrenador = data2, entrenadores = data, name=name,id=id)

#Informacion Gimnasios
@app.route("/home/Gimnasios/<name>/<int:id>")
def Gimnasios(name,id):
    id = str(id)
    cur = mysql.connection.cursor()
    curr = mysql.connection.cursor()
    cur.execute("SELECT gyms.id_gym, gyms.nombre, gyms.direccion, gyms.ciudad, gyms.estado, gyms.horario, gyms.telefono FROM gyms")
    curr.execute("SELECT gyms.id_gym, gyms.nombre, gyms.direccion, gyms.ciudad, gyms.estado, gyms.horario, gyms.telefono FROM gyms WHERE gyms.id_gym = '" + id+ "'")

    data = cur.fetchall()
    data2 = curr.fetchall()
    cur.close()

    return render_template('gimnasios.html',gym = data2, gimnasios= data,name=name,  id=id)

#Informacion Boxeadores
@app.route("/home/Boxeadores/<name>/<int:id>")
def Boxeadores(name,id):
    id = str(id)

    cur = mysql.connection.cursor()
    curr = mysql.connection.cursor()

    boxeadores = ("SELECT usuarios.id_usuario, usuarios.nombre, usuarios.apellido_paterno, boxeadores.alias, boxeadores.guardia, boxeadores.num_peleas, boxeadores.estatura, boxeadores.peso FROM usuarios, boxeadores where usuarios.id_usuario = boxeadores.id_boxeador")
    boxeador = ("SELECT usuarios.id_usuario, usuarios.nombre, usuarios.apellido_paterno, boxeadores.alias, boxeadores.guardia, boxeadores.num_peleas, boxeadores.estatura, boxeadores.peso FROM usuarios, boxeadores where usuarios.id_usuario = boxeadores.id_boxeador AND usuarios.id_usuario = '" + id+ "' AND boxeadores.id_boxeador = '" + id+ "'")

    cur.execute(boxeadores)
    curr.execute(boxeador)

    data = cur.fetchall()
    data2 = curr.fetchall()
    cur.close()

    return render_template('boxeadores.html',boxeadores = data, boxeador = data2, name=name, id=id)


#Login
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html',title='Login')
    else:
            msg='Usuario o Contraseña Incorrecta!'
            name=''
            id=''
            username=request.form['user']
            name=username
            password=request.form['pass']
            session['user'] = request.form['user']

            cursor=mysql.connect.cursor()
            cursor.execute("SELECT * from usuarios where email='" + username + "'and contrasena='" + password + "'")
            data=cursor.fetchone()
            if data is None:
                return render_template('login.html',msg=msg)
            else:
                cursor.execute("SELECT nombre from usuarios where email='" + username + "'")
                name=cursor.fetchone()
                cursor.execute("SELECT id_usuario from usuarios where email='" + username + "'")
                id=cursor.fetchone()
                return redirect(url_for('home',name=name,id=id))

#Template Registro
@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html',title='Registro')

#logout
@app.route("/logout")
def logout():
    session.pop('user')
    session.clear()
    return redirect(url_for('index'))

#Registro de Entrenamientos
@app.route("/home/RegistroEntrenamientos/<name>/<int:id>",methods=['GET','POST'])
def RegistroEntrena(name, id):


    return render_template('registro_entrenamientos.html', name=name, id=id)

#Registro de Peleas
@app.route("/home/RegistroPeleas/<name>/<int:id>",methods=['GET','POST'])
def RegistroPeleas(name,id):
    msg=''
    cursor=mysql.connection.cursor()
    registerData=list()
    if request.method == 'GET':
        return render_template('registro_Peleas.html',title='Registro Peleas')
    else:
        userDetails= request.form
        checkbox_box1=request.form.get('bandera_boxeador1')
        checkbox_box2=request.form.get('bandera_boxeador2')
        checkbox_referi=request.form.get('bandera_referi')
        checkbox_gym=request.form.get('bandera_gym')


        #Datos de la peleas
        division_pelea=userDetails['division']
        ganador=userDetails['ganador']
        resultado_pelea=userDetails['resultado_pelea']
        rounds=userDetails['rounds']
        notas=userDetails['notas']
        fecha_pelea=userDetails['fecha_pelea']


        registerData.append(division_pelea)
        registerData.append(ganador)
        registerData.append(resultado_pelea)
        registerData.append(ganador)
        registerData.append(notas)
        registerData.append(fecha_pelea)




        if checkbox_box1:
            id_box1=userDetails['id_boxeador1']
            pesoDBbox1=cursor.execute("SELECT peso FROM boxeadores where  id_boxeador='" + id_box1+ "'")
            dataPeso1=cursor.fetchone()
            nombreDBbox1=cursor.execute("SELECT nombre FROM usuarios where id_usuario='"+id_box1+"'")
            dataNombre1=cursor.fetchone()

            registerData.append(id_box1)
            registerData.append(dataPeso1)
            registerData.append(dataNombre1)

            print(registerData)
            pass
        else:
            nombre_box1=userDetails['nombre_boxeador1']
            correo_box1=userDetails['correo_boxeador1']
            peso_box1=userDetails['peso_boxeador_1']

            registerData.append(nombre_box1)
            registerData.append(correo_box1)
            registerData.append(peso_box1)
            print(registerData)
            pass

        if checkbox_box2:
            id_box2=userDetails['id_boxeador2']
            pesoDBbox2=cursor.execute("SELECT peso FROM boxeadores where  id_boxeador='" + id_box2+ "'")
            dataPeso2=cursor.fetchone()
            nombreDBbox2=cursor.execute("SELECT nombre FROM usuarios where id_usuario='"+id_box2+"'")
            dataNombre2=cursor.fetchone()
            print(dataPeso2)
            print(dataNombre2)
            registerData.append(id_box2)
            registerData.append(dataPeso2)
            registerData.append(dataNombre2)

            print(registerData)
            pass
        else:
            nombre_box2=userDetails['nombre_boxeador2']
            correo_box2=userDetails['correo_boxeador2']
            peso_box2=userDetails['peso_boxeador_2']

            registerData.append(nombre_box2)
            registerData.append(correo_box2)
            registerData.append(peso_box2)
            print(registerData)
            pass

        if checkbox_referi:
            id_referi=userDetails['id_referi']
            nombreDBReferi=cursor.execute("SELECT nombre FROM usuarios where id_usuario='"+id_referi+"'")
            dataNombre_referi=cursor.fetchone()
            registerData.append(id_referi)
            registerData.append(dataNombre_referi)
            print(registerData)
            pass
        else:
            nombre_referi=userDetails['nombre_referi']
            registerData.append(nombre_referi)
            pass

        if checkbox_gym:
            id_gym=userDetails['id_gym']
            nombreDBgym=cursor.execute("SELECT nombre FROM gyms where id_gym='" + id_gym+ "'")
            dataNombreGym=cursor.fetchone()
            estadoDBgym=cursor.execute("SELECT estado FROM gyms where id_gym='"+id_gym+"'")
            dataEstadoGym=cursor.fetchone()

            registerData.append(id_gym)
            registerData.append(dataNombreGym)
            registerData.append(dataEstadoGym)
            print(registerData)
            return "Success"
        else:
            nombre_gym=userDetails['nombre_gym']
            estado_gym=userDetails['estado_gym']
            registerData.append(nombre_gym)
            registerData.append(estado_gym)
            return "Success"

        


#Redireccion a login
@app.route('/',methods=['GET','POST'])
def mainPage():
        return redirect(url_for('login'))


if __name__=="__main__":
    app.run(debug=True)
