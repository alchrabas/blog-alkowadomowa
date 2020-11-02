$(function () {
  $('#content').find('img').each(function(index, img) {
    $(img).attr("href", $(img).attr("src")).css("cursor", "pointer");
    $(img).attr("title", $(img).attr("alt"));
    $(img).after("<p class='image-caption'>" + $(img).attr("alt") + "</p>");
  });
  $('#content').find('img').colorbox({
    maxWidth: "90%",
    maxHeight: "95%",
    transition: "fade",
    scrolling: false,
    close: "Zamknij"
  });
});
