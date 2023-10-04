// Add a click event handler to the 'INPUT' element with the ID 'btn_translate'
// When the button is clicked, call the 'translate' function
// Add a focus event handler to the 'INPUT' element with the ID 'language_code
$('document').ready(function () {
  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (e) {
      if (e.keyCode === 13) {
        translate();
      }
    });
  });
});

function translate () {
  const url = 'https://www.fourtonfish.com/hellosalut/hello/?';
  $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
    $('div#hello').html(data.hello);
  });
}
