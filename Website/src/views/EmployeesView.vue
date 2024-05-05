<template>
  <div class="main">
    <div class="main"></div>
    <h1>Widok na pracowników</h1>
    <div class="filer-and-add-bar">
      <input class="filer-input" type="text" v-model="this.searchQuery" placeholder="Filter..." />
			<button class="add-record-button" @click="showAddModal = true">Add New Employee</button>
    </div>
      <table class="employees-table">
      <thead>
        <tr>
          <th>Id</th>
          <th>Name</th>
          <th>Surname</th>
          <th>PESEL</th>
          <th>Degree</th>
          <th>Department</th>
          <th>Room number</th>
          <th>Salary</th>
          <th>Edit</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="employee in filteredEmployees" :key="employee.Id">
          <td>{{ employee.Id }}</td>
          <td>{{ employee.Name }}</td>
          <td>{{ employee.Surname }}</td>
          <td>{{ employee.PESEL_number }}</td>
          <td>{{ employee.Degree_Id }}</td>
          <td>{{ employee.Departemnt_Id }}</td>
          <td>{{ employee.Room_number }}</td>
          <td>{{ employee.Salary }}</td>
          <td>
            <div class="edit-delete-container">
							<button class="edit-record-button" @click="showEdit(employee)">Edit Degree</button>
							<button class="delete-record-button" @click="showDelete(employee)">Delete Degree</button>
						</div>
          </td>
        </tr>
      </tbody>
    </table>
    <!-- Add Modal -->
    <div v-if="showAddModal" class="modal">
      <div class="modal-content">
        <span class="close" @click="showAddModal = false">&times;</span>
        <form @submit.prevent="addEmployee">
          <div class="inputs-and-labels-container">
            <label class = "Working" for="Name">Employee Name:</label>
            <input class = "New_Working" type="text" id="Name" v-model="newEmployee.Name" required>

            <label class = "Working" for="Surname">Employee Surname:</label>
            <input class = "New_Working" type="text" id="Surname" v-model="newEmployee.Surname" required>

            <label class = "Working" for="PESEL">Employee PESEL:</label>
            <input class = "New_Working" type="text" id="PESEL" v-model="newEmployee.PESEL_number" required>

            <label class = "Working" for="Degree">Employee Degree:</label>
            <input class = "New_Working" type="text" id="Degree" v-model="newEmployee.Degree_Id" required>

            <label class = "Working" for="Department">Employee Department:</label>
            <input class = "New_Working" type="text" id="Department" v-model="newEmployee.Departemnt_Id" required>

            <label class = "Working" for="Room_Number">Employee Room Number:</label>
            <input class = "New_Working" type="text" id="Room_Number" v-model="newEmployee.Room_Number" required>

            <label class = "Working" for="Salary">Employee Salary:</label>
            <input class = "New_Working" type="text" id="Salary" v-model="newEmployee.Salary" required>
          </div>
          <button type="submit">Submit</button> 
        </form>
      </div>
    </div>
    <!-- Edit Modal -->
    <div v-if="showEditModal">
			<div class="modal">
				<div class="modal-content">
					<span class="close" @click="showEditModal = false">&times;</span>
					<form @submit.prevent="editEmployee">
						<div class="inputs-and-labels-container">
              <label class = "Working" for="Name">Employee Name:</label>
              <input class = "New_Working" type="text" id="Name" v-model="currentEmployee.Name" required>

              <label class = "Working" for="Surname">Employee Surname:</label>
              <input class = "New_Working" type="text" id="Surname" v-model="currentEmployee.Surname" required>

              <label class = "Working" for="PESEL">Employee PESEL:</label>
              <input class = "New_Working" type="text" id="PESEL" v-model="currentEmployee.PESEL_number" required>

              <label class = "Working" for="Degree">Employee Degree:</label>
              <input class = "New_Working" type="text" id="Degree" v-model="currentEmployee.Degree_Id" required>

              <label class = "Working" for="Department">Employee Department:</label>
              <input class = "New_Working" type="text" id="Department" v-model="currentEmployee.Departemnt_Id" required>

              <label class = "Working" for="Room_Number">Employee Room Number:</label>
              <input class = "New_Working" type="text" id="Room_Number" v-model="currentEmployee.Room_number" required>

              <label class = "Working" for="Salary">Employee Salary:</label>
              <input class = "New_Working" type="text" id="Salary" v-model="currentEmployee.Salary" required>
            </div>
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
					<p>Are you sure you want to delete this employee? {{ this.currentEmployee.Name }}?</p>
					<button @click="deleteEmployee">Delete</button>
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
    showAddModal: false,
    showEditModal: false,
    showDeleteModal: false,
    currentEmployee: {
      Id: '',
      Name: '',
      Surname: '',
      PESEL_number: '',
      Degree_Id: '',
      Departemnt_Id: '',
      Room_number: '',
      Salary: ''
    },
    newEmployee: {
      Id: '',
      Name: '',
      Surname: '',
      PESEL_number: '',
      Degree_Id: '',
      Departemnt_Id: '',
      Room_number: '',
      Salary: ''
    },
    employees: [],
    filters: {
      Id: '',
      Name: '',
      Surname: '',
      PESEL_number: '',
      Degree_Id: '',
      Departemnt_Id: '',
      Room_number: '',
      Salary: ''
    },
    searchQuery: ''
  };
},
computed: {
  filteredEmployees() {
    if (!this.searchQuery) {
      return this.employees;
    }
    const query = this.searchQuery.toLowerCase();
    return this.employees.filter(employee =>
      employee.Name.toLowerCase().includes(query) ||
      employee.Surname.toLowerCase().includes(query) ||
      employee.Id.toString().includes(query) ||
      employee.PESEL_number.toString().includes(query) ||
      employee.Degree_Id.toString().includes(query) ||
      employee.Departemnt_Id.toString().includes(query) ||
      employee.Room_number.toString().includes(query) ||
      employee.Salary.toString().includes(query)
    );
  }
},
methods: {
  fetchEmployees() {
    axios.get('http://localhost:1234/get_all_employees')
      .then(response => {
        this.employees = response.data;
        this.filteredEmployees = this.employees;
      })
      .catch(error => {
        console.error('Error fetching employees:', error);
      });
  },
  addEmployee() {
    axios.post('http://localhost:1234/add_employee', {
      Name: this.newEmployee.Name,
      Surname: this.newEmployee.Surname,
      PESEL_number: this.newEmployee.PESEL_number,
      Degree_Id: this.newEmployee.Degree_Id,
      Departemnt_Id: this.newEmployee.Departemnt_Id,
      Room_number: this.newEmployee.Room_number,
      Salary: this.newEmployee.Salary
    })
    .then(() => {
      this.showAddModal = false;
      this.newEmployee = {}; 
      this.fetchEmployees();
    })
    .catch(error => {
      console.error('Error adding new employee:', error);
    });
  },
  showEdit(employee) {
    this.currentEmployee = {...employee};
    this.showEditModal = true;
  },
  editEmployee() {
    axios.post(`http://localhost:1234/edit_employee`, {
      Id: this.currentEmployee.Id,
      Name: this.currentEmployee.Name,
      Surname: this.currentEmployee.Surname,
      PESEL_number: this.currentEmployee.PESEL_number,
      Degree_Id: this.currentEmployee.Degree_Id,
      Departemnt_Id: this.currentEmployee.Departemnt_Id,
      Room_number: this.currentEmployee.Room_number,
      Salary: this.currentEmployee.Salary
    })
    .then(() => {
      this.showEditModal = false;
      this.currentEmployee = {}; 
      this.fetchEmployees();
    })
    .catch(error => {
      console.error('Error editing employee:', error);
    });
  },
  showDelete(employee) {
    this.currentEmployee = {...employee};
    this.showDeleteModal = true;
  },
  deleteEmployee() {
    axios.post(`http://localhost:1234/delete_employee`, {
      Id: this.currentEmployee.Id
    })
    .then(() => {
      this.showDeleteModal = false;
      this.currentEmployee = {}; 
      this.fetchEmployees();
    })
    .catch(error => {
      console.error('Error deleting employee:', error);
    });
  },
},
mounted() {
  this.fetchEmployees();
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

.filter-input {
    margin-right: 5px;
}

.edit-delete-container {
    display: grid;
    grid-template-columns: 50% 50%;
}

.employees-table {
    width: 100%;
    border-collapse: collapse;
    margin: 10px 0;
    font-size: 0.9em;
    font-family: sans-serif;
    min-width: 400px;
    box-shadow: 0 0 20px rgba(0,0,0,0.15);
}

.employees-table thead tr {
    background-color: #779fd4;
    color: #ffffff;
    text-align: left;
}

.employees-table th,
.employees-table td {
    padding: 12px 15px;
}

.employees-table tbody tr {
    border-bottom: 1px solid #dddddd;
}

.employees-table tbody tr:nth-of-type(even) {
    background-color: #f3f3f3;
}

.employees-table tbody tr:last-of-type {
    border-bottom: 2px solid #779fd4;
}

.employees-table tbody tr.active-row {
    font-weight: bold;
    color: #009879;
}

.employees-table th:nth-child(1), 
.employees-table tr:nth-child(1) {
	width: 10%;
}

.employees-table th:nth-child(2), 
.employees-table tr:nth-child(2) {
	width: 10%;
}

.employees-table th:nth-child(3), 
.employees-table tr:nth-child(3) {
	width: 10%;
}

.employees-table th:nth-child(4), 
.employees-table tr:nth-child(4) {
	width: 10%;
}

.employees-table th:nth-child(5), 
.employees-table tr:nth-child(5) {
	width: 10%;
}

.employees-table th:nth-child(6), 
.employees-table tr:nth-child(6) {
	width: 10%;
}

.employees-table th:nth-child(7), 
.employees-table tr:nth-child(7) {
	width: 10%;
}

.employees-table th:nth-child(8), 
.employees-table tr:nth-child(8) {
	width: 10%;
}

.employees-table th:nth-child(9), 
.employees-table tr:nth-child(9) {
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
    background: white;
    padding: 20px;
    border-radius: 5px;
    width: 50%;
    height: 50%;
    max-height: 100%;
    overflow-y: auto;
}

.close {
    float: right;
    cursor: pointer;
}

.add-record-button {
    background-color: #93c768; 
    border: none;
    color: white;
    text-align: center;
    height: 100%;
    text-decoration: none;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.3s ease;
    margin-left: 5px;
}

.add-record-button:hover {
    background-color: #48d65b;
}

.edit-record-button,
.delete-record-button {
    padding: 5px 15px;
    border: none;
    color: white;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 0px 2px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.edit-record-button {
    background-color: #d1cf3d;
}

.edit-record-button:hover {
    background-color: #ebac00;
}

.delete-record-button {
    background-color: #df4a4a;
}

.delete-record-button:hover {
    background-color: #9e1e1e;
}

.inputs-and-labels-container {
  display: flex;
  flex-direction: column;
}

.Working{
  font-size: 150%;
}

.New_Working{
  height: 20px;
  margin-bottom: 15px;
}
</style>