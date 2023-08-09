// Store our API endpoint as queryUrl.
const queryUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson";

//Create the initial map showing the U.S.
let myMap = L.map("map", {
    center: [39.232, -106.0000],
    zoom: 5
});

//Create the base layers
let baseLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap);

let topo = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
    attribution: 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
});






//Create a style object
//let markerStyle = {
    //radius: 15,
    //color: 'black',
    //fillColor: '#006837',
    //fillOpacity: 0.75,
    //weight: 0.5

//};

function color(depth) {
            
    if (depth<20) {
        return '#ffffcc';
        //markerStyle.fillColor = '#ffffcc';
    }
    else if (depth<50) {
        return '#c7e9b4';
    }
    else if (fdepth<100) {
        return '#7fcdbb';
    }
    else if (depth<200) {
        return '#41b6c4';
    }
    else if (depth<300) {
        return '#2c7fb8';
    }
    else {
        return '#253494';
    }
};

// Perform a GET request to the query URL.
d3.json(queryUrl).then(function (data) {
    console.log(data.features);
    //let features = data.features;
    //createFeatures(data.features);
    let geoJson = L.geoJson().addTo(myMap);
    let features = data.features;
    //let earthquakeMarkers = [];
    let radiusArray = [];
    let depthArray = [];
    let latlngArray = [];
    //let features = earthquakeData.features;
    //Loop through earthquake data and extract required values
    for (let i=0;i<features.length;i++) {
        
        radiusArray.push(data.features[i].properties.mag);
        depthArray.push(features[i].geometry.coordinates[2]);
        latlngArray.push([features[i].geometry.coordinates[0],features[i].geometry.coordinates[1]]);
        
        
        let markerStyle = {
            radius: 5,
            color: 'black',
            fillColor: '#006837',
            //fillOpacity: 0.75,
            weight: 0.5
        
        };
        let earthquakes = L.circleMarker([features[i].geometry.coordinates[0],features[i].geometry.coordinates[1]],markerStyle).bindPopup("skldjfa").toGeoJSON();
        //markers.addLayer(L.circleMarker([features[i].geometry.coordinates[0],features[i].geometry.coordinates[1]],markerStyle)).bindPopup("skldjfa")
        //myMap.addLayer(earthquakes);

        //markers.addLayer(L.circleMarker(latlngArray[i],markerStyle)
        //.bindPopup(`<h3>${features[i].properties.place}</h3> <h2>Magnitude: ${features[i].properties.mag}</h2> <hr><p>${new Date(features[i].properties.time)}</p>`));
        
        //L.geoJSON(data, {pointToLayer: function(feature,latlng){
            //return new L.circleMarker(latlng, markerStyle).bindPopup(`<h3>${features[i].properties.place}</h3> <h2>Magnitude: ${features[i].properties.mag}</h2> <hr><p>${new Date(features[i].properties.time)}</p>`).addTo(myMap);
        //}});

        //myMap.addLayer(markers);
        
        //L.circleMarker(latlngArray[i], markerStyle)
        //.bindPopup(`<h3>${features[i].properties.place}</h3> <h2>Magnitude: ${features[i].properties.mag}</h2> <hr><p>${new Date(features[i].properties.time)}</p>`)
        //.addTo(myMap);
        //Create baseMaps object
        earthquakes.addTo(myMap);
        
        let baseMaps = {Street: baseLayer};
        //Create overlayMaps object
        let overlayMaps = {Earthquakes: earthquakes}; 
    
    
    
    }

   





});

    



    

    //console.log(radiusArray);
    //console.log(depthArray);
    //console.log(latlngArray);
    



//};
//Set up the legend
//let legend = L.control({position: "bottomright"});
//legend.addTo(myMap);

// Create a baseMaps object
//let baseMaps = {
    //Street:
    //Topography:
//};



// Create a layer control that contains our baseMaps and overlayMaps, and add them to the map.
//L.control.layers().addTo(myMap);