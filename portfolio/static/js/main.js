$(function() {
	smoothScroll(500);
});

function smoothScroll(time) {
	$('a[href^="#"]').on('click', function(evt) {
		var header = $( $(this).attr('href') );

		if (header.length) {
			evt.preventDefault();
			$('html, body').animate({
				scrollTop: header.offset().top
			}, time);
		}
	});
}