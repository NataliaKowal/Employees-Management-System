<template>
  <nav>
    <router-link to="/">Home</router-link> 
    <router-link to="/employees">Employees</router-link> 
    <router-link to="/departments">Departments</router-link> 
    <router-link to="/degrees">Degrees</router-link> 
    <router-link to="about">About</router-link>
  </nav>
  <router-view/>
</template>

<style>

body{
  font-family: Arial, Helvetica, sans-serif;
}

.add-record-button {
	background-color: #87C38F; 
	border: none;
	color: white;
	text-align: center;
	height: 100%;
	text-decoration: none;
	font-size: 16px;
	cursor: pointer;
	transition: background-color 0.3s ease;
	margin-left: 5px;
}

.add-record-button:hover {
	background-color: #87C38F;
}

.edit-record-button {
	padding-left: 10px;
	background-color: #F8DE7E;
	border: none;
	color: white;
	padding: 5px 15px;
	text-align: center;
	text-decoration: none;
	display: inline-block;
	font-size: 16px;
	margin: 0px 2px;
	cursor: pointer;
	transition: background-color 0.3s ease;
}

.edit-record-button:hover {
	background-color: #F4F0BB;
}

.delete-record-button {
	padding-left: 10px;
	background-color: #DA2C38; 
	color: white;
	padding: 5px 15px;
	text-align: center;
	text-decoration: none;
	display: inline-block;
	font-size: 16px;
	margin: 0px 2px;
	cursor: pointer;
	transition: background-color 0.3s ease;
}

.delete-record-button:hover {
	background-color: #DA2C38;
}

.submit-btn{
    background-color: #87C38F; 
    color: white; 
    padding: 15px 50px; 
    font-size: 16px; 
    border: none; 
    border-radius: 5px;
    cursor: pointer; 
    transition: background-color 0.3s, transform 0.2s; 
    display: block; 
    margin: 0 auto; 
    width: 50%;
}
</style>