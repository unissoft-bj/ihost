<?php  
    try{
        $soap = new SoapClient(null,array('location'=>"http://192.168.1.254/auth/auth.php",'uri'=>'auth.php'));
        $result = $soap->getMac($_GET['mac']);
        //echo $result."<br/>";
        if ($result == 1){
           $auth = 1;
            }
    }catch(SoapFault $e){
        echo "Warning: ".$e->getMessage() . "<br />";
    }catch(Exception $e){
        echo "Warning: ".$e->getMessage() . "<br />";
    }   
?>
            