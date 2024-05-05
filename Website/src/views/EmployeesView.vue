<template>
  <div>
    <h1>Widok na pracowników</h1>
    <table>
      <thead>
        <tr>
          <th>Id <input v-model="filters.id" @input="filterEmployees"></th>
          <th>Imię <input v-model="filters.name" @input="filterEmployees"></th>
          <th>Nazwisko <input v-model="filters.surname" @input="filterEmployees"></th>
          <th>PESEL <input v-model="filters.pesel_number" @input="filterEmployees"></th>
          <th>Wykształcenie <input v-model="filters.degree" @input="filterEmployees"></th>
          <th>Dział <input v-model="filters.department" @input="filterEmployees"></th>
          <th>Numer pokoju <input v-model="filters.room_number" @input="filterEmployees"></th>
          <th>Pensja <input v-model="filters.salary" type="number" @input="filterEmployees"></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="employee in filteredEmployees" :key="employee.id">
          <td>{{ employee.id }}</td>
          <td>{{ employee.name }}</td>
          <td>{{ employee.surname }}</td>
          <td>{{ employee.pesel_number }}</td>
          <td>{{ employee.degree }}</td>
          <td>{{ employee.department }}</td>
          <td>{{ employee.room_number }}</td>
          <td>{{ employee.salary }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      employees: [
        { id: 1, name: "Anna", surname: "Kowalska", pesel_number: "90010112345", degree: "Szkoła średnia ogólnokształcąca", department: "Zarząd", room_number: "101", salary: 4500 },
        { id: 2, name: "Jan", surname: "Nowak", pesel_number: "85050567890", degree: "Studia inżynierskie", department: "Dział: Finanse", room_number: "102", salary: 6000 },
        { id: 3, name: "Marta", surname: "Wiśniewska", pesel_number: "92020234567", degree: "Studia podyplomowe", department: "Dział: Sprzedaż", room_number: "103", salary: 5500 },
        { id: 4, name: "Piotr", surname: "Zieliński", pesel_number: "88080876543", degree: "Technikum", department: "IT (Technologie Informacyjne)", room_number: "104", salary: 6200 },
        { id: 5, name: "Katarzyna", surname: "Wójcik", pesel_number: "93070712321", degree: "Edukacja przedszkolna", department: "Produkcja", room_number: "105", salary: 3000 },
        { id: 6, name: "Michał", surname: "Kamiński", pesel_number: "91060698765", degree: "Szkoła branżowa II stopnia", department: "Logistyka", room_number: "106", salary: 4700 },
        { id: 7, name: "Agnieszka", surname: "Lewandowska", pesel_number: "94040465432", degree: "Studia doktoranckie", department: "Prawny", room_number: "107", salary: 8000 },
        { id: 8, name: "Tomasz", surname: "Dąbrowski", pesel_number: "86030343210", degree: "Studia magisterskie", department: "Bezpieczeństwo Informacji", room_number: "108", salary: 7500 },
        { id: 9, name: "Zofia", surname: "Mazur", pesel_number: "95050555555", degree: "Gimnazjum", department: "Komunikacja Wewnętrzna", room_number: "109", salary: 4200 },
        { id: 10, name: "Marek", surname: "Kozłowski", pesel_number: "87040466666", degree: "Szkoła branżowa I stopnia", department: "Innowacje", room_number: "110", salary: 5000 },
        { id: 11, name: "Julia", surname: "Jankowska", pesel_number: "89090977777", degree: "Studia licencjackie", department: "Dział: Zasoby Ludzkie (HR)", room_number: "201", salary: 4800 },
        { id: 12, name: "Krzysztof", surname: "Wojciechowski", pesel_number: "92070788888", degree: "Studia magisterskie jednolite", department: "Dział: Marketing", room_number: "202", salary: 5300 },
        { id: 13, name: "Teresa", surname: "Szymańska", pesel_number: "85060699999", degree: "Kursy i szkolenia zawodowe", department: "Dział: Obsługa Klienta", room_number: "203", salary: 4000 },
        { id: 14, name: "Adam", surname: "Krawczyk", pesel_number: "84050512349", degree: "Edukacja domowa", department: "Badania i Rozwój (R&D)", room_number: "204", salary: 3200 },
        { id: 15, name: "Dorota", surname: "Pawłowska", pesel_number: "83040412348", degree: "Warsztaty umiejętności miękkich", department: "Rozwój Zrównoważony", room_number: "205", salary: 3900 },
        { id: 16, name: "Robert", surname: "Grabowski", pesel_number: "82030312347", degree: "Akademia seniora (edukacja dla osób starszych)", department: "Relacje Inwestorskie", room_number: "206", salary: 4100 },
        { id: 17, name: "Ewa", surname: "Kaczmarek", pesel_number: "81020212346", degree: "Kursy online (MOOC)", department: "Administracja", room_number: "207", salary: 4300 },
        { id: 18, name: "Krystyna", surname: "Zając", pesel_number: "80010112345", degree: "Kursy językowe", department: "Edukacja i Szkolenia", room_number: "208", salary: 3500 },
        { id: 19, name: "Rafał", surname: "Mazurek", pesel_number: "79020212344", degree: "Szkoła podstawowa", department: "Zakupy", room_number: "209", salary: 2900 },
        { id: 20, name: "Barbara", surname: "Kwiatkowska", pesel_number: "78030312343", degree: "Kształcenie na odległość / E-learning", department: "Jakość", room_number: "210", salary: 4600 }
      ],
      filters: {
        id: '',
        name: '',
        surname: '',
        pesel_number: '',
        degree: '',
        department: '',
        room_number: '',
        salary: ''
      },
      filteredEmployees: []
    }
  },
  mounted() {
    this.filteredEmployees = this.employees;
  },
  methods: {
    filterEmployees() {
      this.filteredEmployees = this.employees.filter(employee => {
        return (
          employee.id.toString().includes(this.filters.id) &&
          employee.name.toLowerCase().includes(this.filters.name.toLowerCase()) &&
          employee.surname.toLowerCase().includes(this.filters.surname.toLowerCase()) &&
          employee.pesel_number.includes(this.filters.pesel_number) &&
          employee.degree.toLowerCase().includes(this.filters.degree.toLowerCase()) &&
          employee.department.toLowerCase().includes(this.filters.department.toLowerCase()) &&
          employee.room_number.toString().includes(this.filters.room_number) &&
          employee.salary.toString().includes(this.filters.salary)
        );
      });
    }
  }
}
</script>

<style>
table {
  width: 100%;
  border-collapse: collapse;
  font-family: Arial, sans-serif; /* Smoother font */
}

th, td {
  border: 1px solid #ccc;
  padding: 8px;
  text-align: left;
}

th {
  background-color: #779fd4; /* Green background for headers */
  color: white; /* White text for headers */
}

tbody tr:nth-child(odd) {
  background-color: #f2f2f2; /* Light grey background for odd rows */
}

tbody tr:nth-child(even) {
  background-color: #ffffff; /* White background for even rows */
}

input {
  width: 100%;
  padding: 8px;
  margin-bottom: 20px;
  box-sizing: border-box; /* Include padding and border in the element's total width and height */
}

h1 {
  text-align: center; 
  margin-top: 20px; 
  margin-bottom: 20px; /* Added bottom margin for spacing */
}
</style>