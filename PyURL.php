<?php
  if($_POST["URL"])
  {
  	echo exec ("parser.py ".$_POST["URL"]);
  }
?>

<html>
  <head>
  </head>
  <body>
  <form action = "PyURL.php" method = "post">
    <td> <input type = "text" size 10 maxlength = "10" name = "URL"> </td>
    <td> <input type = "submit" value = "Submit"; ></td>
  </form>
  </body>
<html>