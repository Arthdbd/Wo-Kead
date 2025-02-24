<?php
header('Content-Type: application/json');

// Текущая версия на сервере
$serverVersion = "7.2.7";

// URL для загрузки обновления
$updateUrl = "https://kead.top/Farmila/update.zip";

// Получаем текущую версию программы от клиента
$clientVersion = isset($_GET['version']) ? $_GET['version'] : null;

if ($clientVersion === null) {
    echo json_encode([
        'status' => 'error',
        'message' => 'Версия не указана.'
    ]);
    exit;
}

// Сравниваем версии
if ($clientVersion === $serverVersion) {
    echo json_encode([
        'status' => 'success',
        'update_available' => false,
        'message' => 'У вас актуальная версия.'
    ]);
} else {
    echo json_encode([
        'status' => 'success',
        'update_available' => true,
        'version' => $serverVersion,
        'update_url' => $updateUrl,
        'message' => 'Доступно новое обновление.'
    ]);
}
?>
