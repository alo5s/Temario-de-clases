from flask import Blueprint, render_template
from routes.auth import user_login_required
from utils.db import get_db_connection


view_students = Blueprint('Estudiantes',__name__)


@view_students.route("/Estudiantes")
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
    return render_template("students.html", alumnos=data_alumno, grupos=data_grupo)

@view_students.route("/task_view_alumno/<id>")
def task_view_alumno(id):
    conn  = get_db_connection()
    cursor = conn .cursor()

    cursor.execute("SELECT * FROM alumno WHERE id= %s",(id,))
    data_id = cursor.fetchall()

    cursor.execute("SELECT * FROM task_alumno WHERE alumno_id= %s",(id,))
    data_task = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return render_template("task_view/task_view_alumno.html", data_alumnos = data_id, alumno_task = data_task)


@view_students.route("/task_view_grupo/<id>")
def task_view_grupo(id):
    conn  = get_db_connection()
    cursor = conn .cursor()

    cursor.execute("SELECT * FROM grupo WHERE id= %s",(id,)) 
    data_id = cursor.fetchall()

    cursor.execute("SELECT * FROM task_grupo WHERE grupo_id= %s",(id,))
    data_task = cursor.fetchall()

    cursor.close()
    conn.close()
    return render_template("task_view/task_view_grupo.html", data_grupo = data_id, grupo_task = data_task )
