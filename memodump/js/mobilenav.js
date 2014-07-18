+function ($) {

  $('.navbar-collapse').on('show.bs.collapse', function () {
    $('.navbar-mobile-toggle').togglejs('show');
  })

  $('.navbar-collapse').on('hidden.bs.collapse', function () {
    $('.navbar-mobile-toggle').togglejs('hide');
  })

}(jQuery);