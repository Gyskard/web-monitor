<template>
  <div id="app">
    <h2>Vue.js WebSocket Tutorial</h2> 
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function() {
    return {
      connection: null
    }
  },
  created: function() {
    this.connection = new WebSocket("ws://localhost:8000/dynamicvalue")
    this.connection.onmessage = function(event) {
      console.log(event)
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>