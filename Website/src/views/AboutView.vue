<template>
  <div>
    <h1>This is an about page</h1>
  </div>
</template>

<script>

</script>

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
  background-color: #0056b3; /* Granatowy kolor paska nawigacyjnego */
  color: white;
  height: 100vh;
  width: 200px; /* szerokość paska nawigacyjnego */
}

nav a {
  font-weight: bold;
  color: white;
  padding: 10px;
  text-decoration: none;
  transition: background-color 0.3s;
}

nav a:hover {
  background-color: #007bff; /* Nieco jaśniejszy niebieski dla efektu hover */
}

nav a.router-link-exact-active {
  background-color: #003366; /* Ciemniejszy niebieski dla aktywnego linku */
  color: white;
}

.content {
  flex-grow: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center; /* Centrowanie tekstu */
  background-color: #add8e6; /* Jasnoniebieskie tło dla głównej zawartości */
}

.main-content {
  max-width: 600px; /* Ograniczenie szerokości treści, aby była bardziej czytelna */
}

h1 {
  text-align: center; /* Wyśrodkowanie tekstu */
  margin-top: 20px; /* Dodatkowy margines górny, jeśli potrzebny */
  width: 100%; /* Zapewnia, że tytuł jest wyśrodkowany w kontenerze */
}
</style>

