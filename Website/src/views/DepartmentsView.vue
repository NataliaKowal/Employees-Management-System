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
