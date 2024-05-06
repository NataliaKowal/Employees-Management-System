<template>
	<div class="main">
		<div class="main"></div>
		<h1>View of the employees</h1>
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
					<td>{{ getDegreeName(employee.Degree_Id) }}</td>
					<td>{{ getDepartmentName(employee.Departemnt_Id) }}</td>
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
				<div class="modal-description-and-close">
					<h2>Add new employee</h2>
					<span class="close" @click="showAddModal = false">&times;</span>
				</div>
				<div class="modal-container">
					<div class="inputs-and-labels-container">
						<label class="Working" for="Name">Employee Name:</label>
						<input class="New_Working" type="text" id="Name" v-model="newEmployee.Name" required>

						<label class="Working" for="Surname">Employee Surname:</label>
						<input class="New_Working" type="text" id="Surname" v-model="newEmployee.Surname" required>

						<label class="Working" for="PESEL">Employee PESEL:</label>
						<input class="New_Working" type="text" id="PESEL" v-model="newEmployee.PESEL_number" required>

						<!-- Department -->
						<label class="Working" for="Department">Employee Department:</label>
						<select class="New_Working" id="Department" v-model="newEmployee.Departemnt_Id" required>
							<option v-for="department in departments" :value="department.Id" :key="department.Id">
								{{ department.Name }}
							</option>
						</select>

						<!-- Degree -->
						<label class="Working" for="Degree">Employee Degree:</label>
						<select class="New_Working" id="Degree" v-model="newEmployee.Degree_Id" required>
							<option v-for="degree in degrees" :value="degree.Id" :key="degree.Id">
								{{ degree.Name }}
							</option>
						</select>


						<label class="Working" for="Room_Number">Employee Room Number:</label>
						<input class="New_Working" type="text" id="Room_Number" v-model="newEmployee.Room_Number"
							required>

						<label class="Working" for="Salary">Employee Salary:</label>
						<input class="New_Working" type="text" id="Salary" v-model="newEmployee.Salary" required>
					</div>
				</div>
				<div class="modal-sumbmit-discard-buttons">
					<button class="submit-btn" @click="addEmployee">Submit</button>
					<button class="cancel-btn" @click="showAddModal = false">Cancel</button>
				</div>
			</div>
		</div>
		<!-- Edit Modal -->
		<div v-if="showEditModal" class="modal">
			<div class="modal-content">
				<div class="modal-description-and-close">
					<h2>Edit employee</h2>
					<span class="close" @click="showEditModal = false">&times;</span>
				</div>
				<div class="modal-container">
					<div class="inputs-and-labels-container">
						<label class="Working" for="Name">Employee Name:</label>
						<input class="New_Working" type="text" id="Name" v-model="currentEmployee.Name" required>

						<label class="Working" for="Surname">Employee Surname:</label>
						<input class="New_Working" type="text" id="Surname" v-model="currentEmployee.Surname" required>

						<label class="Working" for="PESEL">Employee PESEL:</label>
						<input class="New_Working" type="text" id="PESEL" v-model="currentEmployee.PESEL_number"
							required>

						<label class="Working" for="Degree">Employee Degree:</label>
						<input class="New_Working" type="text" id="Degree" v-model="currentEmployee.Degree_Id" required>

						<!-- Department -->
						<label class="Working" for="Department">Employee Department:</label>
						<select class="New_Working" id="Department" v-model="currentEmployee.Departemnt_Id" required>
							<option v-for="department in departments" :value="department.Id" :key="department.Id">
								{{ department.Name }}
							</option>
						</select>

						<!-- Degree -->
						<label class="Working" for="Degree">Employee Degree:</label>
						<select class="New_Working" id="Degree" v-model="currentEmployee.Degree_Id" required>
							<option v-for="degree in degrees" :value="degree.Id" :key="degree.Id">
								{{ degree.Name }}
							</option>
						</select>

						<label class="Working" for="Salary">Employee Salary:</label>
						<input class="New_Working" type="text" id="Salary" v-model="currentEmployee.Salary" required>
					</div>
				</div>
				<div class="modal-edit-discard-buttons">
					<button class="submit-btn" @click="editEmployee">Submit</button>
					<button class="cancel-btn" @click="showEditModal = false">Cancel</button>
				</div>
			</div>
		</div>
		<!-- Delete Modal -->
		<div v-if="showDeleteModal">
			<div class="modal">
				<div class="modal-content-delete">
					<div class="modal-description-and-close">
						<h2>Delete employee</h2>
						<span class="close" @click="showDeleteModal = false">&times;</span>
					</div>
					<p>Are you sure you want to delete employee {{ this.currentEmployee.Name }}?</p>
					<div class="modal-edit-discard-buttons">
						<button class="submit-btn" @click="deleteEmployee">Yes</button>
						<button class="cancel-btn" @click="showDeleteModal = false">No</button>
					</div>
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
			searchQuery: '',
			departments: [],
			degrees: [],
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
			this.currentEmployee = { ...employee };
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
			this.currentEmployee = { ...employee };
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
		fetchDepartments() {
			axios.get('http://localhost:1234/get_all_departments')
				.then(response => {
					this.departments = response.data;
				})
				.catch(error => {
					console.error('Error fetching departments:', error);
				});
		},
		fetchDegrees() {
			axios.get('http://localhost:1234/get_all_degrees')
				.then(response => {
					this.degrees = response.data;
				})
				.catch(error => {
					console.error('Error fetching degrees:', error);
				});
		},
		getDepartmentName(departmentId) {
			const department = this.departments.find(dept => dept.Id === departmentId);
			return department ? department.Name : 'Unknown';
		},
		getDegreeName(degreeId) {
			const degree = this.degrees.find(deg => deg.Id === degreeId);
			return degree ? degree.Name : 'Unknown';
		},
	},
	mounted() {
		this.fetchEmployees();
		this.fetchDepartments();
		this.fetchDegrees();
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
	box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
}

