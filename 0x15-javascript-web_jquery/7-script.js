$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', (data) => {
  const characterName = data.name;

  $('DIV#character').text(characterName);
});
