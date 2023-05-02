from flask import Blueprint, render_template , request ,redirect, url_for, flash, g
from routes.auth import user_login_required, session
from datetime import datetime
from utils.db import get_db_connection



view_task = Blueprint('Tarea',__name__)


@view_task.route("/Tarea")
@user_login_required
def home():
    conn  = get_db_connection()

    cursor = conn .cursor()
    cursor.execute("SELECT * FROM alumno")
    data_alumno = cursor.fetchall()

    cursor.execute("SELECT * FROM grupo")
    data_grupo = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return render_template("task.html", alumnos = data_alumno, grupos = data_grupo)


@view_task.route("/add_task_alumno", methods=['GET', 'POST'])
def add_task_alumno():
    if request.method == 'POST':
        conn  = get_db_connection()

        tiempo = request.form['tiempo']
        fecha_str = request.form['fecha']
        tema= request.form['tema']
        descripcion= request.form['descripcion']
        alumno_id = request.form['alumnoSelect']
        profesor_id = session['profesor_id']

        fecha = datetime.strptime(fecha_str , '%d-%m-%Y')
        
        cursor = conn .cursor()
        cursor.execute("INSERT INTO task_alumno(tema, descripcion, tiempo, fecha, alumno_id,profesor_id) VALUES (%s, %s,  %s, %s, %s, %s)", (tema, descripcion, tiempo, fecha, alumno_id,profesor_id))

        cursor.execute("INSERT INTO data_task_profesor(tema, descripcion, tiempo, fecha, id_alumno_grupo,profesor_id) VALUES (%s, %s,  %s, %s, %s, %s)",(tema, descripcion, tiempo, fecha, alumno_id,profesor_id))
        
        cursor.execute("UPDATE profesor SET tiempo_clase = tiempo_clase + %s WHERE id = %s", (tiempo, profesor_id))
        cursor.execute("UPDATE profesor SET num_tareas = num_tareas + 1 WHERE id = %s", (profesor_id,))
        cursor.close()

        conn.commit()
        conn.close()
        flash('¡Dato guardado correctamente!')
        return redirect(url_for("Tarea.home"))


@view_task.route("/add_task_grupo", methods=['GET', 'POST'])
def add_task_grupo():
    if request.method == 'POST':
        conn  = get_db_connection()

        tiempo = request.form['tiempo']
        fecha_str = request.form['fecha']

        tema= request.form['tema']
        descripcion= request.form['descripcion']
        grupo_id = request.form['grupoSelect']
        profesor_id = session['profesor_id']

        fecha = datetime.strptime(fecha_str , '%d-%m-%Y')
        
        cursor = conn .cursor()
        cursor.execute("INSERT INTO task_grupo(tema, descripcion, tiempo, fecha, grupo_id, profesor_id) VALUES (%s, %s,  %s, %s, %s, %s)", (tema, descripcion, tiempo, fecha, grupo_id, profesor_id))

        cursor.execute("INSERT INTO data_task_profesor(tema, descripcion, tiempo, fecha, id_alumno_grupo,profesor_id) VALUES (%s, %s,  %s, %s, %s, %s)",(tema, descripcion, tiempo, fecha, grupo_id, profesor_id))

        cursor.execute("UPDATE profesor SET tiempo_clase = tiempo_clase + %s WHERE id = %s", (tiempo, profesor_id))
        cursor.execute("UPDATE profesor SET num_tareas = num_tareas + 1 WHERE id = %s", (profesor_id,))
        cursor.close()
        conn.commit()
        conn.close()
        flash('¡Dato guardado correctamente!')
        return redirect(url_for("Tarea.home"))