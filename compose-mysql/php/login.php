<h1>Login Page</h1>

<?php 
if (isset($_POST["user"]) && isset($_POST["password"])) {
	if (($_POST["user"] != "felix") || ($_POST["password"] != "joergen")) {
		echo '<p>Wrong creds.. login: ' . $_POST["user"] . '; pass: ' . $_POST["password"] . '</p><a href="/index.php">Proceed back to index page</a>';
	} else {
		echo "<h2>YAY! pass: joergen</h2>";
	}
} else { 
	echo "<p>username/password missing</p>";
}
?> 
