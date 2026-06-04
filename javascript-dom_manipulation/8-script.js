document.addEventListener('DOMContentLoaded', function () {
    const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';
  
    fetch(url)
      .then(function (response) {
        return response.json();
      })
      .then(function (data) {
        const helloDiv = document.querySelector('#hello');
        helloDiv.textContent = data.hello;
      });
  });
