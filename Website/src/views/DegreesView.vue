<template>
  <div>
    <h1>Employee Education Search</h1>
    <input type="text" v-model="searchQuery" placeholder="Filter..." />
    <table>
      <thead>
        <tr>
          <th>Id</th>
          <th>Name</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="degree in filteredDegrees" :key="degree.id">
          <td>{{ degree.id }}</td>
          <td>{{ degree.name }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      degrees: [],
      searchQuery: ''
    };
  },
  computed: {
    filteredDegrees() {
      if (!this.searchQuery) {
        return this.degrees;
      }
      const query = this.searchQuery.toLowerCase();
      return this.degrees.filter(degree =>
        degree.name.toLowerCase().includes(query) ||
        degree.id.toString().includes(query)
      );
    }
  },
  mounted() {
    this.fetchDegrees();
  },
  methods: {
    fetchDegrees() {
      this.degrees = [
        { id: 1, name: "Preschool Education" },
        { id: 2, name: "Elementary School" },
        { id: 3, name: "Junior High School" },
        { id: 4, name: "General Secondary School" },
        { id: 5, name: "Technical School" },
        { id: 6, name: "Vocational School Level I" },
        { id: 7, name: "Vocational School Level II" },
        { id: 8, name: "Bachelor's Studies" },
        { id: 9, name: "Engineering Studies" },
        { id: 10, name: "Master's Studies" },
        { id: 11, name: "Uniform Master's Studies" },
        { id: 12, name: "Postgraduate Studies" },
        { id: 13, name: "Doctoral Studies" },
        { id: 14, name: "Vocational Courses and Training" },
        { id: 15, name: "Language Courses" },
        { id: 16, name: "Homeschooling" },
        { id: 17, name: "Distance Learning / E-learning" },
        { id: 18, name: "Soft Skills Workshops" },
        { id: 19, name: "Online Courses (MOOC)" },
        { id: 20, name: "Senior Academy (education for the elderly)" }
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
