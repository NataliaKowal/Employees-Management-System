# Description

This project was developed using a combination of modern technologies and frameworks. The front-end is built with <strong> Vue.js </strong>,providing a dynamic and responsive user interface. On the server side, <strong>Flask </strong>, a lightweight web application framework written in <strong> Python</strong>, is used to handle requests and serve data. Data persistence is achieved through <strong> SQLite </strong>, a self-contained, high-reliability, embedded, full-featured, public-domain, SQL database engine.

# Front-end

The Front-end Project is a comprehensive system for managing company data, including employees, departments, and academic degrees. It consists of an HTML template for structure, a JavaScript script for future logic, and CSS styles for aesthetics and responsiveness. Users can view, filter, and manage data through interfaces with modals for adding, editing, and deleting records. The system uses axios for server communication and CSS for styling. To set up the project, clone the repository, install dependencies, and run the development server.

## Home Page

The Company Employee Database Management System consists of three main sections: the HTML template, the JavaScript script, and the CSS styles. The HTML template includes a welcome message for system users, displayed on the HomePage tab. The JavaScript script is currently empty but may contain application logic in the future, managing user interactions and communication with the database. The CSS styling includes importing the Poppins font from Google Fonts, styling the main container of the application, aligning and styling the welcome message, as well as styling the navigation and navigation links. The styling ensures an aesthetic appearance and responsiveness of the application.

![test.img](./img/home.png)

## View of the employees

The Employee Management System is designed to provide a user-friendly interface for managing employee data. Users can view a table of employee details, filter the list by entering a search query, and use modals to add, edit, or delete employee records. The system includes data binding and computed properties to dynamically filter employees based on the search query. Key methods facilitate fetching employee records, adding new employees, editing existing data, and deleting records. The application also fetches department and degree data from the server and provides utility methods to retrieve department and degree names based on their IDs. The interface is styled using CSS to ensure responsiveness and an attractive appearance, utilizing grid layouts, button transitions, and custom scrollbars for modals. The project relies on axios for making HTTP requests to the server. To set up the project, clone the repository, install dependencies, and run the development server. This system offers a comprehensive and functional solution for efficient employee data management.

![test.img](./img/add.png)

# Functionality of the "Add New Employee" Button
The "Add New Employee" button, displayed in the provided images, serves to open a modal form where users can input details for a new employee. This modal form includes fields for the employee's name, surname, PESEL, department, degree, room number, and salary. Upon filling out the form and clicking the "Submit" button, the entered data is sent to the server to create a new employee record. If the user decides not to add a new employee, they can click the "Cancel" button to close the modal without saving any changes. This feature ensures that users can efficiently add new employees to the system while maintaining data integrity and ease of use.

![test.img](./img/add_new.png)

![test.img](./img/add2.png)

## Departments View

The Department Management System provides a user-friendly interface for managing department data. Users can view a table of department details, filter the list by entering a search query, and use modals to add, edit, or delete department records. The system includes data binding and computed properties to dynamically filter departments based on the search query. Key methods facilitate fetching department records, adding new ones, editing existing data, and deleting records. The application also fetches data from the server, ensuring information is up-to-date. The interface is styled using CSS to ensure responsiveness and an aesthetic appearance, with grid layouts, button transitions, and custom scrollbars for modals. The project relies on axios for making HTTP requests to the server. To set up the project, clone the repository, install dependencies, and run the development server. This system offers a comprehensive and functional solution for efficient department data management.

![test.img](./img/Departments_View.png)

## Employee Education Search

This page is used for searching and managing employee academic degrees. Users can view a table of degree data, filter the list by entering a search query, and use modals to add, edit, or delete degree records. The system includes data binding and computed properties to dynamically filter degrees based on the search query. Key methods facilitate fetching degree records, adding new ones, editing existing data, and deleting records. The application also fetches data from the server, ensuring information is up-to-date. The interface is styled using CSS to ensure responsiveness and an aesthetic appearance, with grid layouts, button transitions, and custom scrollbars for modals. The project relies on axios for making HTTP requests to the server. To set up the project, clone the repository, install dependencies, and run the development server. This system offers a comprehensive and functional solution for efficient management of employee academic degree data.

![tekst alternatywny jak nie ma takiego zdjecia](./img/employee.png)
