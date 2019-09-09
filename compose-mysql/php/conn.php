<?php 
	$host = 'db';
	$user = 'devel';
	$password = 'bazinga';
	$db = 'proj';
	$conn = new mysqli($host,$user,$password,$db);
	if ($conn->connect_error) {
		echo 'connection failed: ' . $conn->connect_error;
	}
	else {
		echo "all fine!";
	}
	if (isset($_GET["user"]) && isset($_GET["password"])) {
		$user = md5($_GET["user"]);
		$password = md5($_GET["password"]);
		echo "user:pass => " . $user . ":" . $password;
		if (($_GET["user"] != "felix") || ($_GET["password"] != "joergen")) {
			echo '<p>Wrong creds.. login: ' . $_GET["user"] . '; pass: ' . $_GET["password"] . '</p><a href="/index.php">Proceed back to index page</a>';
		} else {
			echo "<h2>YAY! pass: joergen</h2>";
		}
	} else {
    	echo "<p>username/password missing</p>";
	}
	echo "fin";
?>
