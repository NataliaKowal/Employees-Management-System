<template>
  <div class="page-container">
    <div class="content-container info-section">
      <h1>Baza danych pracowników</h1>
      <p class="description">
        Baza danych pracowników to zbiór wszystkich danych i informacji o pracownikach firmy,
        przechowywanych i zarządzanych w określonej formie.
      </p>
      <p class="description">
        Dawne formy baz danych obejmowały dzienniki, karty pracownicze i teczki. Obecnie
        jednak specjaliści HR skanują i przechowują dokumenty pracowników w formie cyfrowej w
        systemach zarządzania zasobami ludzkimi, takich jak PeopleForce.
      </p>
      <h2>Baza danych pracowników daje specjalistom HR możliwość:</h2>
      <ul class="features-list">
        <li>Przyjmowania nowych pracowników;</li>
        <li>Oddelegowania tych pracowników, którzy z różnych powodów odchodzą z firmy;</li>
        <li>Aktualizowania danych osobowych pracowników;</li>
        <li>Dostęp do historycznych danych dotyczących zatrudnienia;</li>
        <li>Przygotowywania i wysyłki listów weryfikujących zatrudnienie.</li>
      </ul>
      <button class="cta-button" @click="rozpocznij">Dowiedz się więcej</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
  methods: {
    rozpocznij() {
      console.log('Kliknięto przycisk "Dowiedz się więcej"');
      // Tutaj można dodać logikę, która ma się wykonać po kliknięciu przycisku
    }
  }
}
</script>

<style scoped>
body, html {
  margin: 0;
  padding: 0;
  height: 100%;
  font-family: 'Arial', sans-serif;
  background-color: #f0f0f0;
}

.page-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  padding: 20px;
}

.content-container {
  background-color: #d81b60;
  padding: 40px;
  border-radius: 10px;
  color: white;
  max-width: 800px;
  width: 100%;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.info-section {
  text-align: left;
}

h1, h2 {
  color: white;
  margin-bottom: 20px;
}

.description {
  margin-bottom: 15px;
  line-height: 1.6;
}

.features-list {
  padding-left: 20px;
  margin-bottom: 20px;
}

.features-list li {
  margin-bottom: 10px;
}

.cta-button {
  display: block;
  margin: 20px auto 0;
  padding: 12px 24px;
  background-color: white;
  color: #d81b60;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  font-weight: bold;
  transition: background-color 0.3s, color 0.3s;
}

.cta-button:hover {
  background-color: #ff80ab;
  color: white;
}

@media (max-width: 600px) {
  .content-container {
    padding: 20px;
  }
}
</style>
