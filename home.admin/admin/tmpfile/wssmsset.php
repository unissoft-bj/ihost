<?php

    $sql = "  insert into authsms set sms = '"  . $msg  . 
           "',  phone = '" . $_POST['sphone'] .
           "',  stat ='0',  rectime=now()";  
              
    $result = mysql_query($sql);       
    if (!$result) { // Error handling
        echo "send out msg failed"; 
    }
    else{
        mysql_free_result($result);
    }
?>

        