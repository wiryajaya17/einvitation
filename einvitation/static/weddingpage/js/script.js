
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

	$("#my_audio").get(0).play();
	$('#myModal').modal('show');
	$('#tutup').click(function () {
        $("#my_audio").get(0).play();
    });
	$('#buka').click(function () {
	       $("#my_audio").get(0).play();
	});

});
