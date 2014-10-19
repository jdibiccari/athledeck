function highlight() {
  var parser = document.createElement('a');
  parser.href = document.URL;
  var page = parser.pathname;
  $('li a[href="' + page + '"]').parent().addClass('active');
}

$(document).ready(function() {

  highlight();
  
});