<h1>AirBnB Clone <em>-The Console</em></h1>
The AirBnB Console allows us to manage the objects of the web app.
<html>
<head>
<style>
table {
font-family: arial, sans-serif;
border-collapse: collapse;
width: 100%
}
td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}
tr:nth-child(even) {
background-color: #dddddd;
}
</style>
</head>
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
</body>
</html>
