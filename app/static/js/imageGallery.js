
var slideID = 1;

$(document).ready(function () {
    showSlide(slideID);
});

function plusSlide(n) {
    showSlide(slideID += n);
}

function currentSlide(n) {
    showSlide(slideID = n);
}

function showSlide(n) {
    var slides = $(".slide"),
        dots = $(".dot");
    if (n > $(slides).length) {
        slideID = 1;
    }
    if (n < 1) {
        slideID = $(slides).length;
    }
    $(slides).css("display", "none");
    dots.removeClass("white");
    $(slides[slideID - 1]).css("display", "block");
    $(dots[slideID - 1]).addClass("white");
}
