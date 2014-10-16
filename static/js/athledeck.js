//JQuery not available in this file--look into why
$(document).ready(function() {
  $('ul.nav li').on('click', function(){
    this.addClass('active');
  });
});