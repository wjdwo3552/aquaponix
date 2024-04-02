// Highcharts 그래프 초기 설정
var chart = Highcharts.chart('container', {
    chart: {
        type: 'line'
    },
    title: {
        text: 'Temperature Data'
    },
    xAxis: {
        categories: []
    },
    yAxis: {
        title: {
            text: 'Temperature (°C)'
        }
    },
    series: [{
        name: 'Temperature',
        data: []
    }]
});

// 데이터 업데이트 함수
function updateChartData() {
    $.get('test.csv', function(csv) {
        var data = csv.split('\n').map(function(line) {
            return line.split(',');
        });

        var categories = [];
        var temperatures = [];

        for (var i = 1; i < data.length; i++) {
            categories.push(data[i][1]);
            temperatures.push(parseFloat(data[i][2]));
        }

        // 새로운 데이터로 그래프 업데이트
        chart.xAxis[0].setCategories(categories);
        chart.series[0].setData(temperatures);

        // 일정 시간 간격으로 데이터 업데이트
        setTimeout(updateChartData, 5000); // 5초마다 업데이트
    });
}

// 초기 데이터 업데이트 호출
updateChartData();