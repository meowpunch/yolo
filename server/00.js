// Initialize and add the map
function initMap() {
  // The location of Uluru
  var uluru = {lat: 37.601653, lng: 126.649212};
  // CCTV 위치 위도 경도
  // The map, centered at Uluru
  var map = new google.maps.Map(
      document.getElementById('map'), {zoom: 18, center: uluru});
  // The marker, positioned at Uluru
  var marker = new google.maps.Marker({position: uluru, map: map});
}
