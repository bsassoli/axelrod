var ctx = document.getElementById("myChart");

var myChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: steps,
    datasets: [
      { 
        data: cultures      
    }
    ]
  }
});