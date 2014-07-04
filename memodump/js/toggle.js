/*
 * toggle.js - toggle css class
 * Copyright 2014 dossist.
 * Licensed under GNU GPL3.
 */

if (typeof jQuery === 'undefined') { throw new Error('jQuery is required for toggle.js!') }

$(document).ready(function () {

  var $target = $('.toggle');

  if ($.fn.emulateTransitionEnd === undefined) {
    throw new Error('Bootstrap is required for toggle.js!');
  }

  function toggleEnd() {
    this.removeClass('toggling');
  }

  function toggleHandler() {
    $target.addClass('toggling');
    $target.toggleClass('active');
    $target.one('bsTransitionEnd', $.proxy(toggleEnd, $target))
           .emulateTransitionEnd(1000);
  }

  $('[data-toggle=toggle]').click(toggleHandler);
});