var mymap = L.map('map').setView([35.6299,139.7949], 16);

L.tileLayer('http://tile.openstreetmap.jp/{z}/{x}/{y}.png', {
		maxZoom: 18,
		attribution: 'Map data &copy; ' 
			+ '<a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' 
			+ '<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>' 
}).addTo(mymap);

