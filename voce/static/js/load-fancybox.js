var i18n = {
  pl: {
    CLOSE: "Zamknij",
    NEXT: "Następne",
    PREV: "Poprzednie",
    ERROR: "Treść nie może zostać wyświetlona. <br/> Spróbuj ponownie później.",
    PLAY_START: "Rozpocznij pokaz slajdów",
    PLAY_STOP: "Zatrzymaj pokaz slajdów",
    FULL_SCREEN: "Pełny ekran",
    THUMBS: "Miniatury",
    DOWNLOAD: "Pobierz",
    SHARE: "Udostępnij",
    ZOOM: "Przybliż"
  },
};
// Columns per row: fewest rows possible, filled as evenly as possible
function pickCols(count, maxCols) {
  if (count <= maxCols) return Math.max(count, 1); // single row
  var rows = Math.ceil(count / maxCols);
  return Math.ceil(count / rows);
}

$(function () {
  var MAX_COLS = 5;

  var $content = $('#content');
  var $galleries = $content.find('.gallery');
  var $imgs = $content.find('img').not('.ignore-image');

  // Lightbox attributes and captions for single images
  $imgs.each(function (i, img) {
    var $img = $(img);
    var $gallery = $img.closest('.gallery');
    var inGallery = $gallery.length > 0;

    // One group per gallery; a unique group per single image (no arrows)
    var group = inGallery
      ? 'gallery-' + $galleries.index($gallery)
      : 'single-' + i;

    $img.attr({
      href: $img.attr('src'),
      title: $img.attr('alt'),
      'data-thumb': $img.attr('src'),
      'data-fancybox': group
    }).css('cursor', 'pointer');

    // Caption below single images only
    if (!inGallery) {
      $img.after("<p class='image-caption'>" + $img.attr('alt') + "</p>");
    }
  });

  $imgs.fancybox({
    lang: 'pl',
    i18n: i18n,
    caption: function (instance, item) {
      return $(this).attr('title');
    },
    buttons: ['zoom', 'slideShow', 'thumbs', 'close']
  });

  // Caption below the whole gallery, from the data-caption attribute
  $galleries.filter('[data-caption]').each(function () {
    var text = $(this).attr('data-caption');
    $(this).after($("<p class='image-caption gallery-caption-all'></p>").text(text));
  });

  // Column count per gallery; a manual cols-N class takes precedence
  $galleries.each(function () {
    if (/\bcols-\d+\b/.test(this.className)) return;
    var count = $(this).find('img').length;
    this.style.setProperty('--cols', pickCols(count, MAX_COLS));
  });
});