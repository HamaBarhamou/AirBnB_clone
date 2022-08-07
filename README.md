<h1>AirBnB Clone <em>-The Console</em></h1>
<img src="screenshot.png" alt="HBNB Image" title="AirBnB Clone">
The AirBnB Console allows us to manage the objects of the web app.
<html>
<body>

<table>
<tr>
<th>Commands</th>
<th>Command to use</th>
<th>¿What the cmd is doing?</th>
</tr>
<tr>
<td>Create)</td>
<td>create BaseModel</td>
<td>Creates a new instance of BaseModel (ex: User or Place)</td>
</tr>
<tr>
<td>Show</td>
<td>show BaseModel / show BaseModel My_First_Model</td>
<td>If the ID is missing or instance not found it's going to show the message.</td>
</tr>
<tr>
<td>Destroy</td>
<td>destroy BaseModel</td>
<td>Deletes an instance based on the class and id</td>
</tr>
<tr>
<td>All</td>
<td>all BaseModel</td>
<td>Prints all objects based or not on the class name as a list of strings</td>
</tr>
<tr>
<td>Update</td>
<td>update BaseModel</td>
<td>Updates an object based on the class name and id (id, created_at, updated_at can't be updated</td>
</tr>
<table>
<tr>
<td>EOF</td>
<td>EOF</td>
<td>exit the program</td>
</tr>
<tr>
<td>quit</td>
<td>quit</td>
<td>exit the program</td>
</tr>
<tr>
<td>help</td>
<td>help/help quit/help EOF</td>
<td>help exiting the program</td>
</tr>
<tr>
<tr>
<td>Empty line</td>
<td>N/A</td>
<td>an empty line + ENTER shouldn't execute anything</td>
</tr>
<td>Custom Prompt</td>
<td>(hbnb)</t>
<td>N/A</td>
</tr>

</body>
</html>

<h2>Execution of the console</h2>

````
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

```
````
