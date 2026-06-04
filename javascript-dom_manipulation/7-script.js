const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch(url)
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    const listMovies = document.querySelector('#list_movies');
    const movies = data.results;

    for (const movie of movies) {
      const newItem = document.createElement('li');
      newItem.textContent = movie.title;
      listMovies.appendChild(newItem);
    }
  });
