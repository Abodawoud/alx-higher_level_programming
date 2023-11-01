$.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data) => {
  const movies = data.results;
  const $list = $('#list_movies');

  movies.forEach((movie) => {
    $list.append('<li>' + movie.title + '</li>');
  });
});
