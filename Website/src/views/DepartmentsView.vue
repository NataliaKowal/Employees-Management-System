<template>
  <div>
    <h1>Departments View</h1>
    <input type="text" v-model="searchQuery" placeholder="Filter..." />
    <table>
      <thead>
        <tr>
          <th>Id</th>
          <th>Name</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="department in filteredDepartments" :key="department.id">
          <td>{{ department.id }}</td>
          <td>{{ department.name }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      departments: [],
      searchQuery: ''
    };
  },
  computed: {
    filteredDepartments() {
      if (!this.searchQuery) {
        return this.departments;
      }
      const query = this.searchQuery.toLowerCase();
      return this.departments.filter(department =>
        department.name.toLowerCase().includes(query) ||
        department.id.toString().includes(query)
      );
    }
  },
  mounted() {
    this.fetchDepartments();
  },
  methods: {
    fetchDepartments() {
      this.departments = [
        { id: 1, name: "Management" },
        { id: 2, name: "Human Resources (HR)" },
        { id: 3, name: "Finance" },
        { id: 4, name: "Marketing" },
        { id: 5, name: "Sales" },
        { id: 6, name: "Customer Service" },
        { id: 7, name: "IT (Information Technology)" },
        { id: 8, name: "Research and Development (R&D)" },
        { id: 9, name: "Production" },
        { id: 10, name: "Logistics" },
        { id: 11, name: "Purchasing" },
        { id: 12, name: "Quality" },
        { id: 13, name: "Legal" },
        { id: 14, name: "Administration" },
        { id: 15, name: "Information Security" },
        { id: 16, name: "Education and Training" },
        { id: 17, name: "Internal Communication" },
        { id: 18, name: "Sustainable Development" },
        { id: 19, name: "Innovation" },
        { id: 20, name: "Investor Relations" }
      ];
    }
  }
}
</script>

<style>
table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  border: 1px solid #ccc;
  padding: 8px;
  text-align: left;
}

input {
  margin-bottom: 10px;
}
h1 {
  text-align: center; /* Wyśrodkowanie tekstu */
  margin-top: 20px; /* Dodatkowy margines na górze dla lepszego wyglądu */
}
</style>
