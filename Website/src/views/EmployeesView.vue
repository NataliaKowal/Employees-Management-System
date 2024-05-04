<template>
  <div>
    <h1>Widok na pracowników</h1>
    <!-- Wyświetlanie odpowiedzi serwera pod nagłówkiem -->
    <h1>{{ responseMessage }}</h1>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      // Zmienna do przechowywania odpowiedzi serwera
      responseMessage: ''
    }
  },
  mounted() {
    // Wysyłanie zapytania do serwera po załadowaniu komponentu
    this.fetchData();
  },
  methods: {
    fetchData() {
      axios.get('http://localhost:1234/hello_world')
        .then(response => {
          // Przechowywanie odpowiedzi serwera, dostosowanie do struktury JSON
          this.responseMessage = response.data.message;
        })
        .catch(error => {
          console.error('There was an error!', error);
        });
    }
  }
}
</script>

<style>
/* Tutaj możesz dodać style CSS, jeśli potrzebujesz */
</style>
