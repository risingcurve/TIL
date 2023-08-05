function onGeoOk(position) {
  const lat = position.coords.latitude;
  const lon = position.coords.longitude;
  const WEATHER_API = config.API_KEY
  const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${WEATHER_API}&units=metric`;
  fetch(url)
    .then(res => res.json())
    .then(data => {
      const weather = document.querySelector('#weather span:first-child');
      const city = document.querySelector('#weather span:last-child');
      weather.innerText = data.name;
      city.innerText = `${data.weather[0].main} / ${data.main.temp}`;
  });
}

function onGeoError() {
  alert("Can't find you. No weather for you.");
}


navigator.geolocation.getCurrentPosition(onGeoOk,onGeoError);