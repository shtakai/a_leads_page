$(document).ready(function() {
  console.log('emit');
  $('.container .input-group.date').datepicker({
    format: "yyyy-mm-dd"
  });
 $('form').submit(function() {
    console.log('submit-', $(this));
    //$('#result').html('<img src="/static/img/default.gif">');
    // load up any gif you want, this will be shown while user is waiting for response
    //$.post($(this).attr('action'), $(this).serialize(), function(res) {
       //pay careful attention to the response object
      //var html_string = '';
      //if(res.routes.length == 0){
        //html_string += '<h4>route not found</h4>';
      //}else{
        //html_string += '<ol>'
        //for (var i in res.routes[0].legs[0].steps) {
          //html_string += '<li>' +res.routes[0].legs[0].steps[i].html_instructions + '</li>';
        //}
        //html_string += '</ol>'
      //}
      //$('#result').html(html_string);
    //}, 'json');
    // don't forget, without it the page will refresh
    //return false;
  });
});