.employees-table thead tr {
	background-color: #FF8FA3;
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
	border-bottom: 2px solid #FF8FA3;
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
	background: #ffccd5;
	padding: 25px;
	border-radius: 10px;
	width: 50%;
	height: 520px;
}

.modal-content-delete {
	background: #ffccd5;
	padding: 25px;
	border-radius: 10px;
	width: 50%;
	height: 175px;
}

.modal-content input {
	background-color: #fff0f3;
	border: 1px solid #ff4d6d;
	padding: 8px;
	margin: 10px 0;
}

.modal-container {
	max-height: 400px;
	overflow-y: auto;
}


/* Stylizowanie suwaka */
.modal-container::-webkit-scrollbar {
	width: 10px;
	/* Szerokość suwaka */
}

.modal-container::-webkit-scrollbar-track {
	background: #FFF0F3;
	/* Kolor tła toru suwaka */
}

.modal-container::-webkit-scrollbar-thumb {
	background: #FF758F;
	/* Kolor suwaka */
}

.modal-container::-webkit-scrollbar-thumb:hover {
	background: #C9184A;
	/* Kolor suwaka przy najechaniu */
}

.modal-description-and-close {
	display: grid;
	grid-template-columns: 99% 1%;
}

.modal-sumbmit-discard-buttons {
	margin-top: 10px;
	margin-bottom: 10px;
	display: grid;
	grid-template-columns: 50% 50%;
}

.close {
	float: right;
	cursor: pointer;
}

.inputs-and-labels-container {
	display: flex;
	flex-direction: column;
	width: 98%;
}

.Working {
	font-size: 150%;
}

.New_Working {
	height: 20px;
	margin-bottom: 15px;

}

.modal-edit-discard-buttons {
	margin-top: 10px;
	margin-bottom: 10px;
	display: grid;
	grid-template-columns: 50% 50%;
}
</style>