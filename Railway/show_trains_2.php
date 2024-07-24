<html>
<body style=" background-image: url(https://th.bing.com/th?id=OIP.bcOP7ZTpLAyyl3tKpdk5gAHaFB&w=303&h=206&c=8&rs=1&qlt=90&o=6&dpr=1.5&pid=3.1&rm=2);
    height: 100%; 
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;">

<form action="search_results.php" method="post">
    <input type="int" placeholder="enter starting point" name="searchs" required><br>
    <input type="submit" value="Search" required><br>

<?php

require "db.php";

$cdquery="SELECT * FROM train join classseats where classseats.trainno=train.trainno";
$cdresult=mysqli_query($conn,$cdquery);
echo "
<table>
<thead><td>Train_no</td><td>Train_name</td><td>Starting_Point</td><td>Arrival_Time</td><td>Destination_Point</td><td>Departure_Time</td><td>Day</td><td>Distance</td><td>Date_of_Dept</td></thead>
";

while ($cdrow=mysqli_fetch_array($cdresult)) 
{
	echo "
<tr><td>".$cdrow['trainno']."</td><td>".$cdrow['tname']."</td><td>".$cdrow['sp']."</td><td>".$cdrow['st']."</td><td>".$cdrow['dp']."</td><td>".$cdrow['dt']."</td><td>".$cdrow['dd']."</td><td>".$cdrow['distance']."</td><td>".$cdrow['doj']."</td></tr>
";
}

?>
</body>
</html>