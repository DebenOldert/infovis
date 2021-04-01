<?php
$i = 0;
$lines = $_GET['lines'];

$output = "";

$file = fopen("data/body.csv", "rb");

while(($line = fgets($file)) !== false) {
    if (feof($file)) break;
    $output .= $line;
    if ($i++ >= $lines) {
        break;
    }
}

fclose($file);

echo $output;