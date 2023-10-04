const $ = window.$;
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (const i in data.results) {
    $('<li>' + i.title + '<li>').appendTo($('UL#list_movies'));
  }
});
