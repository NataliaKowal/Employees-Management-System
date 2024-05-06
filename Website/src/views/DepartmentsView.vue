<template>
  <div  class="main">
    <h1>Departments View</h1>
    <div class="filter-and-add-bar">
      <input class="filter-input" type="text" v-model="searchQuery" placeholder="Filter..." />
      <button class="add-record-button" @click="showAddModal = true">Add New Department</button>
    </div>
    <table class="department-table">
      <thead>
        <tr>
          <th>Id</th>
          <th>Name</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="department in filteredDepartments" :key="department.id">
          <td>{{ department.Id }}</td>
          <td>{{ department.Name }}</td>
          <td>
            <div class="edit-delete-container">
              <button class="edit-record-button" @click="showEdit(department)">Edit Department</button>
              <button class="delete-record-button" @click="showDelete(department)">Delete Department</button>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
    <!-- Add Modal -->
    <div v-if="showAddModal">
      <div class="modal">
        <div class="modal-content">
          <span class="close" @click="showAddModal = false">&times;</span>
          <form @submit.prevent="addDepartment">
            <label for="Name">Department Name:</label>
            <input type="text" id="Name" v-model="newDepartmentName" required>
            <button class="submit-btn" type="submit">Submit</button>
          </form>
        </div>
      </div>
    </div>
    <!-- Edit Modal -->
    <div v-if="showEditModal">
      <div class="modal">
        <div class="modal-content">
          <span class="close" @click="showEditModal = false">&times;</span>
          <form @submit.prevent="editDepartment">
            <label for="Name">Department Name:</label>
            <input type="text" id="Name" v-model="currentDepartment.name" required>
            <button type="submit">Submit</button>
          </form>
        </div>
      </div>
    </div>
    <!-- Delete Modal -->
    <div v-if="showDeleteModal">
      <div class="modal">
        <div class="modal-content">
          <span class="close" @click="showDeleteModal = false">&times;</span>
          <p>Are you sure you want to delete this department: {{ currentDepartment.name }}?</p>
          <button @click="deleteDepartment">Delete</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      departments: [],
      searchQuery: '',
      showAddModal: false,
      showEditModal: false,
      showDeleteModal: false,
      currentDepartment: {}
    };
  },
  computed: {
    filteredDepartments() {
      if (!this.searchQuery) {
        return this.departments;
      }
      const query = this.searchQuery.toLowerCase();
      return this.departments.filter(department =>
        department.Name.toLowerCase().includes(query) ||
        department.Id.toString().includes(query)
      );
    }
  },
  methods: {
    fetchDepartments() {
      axios.get('http://localhost:1234/get_all_departments')
        .then(response => {
          this.departments = response.data;
        })
        .catch(error => {
          console.error('Error fetching departments:', error);
        });
    },
    addDepartment() {
      axios.post('http://localhost:1234/add_department', {
        name: this.newDepartmentName
      })
        .then(() => {
          this.showAddModal = false;
          this.currentDepartment = {}; 
          this.fetchDepartments();
        })
        .catch(error => {
          console.error('Error adding new department:', error);
        });
    },
    showEdit(department) {
      this.currentDepartment = {...department};
      this.showEditModal = true;
    },
    editDepartment() {
    axios.post(`http://localhost:1234/edit_department`, {
    id: this.currentDepartment.id,
    name: this.currentDepartment.name
  })
    .then(() => {
      this.showEditModal = false;
      this.currentDepartment = {}; 
      this.fetchDepartments();
    })
    .catch(error => {
      console.error('Error editing department:', error);
    });
},

    showDelete(department) {
      this.currentDepartment = {...department};
      this.showDeleteModal = true;
    },
    deleteDepartment() {
      axios.delete(`http://localhost:1234/delete_department/${this.currentDepartment.id}`)
        .then(() => {
          this.showDeleteModal = false;
          this.currentDepartment = {}; 
          this.fetchDepartments();
        })
        .catch(error => {
          console.error('Error deleting department:', error);
        });
    },
  },
  mounted() {
    this.fetchDepartments();
  },
}
</script>

<style>
.main {
	padding-left: 20px;
	padding-right: 20px;
	width: 100%;
}

.filter-and-add-bar {
	display: grid;
	grid-template-columns: 80% 20%;
	padding-bottom: 10px;
	height: 30px;
}

.filer-input {
	margin-right: 5px;
}

.edit-delete-container {
	display: grid;
	grid-template-columns: 50% 50%;
}

.department-table {
	width: 100%;
	border-collapse: collapse;
	margin: 10px 0;
	font-size: 0.9em;
	font-family: sans-serif;
	min-width: 400px;
	box-shadow: 0 0 20px rgba(0,0,0,0.15);
}

.department-table thead tr {
	background-color: #FF8FA3;
	color: #ffffff;
	text-align: left;
}

.department-table th,
.department-table td {
	padding: 12px 15px;
}

.department-table tbody tr {
	border-bottom: 1px solid #dddddd;
}

.department-table tbody tr:nth-of-type(even) {
	background-color: #f3f3f3;
}

.department-table tbody tr:last-of-type {
	border-bottom: 2px solid #FF8FA3;
}

.department-table tbody tr.active-row {
	font-weight: bold;
	color: #009879;
}

.department-table th:nth-child(1), 
.department-table tr:nth-child(1) {
	width: 20%;
}

.department-table th:nth-child(2), 
.department-table tr:nth-child(2) {
	width: 60%;
}

.department-table th:nth-child(3), 
.department-table tr:nth-child(3) {
	width: 20%;
}

.modal {
	position: fixed;
	left: 0;
	top: 0;
	width: 100%;
	height: 100%;
	background-color: rgba(0, 0, 0, 0.5);
	display: flex;
	justify-content: center;
	align-items: center;
}

.modal-content {
	background-color: #fff0f3;
  border: 1px solid #ff4d6d;
  padding: 8px;
  width: 100%;
  margin: 5px 0;
}

.close {
	float: right;
	cursor: pointer;
}
</style>