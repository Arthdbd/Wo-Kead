<?php
// Указываем версию и ссылку на новую программу
$response = [
    "version" => "7.2.9 beta",  // Новая версия
    "url" => "https://kead.top/farmila.exe"  // Прямая ссылка на .exe
];

// Устанавливаем заголовок JSON
header("Content-Type: application/json");

// Выводим JSON-ответ
echo json_encode($response);
