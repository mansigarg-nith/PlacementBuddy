var ctx2 = document.getElementById('doughnut').getContext('2d');
var myChart2 = new Chart(ctx2, {
    type: 'doughnut',
    data: {
        labels: ['B.Tech', 'Dual Degree', 'M.Tech', 'M.Sc', 'MBA', 'B.Arch'],

        datasets: [{
            label: 'Placements',
            data: [417, 102, 81, 13, 07, 06],
            backgroundColor: [
                'rgb(252, 12, 27,1)',
                'rgb(31, 166, 0,1)',
                'rgb(2, 63, 114,1)',
                'rgb(255, 221, 1,1)',
                'rgb(255, 77, 186,1)',
                'rgb(67, 163, 254,1)'

            ],
            borderColor: [
                'rgb(252, 12, 27,1)',
                'rgb(31, 166, 0,1)',
                'rgb(2, 63, 114,1)',
                'rgb(255, 221, 1,1)',
                'rgb(255, 77, 186,1)',
                'rgb(67, 163, 254,1)'


            ],
            borderWidth: 1
        }]

    },
    options: {
        responsive: true
    }
});