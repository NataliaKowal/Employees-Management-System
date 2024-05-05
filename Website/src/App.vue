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
}

nav {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: start;
  padding: 20px;
  background-color: #00fff2; /* Granatowy kolor paska nawigacyjnego */
  color: white;
  height: 100vh;
  width: 200px; /* szerokość paska nawigacyjnego */
}

nav a {
  font-weight: bold;
  color: rgb(255, 255, 255);
  padding: 10px;
  text-decoration: none;
  transition: background-color 0.5s;
}

nav a:hover {
  background-color: #00fff2; /* Nieco jaśniejszy niebieski dla efektu hover */
}

nav a.router-link-exact-active {
  background-color: #00fff2; /* Ciemniejszy niebieski dla aktywnego linku */
  color: white;
}

.content {
  flex-grow: 1;
  padding: 20px;
  background-color: #add8e6; /* Jasnoniebieskie tło dla głównej zawartości */
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center; /* Centrowanie tekstu */
}

.main-content {
  max-width: 600px;
}
</style>