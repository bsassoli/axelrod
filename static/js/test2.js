window.onload=function () {
        const config = {
            type: 'line',
            data: {
                labels: [],
                datasets: [{
                    label: "Cultures over time",
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
                    text: 'Simulating culture dissemination'
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
                            labelString: 'Step'
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

        const context = document.getElementById('canvas').getContext('2d');
        const lineChart = new Chart(context, config);

        let source;
        {% if max_value %}
            source = new EventSource("/chart-data?max-value={{ max_value }}&no_features={{ no_features }}&no_traits={{ no_traits }}");
        {% else %}
            source = new EventSource("/chart-data");
        {% endif %}


        source.onmessage = function (event) {
            const data = JSON.parse(event.data);
            if (config.data.labels.length === 20) {
                config.data.labels.shift();
                config.data.datasets[0].data.shift();
            }
            config.data.labels.push(data.time);
            config.data.datasets[0].data.push(data.value);
            lineChart.update();
            if (data.step === -1000) {
            change = document.getElementById("headline");
            change.innerText="Equilibrium reached";
            lineChart.stop();
            source.close();
            }
        }
    });