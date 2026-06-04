const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

fetch(url)
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    const characterDiv = document.querySelector('#character');
    characterDiv.textContent = data.name;
  });
