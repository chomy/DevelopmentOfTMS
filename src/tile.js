var mymap = L.map('map').setView([35.6299,139.7949], 2);

L.tileLayer('http://tile.openstreetmap.jp/{z}/{x}/{y}.png', {
		maxZoom: 18,
		attribution: 'Map data &copy; ' 
			+ '<a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' 
			+ '<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>' 
}).addTo(mymap);

L.tileLayer('http://tms.example.org/1.0.0/{z}/{x}/{y}.png', {
	maxZoom: 2,
	tms: true}).addTo(mymap);
