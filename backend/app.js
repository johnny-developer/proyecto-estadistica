console.log("Hello world backend");


function construirJSON() {
    
    /*
    var nombre = document.getElementById('nombre').value;
    var edad = document.getElementById('edad').value;
    var ciudad = document.getElementById('ciudad').value;
    */
    
    var jsonData = {
        "tipo": 1,
        "x1": 68,
        "x2": 74,
        "media": 70,
        "desviacion": 2
    };

    normal(jsonData)
}

function normal(jsonData) {
    console.log("tipo: " + jsonData.tipo);
    console.log("x1: " + jsonData.x1);
    console.log("x2: " + jsonData.x2);
    console.log("media: " + jsonData.media);
    console.log("desviacion: " + jsonData.desviacion);

    var z1 = calcularProbabilidad(jsonData.x1, jsonData.media, jsonData.desviacion);
    var z2 = calcularProbabilidad(jsonData.x2, jsonData.media, jsonData.desviacion);

    //Obtener valor de excel

    console.log("Probabilidad acumulativa para x1: " + z1);
    console.log("Probabilidad acumulativa para x2: " + z2);

    var probabilidadAcumulativa1 = 0.5 * (1 + erf(z1 / Math.sqrt(2)));
    var probabilidadAcumulativa2 = 0.5 * (1 + erf(z2 / Math.sqrt(2)));

    console.log("Probabilidad acumulativa para x1: " + probabilidadAcumulativa1);
    console.log("Probabilidad acumulativa para x2: " + probabilidadAcumulativa2);
}

function calcularProbabilidad(x, media, desviacion) {
    z = (x-media)/desviacion;
    return z;
}



// Ejemplo de uso
construirJSON();




// Función de error estándar (erf)
function erf(x) {
    var a1 =  0.254829592;
    var a2 = -0.284496736;
    var a3 =  1.421413741;
    var a4 = -1.453152027;
    var a5 =  1.061405429;
    var p  =  0.3275911;

    var sign = (x < 0) ? -1 : 1;
    x = Math.abs(x);

    var t = 1.0 / (1.0 + p * x);
    var y = ((((a5 * t + a4) * t) + a3) * t + a2) * t + a1;

    return sign * (1.0 - y * Math.exp(-x * x));
}