$(document).ready(function () {
  // Function to fetch translation
  function fetchTranslation () {
    const languageCode = $('#language_code').val();
    const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + languageCode;

    $.get(apiUrl, function (data) {
      $('#hello').text(data.hello);
    }).fail(function () {
      $('#hello').text('Error: Unable to fetch translation.');
    });
  }

  // Fetch translation on button click
  $('#btn_translate').click(function () {
    fetchTranslation();
  });

  // Fetch translation on Enter key press in the input field
  $('#language_code').keypress(function (event) {
    if (event.which === 13) { // Enter key code
      event.preventDefault(); // Prevent the default action
      fetchTranslation();
    }
  });
});
