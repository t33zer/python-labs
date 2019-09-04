<h1> AAABBBAAAAAAAAAA</h1>

<form action="/login.php" method="post">
	<input type="text" name="user" value="chenado?">
	<input type="password" name="password">
	<input type="submit">
</form>
<?php



echo phpinfo();

?>

<h1>Login Page</h1>

<?php 
if (isset($_POST["user"]) && isset($_POST["password"])) {
	if (($_POST["user"] == "felix") || ($_POST["password"] != "joergen")) {
		echo '<p>Wrong creds...</p>\n<a href="/index.php">Proceed back to index page</a>';
	} else {
		echo "<h2>YAY! pass: joergen</h2>";
	}
} else { 
	echo "<p>username/password missing</p>";
}
?> 