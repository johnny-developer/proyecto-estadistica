console.log("Hello world backend");


function construirJSON() {
    
    var nombre = document.getElementById('nombre').value;
    var edad = document.getElementById('edad').value;
    var ciudad = document.getElementById('ciudad').value;

    var jsonData = {
        "nombre": nombre,
        "edad": edad,
        "ciudad": ciudad
    };

    normal(jsonData)
}



function normal(jsonData) {
    console.log("Nombre: " + jsonData.nombre);
    console.log("Edad: " + jsonData.edad);
    console.log("Ciudad: " + jsonData.ciudad);
}