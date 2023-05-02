from flask import Blueprint, render_template , request ,redirect, flash,url_for, session
from routes.auth import admin_login_required
from utils.db import get_db_connection

view_admin = Blueprint('admin',__name__)


@view_admin.route("/admin")
@admin_login_required
def home():
    conn  = get_db_connection()
    cursor = conn .cursor()

    cursor.execute("SELECT * FROM profesor ")
    data_profe= cursor.fetchall()

    cursor.execute("SELECT * FROM alumno")
    data_alumno = cursor.fetchall()

    cursor.execute("SELECT * FROM grupo")
    data_grupo = cursor.fetchall()
    
    cursor.close()
    conn.close()

    return render_template("/admin_view/admin_home.html", profes = data_profe ,alumnos=data_alumno, grupos=data_grupo)



@view_admin.route("/add_profe",  methods=["POST"])
def add_porfesor():
    if request.method == 'POST':
        conn  = get_db_connection()
        cursor = conn .cursor()

        username = request.form['username']
        contraseña = request.form['password']
        
        cursor.execute("INSERT INTO profesor (username, contraseña) VALUES (%s, %s)", (username, contraseña))
        conn.commit()
        
        cursor.close()
        conn.close()
        flash('¡Profesor Agregado correctamente!')
        return redirect(url_for("admin.home"))

@view_admin.route("/delet-profesor/<id>")
def delete_profesor(id):
    conn  = get_db_connection()
    cursor = conn .cursor()
    cursor.execute("DELETE FROM profesor WHERE id= %s",(id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(request.referrer)
    #return redirect(url_for("admin.home"))


@view_admin.route("/add_estudian",  methods=["POST"])
def add_estudian():
    if request.method == 'POST':
        conn  = get_db_connection()
        cursor = conn .cursor()

        nombre = request.form['nombre']
        apellido = request.form['apellido']
        
        cursor.execute("INSERT INTO alumno (nombre, apellido) VALUES (%s, %s)", (nombre, apellido))
        conn.commit()

        cursor.close()
        conn.close()
        flash('¡Estudiante Agregado correctamente!')
        return redirect(url_for("admin.home"))

@view_admin.route("/delet-estudian/<id>")
def delete_estudian(id):
    conn  = get_db_connection()
    cursor = conn .cursor()
    cursor.execute("DELETE FROM alumno WHERE id= %s",(id,))
    conn.commit()
    cursor.close()
    conn.close()
    

    return redirect(url_for("admin.home"))


@view_admin.route("/add_grupo",  methods=["POST"])
def add_grupo():
    if request.method == 'POST':
        conn  = get_db_connection()
        cursor = conn .cursor()
   
        nombre= request.form['nombre']
        grupo= request.form['grupo']

        cursor.execute("INSERT INTO grupo (nombre,grupo) VALUES (%s, %s)", (nombre, grupo))
        conn.commit()
       
        cursor.close()
        conn.close()
        flash('¡Grupo Agregado correctamente!')
        return redirect(url_for("admin.home"))

@view_admin.route("/delet-grupo/<id>")
def delete_grupo(id):
    conn  = get_db_connection()
    cursor = conn .cursor()
    cursor.execute("DELETE FROM grupo WHERE id= %s",(id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for("admin.home"))


@view_admin.route("/admin_view_infor/<id>")
def admin_view_infor(id):
    conn  = get_db_connection()
    cursor = conn .cursor()

    cursor.execute("SELECT * FROM profesor WHERE id= %s",(id,)) 
    data_id = cursor.fetchall()

    cursor.execute("SELECT * FROM data_task_profesor WHERE profesor_id= %s",(id,))
    data_id_task_alumno = cursor.fetchall()

    
    cursor.close()
    conn.close()
    return render_template("/admin_view/admin_view_infor.html", data_info = data_id, data_task_alumno = data_id_task_alumno)




@view_admin.route("/admin-view-task-alumno/<id>")
def admin_view_task_alumno(id):
    conn  = get_db_connection()
    cursor = conn .cursor()

    cursor.execute("SELECT * FROM alumno WHERE id= %s",(id,)) 
    data_id = cursor.fetchall()
 
    cursor.execute("SELECT * FROM task_alumno WHERE alumno_id= %s",(id,))

    data_id_task= cursor.fetchall()

    cursor.close()

    return render_template("/admin_view/admin_view_task.html", data_info = data_id, data_task = data_id_task)




@view_admin.route("/admin-view-task-grupo/<id>")
def admin_view_task_grupo(id):
    conn  = get_db_connection()
    cursor = conn .cursor()

    cursor.execute("SELECT * FROM grupo WHERE id= %s",(id,)) 
    data_id = cursor.fetchall()
 
    cursor.execute("SELECT * FROM task_grupo WHERE grupo_id= %s",(id,))
    data_id_task = cursor.fetchall()

    cursor.close()
    conn.close()
    return render_template("/admin_view/admin_view_task.html", data_info = data_id, data_task = data_id_task)



@view_admin.route("/delet-profe-task/<id>")
def delet_profe_task(id):
    conn  = get_db_connection()
    cursor = conn .cursor()

    cursor.execute("SELECT profesor_id, tiempo FROM data_task_profesor WHERE id = %s", (id,))

    row = cursor.fetchone()
    
    if row is not None:
        profesor_id = row[0]
        tiempo_tarea = row[1]

        cursor.execute("DELETE FROM data_task_profesor WHERE id= %s",(id,))
        conn.commit()
        cursor.execute("UPDATE profesor SET num_tareas = num_tareas - 1, tiempo_clase = tiempo_clase - %s WHERE id = %s", (tiempo_tarea, profesor_id))
        conn.commit()
    
    cursor.close()
    conn.close()
    return redirect(request.referrer)  


@view_admin.route("/delet-task-alumno-grupo/<id>")
def dele_task_grupo_alumno(id):
    conn  = get_db_connection()
    cursor = conn .cursor()

    cursor.execute("DELETE FROM task_alumno WHERE id= %s",(id,))
    conn.commit()

    cursor.execute("DELETE FROM task_grupo WHERE id= %s",(id,))
    conn.commit()

    cursor.close()
    conn.close()
    return redirect(request.referrer) 
