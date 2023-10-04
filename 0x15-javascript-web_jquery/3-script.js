const $ = window.$;
$('DIV#red_header').click(function () {
  $('header').last().addClass('red');
});
