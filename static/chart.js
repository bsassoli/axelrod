var ctx = document.getElementById('myChart');
/* var popData = JSON.parse('{{ dataJS | tojson | safe}}'); */
var popData = {{ dataJS.data }};
/* var popData = {
  datasets: [{
    label: ['Deer Population'],
    data: [{
      x: 100,
      y: 0,
      r: 10
    }, {
      x: 60,
      y: 30,
      r: 20
    }, {
      x: 40,
      y: 60,
      r: 25
    }, {
      x: 80,
      y: 80,
      r: 50
    }, {
      x: 20,
      y: 30,
      r: 25
    }, {
      x: 0,
      y: 100,
      r: 5
    }],
    backgroundColor: "#FF9966"
  }]
}; 
*/
var bubbleChart = new Chart(ctx, {
    type: 'bubble', 
    data: popData
});
