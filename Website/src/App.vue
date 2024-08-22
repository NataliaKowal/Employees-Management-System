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

#app {
  display: flex;
  min-height: 100vh;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background-color: #f0f0f0; 
}

body{
  font-family: Arial, Helvetica, sans-serif;
}

/* Bazowy styl dla wszystkich przycisków */
button {
    padding: 10px 15px;
    border: none;
    color: white;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.2s;
    border-radius: 5px;
    display: inline-block;
    margin: 0px 5px;
}

/* Styl dla przycisku dodawania */
.add-record-button {
    background-color: #4CAF50; /* Zmieniono na bardziej żywy odcień zieleni */
}

.add-record-button:hover {
    background-color: #45a049; /* Ciemniejszy odcień dla hover */
}

/* Styl dla przycisku edycji */
.edit-record-button {
    background-color: #FFC107; /* Zmieniono na bardziej żywy odcień żółtego */
}

.edit-record-button:hover {
    background-color: #ffb300; /* Ciemniejszy odcień dla hover */
}

/* Styl dla przycisku usuwania */
.delete-record-button {
    background-color: #f44336; /* Zmieniono na bardziej żywy odcień czerwieni */
}

.delete-record-button:hover {
    background-color: #e53935; /* Ciemniejszy odcień dla hover */
}

/* Styl dla przycisków w modalach */
.submit-btn, .cancel-btn {
    padding: 15px 20px;
    width: 80%; /* Zwiększona szerokość dla lepszego dopasowania */
    margin: 20px auto; /* Zwiększony margines dla lepszego wyśrodkowania */
}

.submit-btn {
    background-color: #4CAF50; /* Ujednolicenie koloru z przyciskiem dodawania */
}

.submit-btn:hover {
    background-color: #45a049; /* Ciemniejszy odcień dla hover */
}

.cancel-btn {
    background-color: #f44336; /* Ujednolicenie koloru z przyciskiem usuwania */
}

.cancel-btn:hover {
    background-color: #e53935; /* Ciemniejszy odcień dla hover */
}
</style>