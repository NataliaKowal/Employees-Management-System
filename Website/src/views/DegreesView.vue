<template>
	<div class="main">
		<h1>Employee Education Search</h1>
		<input type="text" v-model="searchQuery" placeholder="Filter..." />
		<button @click="showAddModal = true">Add New Degree</button>
		<table>
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
						<button @click="showEdit(degree)">Edit Degree</button>
						<button @click="showDelete(degree)">Delete Degree</button>
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
</style>
