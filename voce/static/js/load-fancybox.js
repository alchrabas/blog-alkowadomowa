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

$(function () {
  $('#content').find('img').not('.ignore-image').each(function (index, img) {
    $(img).attr("href", $(img).attr("src")).css("cursor", "pointer");
    $(img).attr("title", $(img).attr("alt"));
    $(img).after("<p class='image-caption'>" + $(img).attr("alt") + "</p>");
    $(img).fancybox({
      lang: "pl",
      i18n: i18n,
      caption: function (instance, item) {
        return $(this).attr("title");
      },
    });
  });
});
