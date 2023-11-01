$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (data) => {
  const translation = data.hello;
  $('#hello').text(translation);
});
