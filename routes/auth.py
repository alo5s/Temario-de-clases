from flask import Blueprint, session, redirect, url_for, request, render_template
from functools import wraps
from utils.db import get_db_connection

auth= Blueprint('auth',__name__)

@auth.route('/login/User', methods=['GET', 'POST'])
def login_user():
    error = None
    if request.method == 'POST':
        conn  = get_db_connection()

        cursor = conn.cursor()

        username = request.form['username']
        contraseña = request.form['password']
        cursor.execute("SELECT * FROM profesor WHERE username = %s AND contraseña = %s", (username, contraseña))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        if user is None:
            error = 'Nombre de usuario o contraseña incorrectos'
        else:
            session['user_logged_in'] = True
            session['username'] = user[1]
            session['profesor_id'] = user[0]
            return redirect(url_for('home.home'))
    return render_template('/auth/login.html', error=error)


@auth.route('/admin/login', methods=['GET', 'POST'])
def login_admin():
    error = None
    if request.method == 'POST':
        conn  = get_db_connection()
        cursor = conn.cursor()

        username = request.form['username']
        password = request.form['password']
        cursor.execute("SELECT * FROM admin_login WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        if user is None:
            error = 'Nombre de usuario o contraseña incorrectos'
        else:
            session['admin_logged_in'] = True
            session['username'] = user[1]
            return redirect(url_for("admin.home"))
    return render_template('admin_view/auth/login.html', error=error)



def user_login_required(f):
    @wraps(f)
    def decorated_function_user(*args, **kwargs):
        if not session.get('user_logged_in'):
            return redirect(url_for('auth.login_user', next=request.url))
        return f(*args, **kwargs)
    return decorated_function_user

def admin_login_required(f):
    @wraps(f)
    def decorated_function_admin(*args, **kwargs):
        if not session.get('admin_logged_in'):
            return redirect(url_for('auth.login_admin', next=request.url))
        return f(*args, **kwargs)
    return decorated_function_admin


@auth.route('/logout-user')
def logout_user():
    if session.pop('user_logged_in', None):
        return redirect(url_for('auth.login_user'))
    
@auth.route('/logout-admin')
def logout_admin():
    if session.pop('admin_logged_in', None):
       return redirect(url_for('auth.login_admin')) 
       