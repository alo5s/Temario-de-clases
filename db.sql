CREATE TABLE profesor(
  id INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(50) NOT NULL,
  contraseña VARCHAR(50) NOT NULL,
  num_tareas INT NOT NULL DEFAULT 0,
  tiempo_clase INT NOT NULL DEFAULT 0
);


CREATE TABLE alumno (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  apellido VARCHAR(50) NOT NULL
);

CREATE TABLE data_task_profesor (
  id INT PRIMARY KEY AUTO_INCREMENT,
  tema VARCHAR(50) NOT NULL,
  descripcion VARCHAR(255),
  tiempo INT NOT NULL,
  fecha DATE NOT NULL,
  id_alumno_grupo INT NOT NULL,
  profesor_id INT NOT NULL,
  FOREIGN KEY (profesor_id) REFERENCES profesor(id)
);

CREATE TABLE task_alumno (
  id INT PRIMARY KEY AUTO_INCREMENT,
  tema VARCHAR(50) NOT NULL,
  descripcion VARCHAR(255),
  tiempo INT NOT NULL,
  fecha DATE NOT NULL,
  alumno_id INT NOT NULL,
  profesor_id INT NOT NULL,
  FOREIGN KEY (alumno_id) REFERENCES alumno(id)
);


CREATE TABLE grupo (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  grupo VARCHAR(50) NOT NULL
);


CREATE TABLE task_grupo (
  id INT PRIMARY KEY AUTO_INCREMENT,
  tema VARCHAR(50) NOT NULL,
  descripcion VARCHAR(255),
  tiempo INT NOT NULL,
  fecha DATE NOT NULL,
  grupo_id INT NOT NULL,
  profesor_id INT NOT NULL,
  FOREIGN KEY (grupo_id) REFERENCES grupo(id)
);
