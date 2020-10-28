$(function () {
  $('#content').find('img').each(function(index, img) {
    $(img).attr("href", $(img).attr("src")).css("cursor", "pointer");
  });
  $('#content').find('img').colorbox({
    maxWidth: "90%",
    maxHeight: "95%",
    transition: "fade",
    scrolling: false
  });
});
