
$(document).ready(function(){


	/* ---- Countdown timer ---- */
	/* ---- Change timestamp to Wedding Date ---- */

	$('#counter').countdown({
		timestamp : (new Date(2021,0,1)).getTime()
	});


	/* ---- Animations ---- */

	$('#links a').hover(
		function(){ $(this).animate({ left: 3 }, 'fast'); },
		function(){ $(this).animate({ left: 0 }, 'fast'); }
	);

	$('footer a').hover(
		function(){ $(this).animate({ top: 3 }, 'fast'); },
		function(){ $(this).animate({ top: 0 }, 'fast'); }
	);




});
