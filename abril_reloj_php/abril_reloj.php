<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Hora Invertida </title>
    <link rel="stylesheet" href="estil.css">
</head>
<body>

<div class="tarjeta">
    <h2>Hora Invertida en PHP</h2>

    <form method="POST">
        <input type="text" name="hora" placeholder="HH:MM" required>
        <button type="submit">Calcular</button>
    </form>

   <div id="resultado">
    <?php
    if($_POST){
        $hora = $_POST['hora'];
        $partes = explode(":", $hora);

        $h = intval($partes[0]);
        $m = intval($partes[1]);

        $total = $h * 60 + $m;
        $invertido = 720 - $total;

        $nueva_h = intdiv($invertido, 60);
        $nueva_m = $invertido % 60;

        echo sprintf("%02d:%02d", $nueva_h, $nueva_m);
    }
    ?>
</div>
    </div>
</div>

</body>
</html>