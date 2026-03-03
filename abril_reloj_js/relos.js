document.getElementById("formHora").addEventListener("submit", function(e){
    e.preventDefault();

    let hora = document.getElementById("hora").value;

    let h = parseInt(hora.split(":")[0]);
    let m = parseInt(hora.split(":")[1]);

    let total = h * 60 + m;
    let invertido = 720 - total;

    let nueva_h = Math.floor(invertido / 60);
    let nueva_m = invertido % 60;

    document.getElementById("resultado").innerHTML =
        nueva_h + ":" + nueva_m;
});