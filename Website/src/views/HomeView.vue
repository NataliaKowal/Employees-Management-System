<template>
  <div id="welcome-message">
    <h1>Witaj w systemie zarządzania bazą pracowników firmy!</h1>
  </div>
</template>

<script>

</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

#app {
  display: flex;
  min-height: 100vh;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background-color: #f0f0f0; 
}

#welcome-message {
  width: 100%; 
  display: flex;
  justify-content: center; 
  align-items: center; 
  min-height: 100vh; 
  font-size: 24px; 
  background-color: #FFF0F3; 
  font-family: 'Poppins';
}

nav {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: start;
  padding: 20px;
  background-color: #c9184A; 
  color: white;
  height: 100vh;
  width: 200px; 
}

nav a {
  font-weight: bold;
  color: white;
  padding: 10px;
  text-decoration: none;
  transition: background-color 0.3s;
}

nav a:hover {
  background-color: #FF8FA3; 
}

nav a.router-link-exact-active {
  background-color: #FF8FA3; 
  color: white;
}

.content {
  flex-grow: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center; 
  background-color: #FF8FA3; 

.main-content {
  max-width: 600px; 
}
}

h1 {
  text-align: center; 
  margin-top: 20px; 
  width: 100%; 
}
</style>
