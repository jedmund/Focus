// Define the map to use from MapBox
// This is the TileJSON endpoint copied from the embed button on your map
var url = 'http://a.tiles.mapbox.com/v3/jedmund.map-h3sojoku.jsonp';

// Make a new Leaflet map in your container div
var map = new L.Map('mapbox')  // container's id="mapbox"

// Center the map on Washington, DC, at zoom 15
.setView(new L.LatLng(40.758973066293485, -73.97727147899819), 13);

// Get metadata about the map from MapBox
wax.tilejson(url, function(tilejson) {
    map.addLayer(new wax.leaf.connector(tilejson));
});

var geojsonLayer = new L.GeoJSON();

var MarkerIcon = L.Icon.extend({
    iconUrl: '/static/img/marker.png',
    shadowUrl: '/static/img/marker-shadow.png'
});

// Simple geocoder function from Google
// https://developers.google.com/maps/documentation/javascript/geocoding

function codeAddress(address) {
    var geocoder = new google.maps.Geocoder();
    var result = '';

    geocoder.geocode({
        'address': address
    }, function(results, status) {
        if (status == google.maps.GeocoderStatus.OK) {
            result = results[0].geometry.location;
            addToMapBox(map, result);
        } else {
            alert("Geocode was not successful for the following reason: " + status);
        }
    });

    return result;
}

function addToMapBox(map, result) {
    var g = {
        lat: result.$a,
        lng: result.ab
    }

    var marker = new L.Marker(new L.LatLng(g.lat, g.lng), {icon: new MarkerIcon()});
    map.setView(new L.LatLng(g.lat, g.lng), 18);

    map.addLayer(marker);
}