$(document).ready(function () {
    const config = {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: "Cultures",
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: [],
                fill: false,
            }],
        },
        options: {
            responsive: true,
            title: {
                display: true,
                text: 'AXELROD CULTURE DISSEMINATION MODEL'
            },
            tooltips: {
                mode: 'index',
                intersect: false,
            },
            hover: {
                mode: 'nearest',
                intersect: true
            },
            scales: {
                xAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Timestep'
                    }
                }],
                yAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'No. of cultures'
                    }
                }]
            }
        }
    };

    const context = document.getElementById('myChart').getContext('2d');

    const lineChart = new Chart(context, config);

    const source = new EventSource("/chart-data");

    source.onmessage = function (event) {
        const data = JSON.parse(event.data);
        console.log("Banzo")
        change = document.getElementById("headline"); 
        change.innerText=data.step;
        if (config.data.labels.length === 20) {
            config.data.labels.shift();
            config.data.datasets[0].data.shift();
        }
        config.data.labels.push(data.step);
        config.data.datasets[0].data.push(data.cultures);
        lineChart.update();
        if (data.step === -1000) {
            console.log("Banzai!!!!!!!")
            change = document.getElementById("headline"); 
            change.innerText="POLLO";
            lineChart.stop();
            source.close();
        }
    }
    
});