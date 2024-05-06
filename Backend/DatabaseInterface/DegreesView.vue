<template>
	<div class="main">
		<h1>Employee Education Search</h1>
		<div class="filer-and-add-bar">
			<input class="filer-input" type="text" v-model="searchQuery" placeholder="Filter..." />
			<button class="add-record-button" @click="showAddModal = true">Add New Degree</button>
		</div>
		<table class="deegree-table">
			<thead>
				<tr>
					<th>Id</th>
					<th>Name</th>
					<th>Actions</th>
				</tr>
			</thead>
			<tbody>
				<tr v-for="degree in filteredDegrees" :key="degree.id">
					<td>{{ degree.Id }}</td>
					<td>{{ degree.Name }}</td>
					<td>
						<div class="edit-delete-container">
							<button class="edit-record-button" @click="showEdit(degree)">Edit Degree</button>
							<button class="delete-record-button" @click="showDelete(degree)">Delete Degree</button>
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
					<form @submit.prevent="addDegree">
						<label for="Name">Degree Name:</label>
						<input type="text" id="Name" v-model="newDegreeName" required>
						<button type="submit">Submit</button>
					</form>
				</div>
			</div>
		</div>
		<!-- Edit Modal -->
		<div v-if="showEditModal">
			<div class="modal">
				<div class="modal-content">
					<span class="close" @click="showEditModal = false">&times;</span>
					<form @submit.prevent="editDegree">
						<label for="Name">Degree Name:</label>
						<input type="text" id="Name" v-model="currentDegree.Name" required>
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
					<p>Are you sure you want to delete this degree: {{ currentDegree.Name }}?</p>
					<button @click="deleteDegree">Delete</button>
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
			degrees: [],
			searchQuery: '',
			showAddModal: false,
			showEditModal: false,
			showDeleteModal: false,
			currentDegree: {}
		};
	},
	computed: {
		filteredDegrees() {
			if (!this.searchQuery) {
				return this.degrees;
			}
			const query = this.searchQuery.toLowerCase();
			return this.degrees.filter(degree =>
				degree.Name.toLowerCase().includes(query) ||
				degree.id.toString().includes(query)
			);
		}
	},
	methods: {
		fetchDegrees() {
			axios.get('http://localhost:1234/get_all_degrees')
				.then(response => {
					this.degrees = response.data;
				})
				.catch(error => {
					console.error('Error fetching degrees:', error);
				});
		},
		addDegree() {
			axios.post('http://localhost:1234/add_degree', {
				Name: this.newDegreeName
			})
				.then(() => {
					this.showAddModal = false;
					this.currentDegree = {}; 
					this.fetchDegrees();
				})
				.catch(error => {
					console.error('Error adding new degree:', error);
				});
		},
		showEdit(degree) {
			this.currentDegree = {...degree};
			this.showEditModal = true;
		},
		editDegree() {
			axios.post(`http://localhost:1234/edit_degree`, {
				Name: this.currentDegree.Name,
				Id: this.currentDegree.Id
			})
				.then(() => {
					this.showEditModal = false;
					this.currentDegree = {}; 
					this.fetchDegrees();
				})
				.catch(error => {
					console.error('Error editing degree:', error);
				});
		},
		showDelete(degree) {
			this.currentDegree = {...degree};
			this.showDeleteModal = true;
		},
		deleteDegree() {
			axios.post(`http://localhost:1234/delete_degree`, {
				Id: this.currentDegree.Id
			})
				.then(() => {
					this.showDeleteModal = false;
					this.currentDegree = {}; 
					this.fetchDegrees();
				})
				.catch(error => {
					console.error('Error deleting degree:', error);
				});
		},
	},
	mounted() {
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

.filer-and-add-bar {
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

.deegree-table {
	width: 100%;
	border-collapse: collapse;
	margin: 10px 0;
	font-size: 0.9em;
	font-family: sans-serif;
	min-width: 400px;
	box-shadow: 0 0 20px rgba(0,0,0,0.15);
}

.deegree-table thead tr {
	background-color: #4386dd;
	color: #ffffff;
	text-align: left;
}

.deegree-table th,
.deegree-table td {
	padding: 12px 15px;
}

.deegree-table tbody tr {
	border-bottom: 1px solid #dddddd;
}

.deegree-table tbody tr:nth-of-type(even) {
	background-color: #f3f3f3;
}

.deegree-table tbody tr:last-of-type {
	border-bottom: 2px solid #4386dd;
}

.deegree-table tbody tr.active-row {
	font-weight: bold;
	color: #009879;
}

.deegree-table th:nth-child(1), 
.deegree-table tr:nth-child(1) {
	width: 20%;
}

.deegree-table th:nth-child(2), 
.deegree-table tr:nth-child(2) {
	width: 60%;
}

.deegree-table th:nth-child(3), 
.deegree-table tr:nth-child(3) {
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

.edit-record-button {
	padding-left: 10px;
	background-color: #d1cf3d;
	border: none;
	color: white;
	padding: 5px 15px;
	text-align: center;
	text-decoration: none;
	display: inline-block;
	font-size: 16px;
	margin: 0px 2px;
	cursor: pointer;
	transition: background-color 0.3s ease;
}

.edit-record-button:hover {
	background-color: #ebac00;
}

.delete-record-button {
	padding-left: 10px;
	background-color: #df4a4a; 
	color: white;
	padding: 5px 15px;
	text-align: center;
	text-decoration: none;
	display: inline-block;
	font-size: 16px;
	margin: 0px 2px;
	cursor: pointer;
	transition: background-color 0.3s ease;
}

.delete-record-button:hover {
	background-color: #9e1e1e;
}
</style>

