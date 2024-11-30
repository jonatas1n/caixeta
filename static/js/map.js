const map = L.map('map').setView([20, 0], 2);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 19,
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
}).addTo(map);

const imageBounds = [
  [25, -120],
  [40, 30],
];

const imageUrl = "/static/img/yellow.svg";

L.imageOverlay(imageUrl, imageBounds).addTo(map);

window.onresize = () => {
  map.invalidateSize();
};

fetch('https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json')
  .then(response => response.json())
  .then(geojsonData => {
    L.geoJSON(geojsonData, {
      style: () => ({
        color: '#FFA07A',
        weight: 1,
        fillColor: '#FFA07A',
        fillOpacity: 0.6,
      }),
      onEachFeature: (feature, layer) => {
        layer.on('click', () => {
          const countryId = feature.id || 'N/A';
          discoverCountry(countryId);
        });

        layer.bindTooltip(feature.properties.name, {
          sticky: true,
        });
      },
    }).addTo(map);
  })
  .catch(error => console.error('Erro ao carregar o GeoJSON:', error));