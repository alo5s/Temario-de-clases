import os
from flask import Flask
from dotenv import load_dotenv
from routes.home import view_home
from routes.task import view_task
from routes.students import view_students
from routes.admin import view_admin
from routes.auth import auth

app = Flask(__name__)
# Carga las variables de entorno desde el archivo .env
load_dotenv()

app.secret_key= os.environ.get('SECRET_KEY')

app.register_blueprint(auth)
app.register_blueprint(view_admin)
app.register_blueprint(view_home)
app.register_blueprint(view_task)
app.register_blueprint(view_students)


if __name__=='__main__':
    app.run(debug=True)
