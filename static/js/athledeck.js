$(document).ready(function() {
  $('ul.nav li').on('click', function(e){
    e.default();
    $(this).addClass('active');
  });
});