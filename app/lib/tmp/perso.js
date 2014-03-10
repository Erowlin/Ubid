var timerAnim = 0.5;

$(document).on("click", "#btnOpenVolet", function() {
	$('#voletAction').animate({height: 310}, 200);
	$('#btnOpenVolet').toggle();
	$('#btnCloseVolet').toggle();
});
$(document).on("click", "#btnCloseVolet", function() {
	$('#voletAction').animate({height: 50}, 200);
	$('#btnOpenVolet').toggle();
	$('#btnCloseVolet').toggle();
});