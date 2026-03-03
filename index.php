<?php
function espejo($hora) {
    $partes = explode(":", $hora);
    $h = intval($partes[0]) % 12;
    $m = intval($partes[1]);

    $mReal = (60 - $m) % 60;
    $hReal = (11 - $h + ($m > 0 ? 1 : 0)) % 12;
    if ($hReal == 0) $hReal = 12;

    return sprintf("%02d:%02d", $hReal, $mReal);
}

$salida = "";
if (!empty($_POST["hora"])) {
    $salida = espejo($_POST["hora"]);
}
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Hora Reflejada</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<div class="panel">
    <h1>Hora reflejada</h1>
    <p>Ingrese la hora observada en el espejo</p>

    <form method="post">
        <input type="time" name="hora" required>
        <button>Calcular</button>
    </form>

    <?php if ($salida): ?>
        <div class="respuesta">
            Hora real: <strong><?= $salida ?></strong>
        </div>
    <?php endif; ?>
</div>

</body>
</html>