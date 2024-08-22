<template>
  <div>
    <div id="content-wrapper"></div>
    <h1>This is an about page</h1>
    <div class="project-description">
      <p>I developed this project using a combination of modern technologies and frameworks. The front-end is built with <strong>Vue.js</strong>, providing a dynamic and responsive user interface.On the server side, <strong>Flask</strong>, a lightweight web application framework written in Python, is used to handle requests and serve data. Data persistence is achieved through <strong> SQLite </strong>, a self-contained, high-reliability, embedded, full-featured, public-domain, SQL database engine. </p>
      <p>The entire project is available on GitHub under the name "Employees-Management-System": <a href="https://github.com/NataliaKowal"> <strong> GitHubLink </strong></a>.</p>
    </div>
  </div>
</template>
<script>

</script>

<style>

#content-wrapper {
  max-width: 800px;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
}

.project-description {
  max-width: 1580px;
  margin-left: 10px;
  margin-right: -15px;
  padding: 20px;
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  text-align: justify;
  line-height: 1.6;
}

nav {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: start;
  padding: 20px;
  background-color: #c9184A; 
  color: white;
  height: 100vh;
  width: 200px; 
}

nav a {
  font-weight: bold;
  color: white;
  padding: 10px;
  text-decoration: none;
  transition: background-color 0.3s;
}

nav a:hover {
  background-color: #FF8FA3; 
}

nav a.router-link-exact-active {
  background-color: #FF8FA3; 
  color: white;
}

h1 {
  text-align: center; 
  margin-top: 20px; 
  width: 100%; 
}
</style>

