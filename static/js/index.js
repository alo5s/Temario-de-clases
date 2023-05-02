const navboggle = document.querySelector(".nav-toggle")
const navtoggle = document.querySelector(".nav-link-ul")

navboggle.addEventListener("click", () => {
  navtoggle.classList.toggle("nav-link-ul-visible")
})



function showFields() {
    var taskSelect = document.getElementById("task-form");
    var estudianteFields = document.getElementById("task-estudiante");
    var grupoFields = document.getElementById("task-grupo");

    estudianteFields.style.display = "none";
    grupoFields.style.display = "none";

    if (taskSelect.value === "estudiantes") {
        estudianteFields.style.display = "block";
    } else if (taskSelect.value === "grupo") {
        grupoFields.style.display = "block";
    }
}

function fieldAdmin() {
    var tbSelect = document.getElementById("tabla-view");

    var tbProfesor = document.getElementById("tb-profesor");
    var tbProfesor_add = document.getElementById("tb-profesor-add");

    var tbAlumno = document.getElementById("tb-alumno");
    var tbAlumno_add = document.getElementById("tb-alumno-add");

    var tbGrupo = document.getElementById("tb-grupo");
    var tbGrupo_add = document.getElementById("tb-grupo-add");

    tbProfesor.style.display = "none";
    tbProfesor_add.style.display = "none";
    tbAlumno.style.display = "none";
    tbAlumno_add.style.display = "none";
    tbGrupo.style.display = "none";
    tbGrupo_add.style.display = "none";
  
    if (tbSelect.value === "profesores") {
      tbProfesor.style.display = "table";
      tbProfesor_add.style.display = "flex";
    } else if (tbSelect.value === "alumno") {
      tbAlumno.style.display = "table";
      tbAlumno_add.style.display = "flex";
    } else if (tbSelect.value === "grupo") {
      tbGrupo.style.display = "table";
      tbGrupo_add.style.display = "flex";
    }
  }


flatpickr("#fecha", {
  dateFormat: "d-m-Y",
  defaultDate: "today",
  maxDate: "today",
  locale: "es"
});

