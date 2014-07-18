/*
 * toggle.js - toggle css class
 * Copyright 2014 dossist.
 * Licensed under GNU GPL3.
 */

if (typeof jQuery === 'undefined') { throw new Error('jQuery is required for toggle.js!') }
if ($.fn.emulateTransitionEnd === undefined) { throw new Error('Bootstrap is required for toggle.js!') }

+function ($) {

  function End() {
    this.removeClass('toggling');
  }

  function Show() {
    $this = $(this);

    if ($this.hasClass('on')) return;

    $this.addClass('toggling')
         .addClass('on')
         .one('bsTransitionEnd', $.proxy(End, $this))
         .emulateTransitionEnd(250);
  }

  function Hide() {
    $this = $(this);

    if (!$this.hasClass('on')) return;

    $this.addClass('toggling')
         .removeClass('on')
         .one('bsTransitionEnd', $.proxy(End, $this))
         .emulateTransitionEnd(250);
  }

  function Toggle() {
    $this = $(this);
    $this.hasClass('on') ? Hide.call(this) : Show.call(this);
  }

  function getTarget(elem) {
    var $elem = $(elem);
    var target = $elem.attr('data-target') || elem;
    return $(target);
  }

  function Plugin(option) {
    return this.each(function () {
      var $target = getTarget(this);

      var func = Toggle
      if (typeof option == 'string') {
        var options = {'show': Show, 'hide': Hide, 'toggle': Toggle};
        func = options[option] ? options[option] : Toggle;
      }

      $target.each(func);
    })
  }

  $.fn.togglejs = Plugin;

  function toggleHandler() {
    var $target = getTarget(this);
    $target.each(Toggle);
  }

  $('[data-toggle="toggle"]').click(toggleHandler);
}(jQuery);