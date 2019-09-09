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
		$user = $conn->real_escape_string($_GET["user"]);
		$password = $conn->real_escape_string($_GET["password"]);
		echo "user:pass => " . $user . ":" . $password ;
		$query = "SELECT * FROM creds WHERE username='$user' AND password='$password'";
		$result = $conn->query($query);
		if ($result->num_rows == 1) {
			echo "<h2>YAY! pass: joergen</h2>";
			printf("select returned  %d rows", $result->num_rows);
		}
		else {
			echo '<p>Wrong creds.. login: ' . $_GET["user"] . '; pass: ' . $_GET["password"] . '</p><a href="/index.php">Proceed back to index page</a>';
		}
	}
?>
