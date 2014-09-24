
$(function() {

	// Detect Browser Height
	var window_height = $(window).height();

	// Only set height for bigger screens
	if (window_height>1000) {

		$('.hero').height(window_height - 50);
	}
});