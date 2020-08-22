var app = new Vue({
  el: '#app',
  data: {
    staticValue: null,
    dynamicValue: null,
    startRequest: false
  },
  methods: {
    updateDynamicValue: function (data) {
      if(!this.startRequest) this.startRequest = true;
      this.dynamicValue = JSON.parse(data)
    }
  },
  mounted: function() {
    //http request for static value
    axios
      .get('http://localhost:8000/staticvalue')
      .then(response => (this.staticValue = response.data))
    //websocket request for dynamic value
    this.connection = new WebSocket("ws://localhost:8000/dynamicvalue")
    this.connection.onmessage = function(event) {
      app.updateDynamicValue(event.data)
    }
  }
})