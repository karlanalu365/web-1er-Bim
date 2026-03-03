const hora = document.getElementById("hora");
const minuto = document.getElementById("minuto");
const resultado = document.getElementById("resultado");

// Cargar horas
for (let i = 0; i < 24; i++) {
    hora.innerHTML += `<option value="${i}">${String(i).padStart(2, "0")}</option>`;
}

// Cargar minutos
for (let i = 0; i < 60; i++) {
    minuto.innerHTML += `<option value="${i}">${String(i).padStart(2, "0")}</option>`;
}

function calcular() {
    let h = parseInt(hora.value);
    let m = parseInt(minuto.value);

    h = h % 12;

    let minReal = (60 - m) % 60;
    let horaReal = (11 - h + (m > 0 ? 1 : 0)) % 12;

    if (horaReal === 0) horaReal = 12;

    resultado.innerHTML =
        `⏰ Hora real<br>${String(horaReal).padStart(2, "0")}:${String(minReal).padStart(2, "0")}`;
}