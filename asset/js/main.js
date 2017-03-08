
// sidebar
;(function(global, $) {
	$(document).ready(function() {
		var sidebar = {
			toggle: function(){
				$('.ui.sidebar')
				  .sidebar('toggle')
				;
			}
		};

		var btnSidebar = '.menu-btn';
		$(document).on('click', btnSidebar, function(evt) {
			evt.preventDefault();
			sidebar.toggle();
		});
	});
})(window, jQuery);


// not found
;(function(global, $) {
	$(document).ready(function() {
		var pnlNotFound = '.pnl-not-found';
		$(pnlNotFound).show('slide');
	});
})(window, jQuery);


// scroll to top
;(function(global, $) {
	var ui = {
		scrollToTop: function() {
			$('body').velocity('scroll', {duration: 1000, easing: 'spring'}); //http://julian.com/research/velocity/#scroll
		}
	};

	$(document).ready(function() {

		var btnTop = '.ui-btn-top';
		var btnTopHide = '.ui-btn-top-hide';

		$(btnTopHide).hide();

		$(document).on('click', btnTop, function(evt) {
			evt.preventDefault();
			ui.scrollToTop();
		});

		$(document).on('click', btnTopHide, function(evt) {
			evt.preventDefault();
			ui.scrollToTop();
		});

		$(window).on('scroll', function(){
			if ($(this).scrollTop() > 100) {
				$(btnTopHide).fadeIn();
			} else {
				$(btnTopHide).fadeOut();
			}
		});

	});
	global.ui = ui;
})(window, jQuery);
