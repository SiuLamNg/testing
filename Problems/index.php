<?php
$salt = "958083d28ef2";
$hash = "45e2d1488e713a122d7f9eee2f0059f2";

$word_list_file = 'E:\testingProject\testing\Problems\word-list-7-letters.txt';
$word_list = fopen($word_list_file, 'r');

if ($word_list){
  while (($line =fgets($word_list))!== false){

      $temp_hash = md5(trim($line) . $salt);
          if ($temp_hash == $hash) {
            echo trim($line);
            break;
          }
  }
  fclose($word_list);

} else {
    echo "Error.";

}

?>