from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)

@app.route('/')
def index():
   return render_template("index.html")



# Crud Puesto

@app.route('/puesto')
def puesto():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh' )
    cursor = conn.cursor()
    cursor.execute('select idPuesto, nomPuesto from puesto order by idPuesto')
    datos = cursor.fetchall()
    return render_template("puesto.html", pue=datos, dat=' ', catArea=' ', catEdoCivil=' ', catEscolaridad=' ', catGradoAvance=' ', catCarrera=' ', catIdioma=' ', catHabilidad=' ')

@app.route('/puesto_fdetalle/<string:idP>', methods=['GET'])
def puesto_fdetalle(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('select idPuesto, nomPuesto from puesto order by idPuesto')
    datos = cursor.fetchall()
    cursor.execute('select idPuesto,codPuesto,nomPuesto,''reqFisicos,reqPsicologicos,responsabilidades,condicionesTrabajo from puesto where idPuesto = %s', (idP))
    dato = cursor.fetchall()


    return render_template("puesto.html", pue = datos, dat=dato[0])

@app.route('/puesto_borrar/<string:idP>')
def puesto_borrar(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('delete from puesto where idPuesto = %s',(idP))
    conn.commit()

    return redirect(url_for('puesto'))

@app.route('/puesto_agregar')
def puesto_agregar():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    #cursor.execute('select idArea, descripcion from area ')
    #datos1 = cursor.fetchall()

    return render_template("puesto_agr.html" )#, catArea=datos1, catEdoCivil=datos2,catEscolaridad=datos3, catGradoAvance=datos4, catCarrera=datos5, catIdioma=datos6,catHabilidad=datos7)


@app.route('/puesto_fagrega', methods=['POST'])
def puesto_fagrega():
    if request.method == 'POST':

        codP = request.form['codPuesto']
        nomP = request.form['nomPuesto']
        reqF = request.form['reqFisicos']
        reqP = request.form['reqPsicologicos']
        resp = request.form['responsabilidades']
        conT = request.form['condicionesTrabajo']

    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('insert into puesto (codPuesto,nomPuesto,''reqFisicos,reqPsicologicos,responsabilidades,condicionesTrabajo)values(%s,%s,%s,%s,%s,%s)',(codP, nomP, reqF, reqP, resp, conT))
    conn.commit()
    cursor.execute('select idPuesto, nomPuesto from puesto where idPuesto=(select max(idPuesto) from puesto) ')
    dato=cursor.fetchall()
    return redirect(url_for('puesto', dat=dato[0]))


#puesto editar
@app.route('/puesto_editar/<string:idP>')
def puesto_editar(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('select idPuesto,codPuesto,nomPuesto,''reqFisicos,reqPsicologicos,responsabilidades,condicionesTrabajo from puesto where idPuesto = %s', (idP))
    dato = cursor.fetchall()

    return render_template("puesto_edi.html", dat=dato[0])


@app.route('/puesto_fedita/<string:idP>', methods=['POST'])
def puesto_fedita(idP):
    if request.method == 'POST':
        if 'idGradoAvance' in request.form:
            idGA = request.form['idGradoAvance']
        else:
            idGA = '1'
        if 'idCarrera' in request.form:
            idCa = request.form['idCarrera']
        else:
            idCa = '1'
        codP = request.form['codPuesto']

        nomP = request.form['nomPuesto']

        reqF = request.form['reqFisicos']
        reqP = request.form['reqPsicologicos']
        resp = request.form['responsabilidades']
        conT = request.form['condicionesTrabajo']

    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('update puesto set codPuesto = %s, nomPuesto = %s, reqFisicos = %s, reqPsicologicos = %s, responsabilidades = %s, '
                   'condicionesTrabajo = %s where idPuesto = %s', (codP, nomP, reqF, reqP, resp, conT, idP))
    conn.commit()
    return redirect(url_for('puesto'))






if __name__ == "__main__":
    app.run(debug=True)

