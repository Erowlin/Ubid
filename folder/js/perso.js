$(document).ready(function(){

	var btnOpenVolet = document.getElementById('btnOpenVolet');
	var btnCloseVolet = document.getElementById('btnCloseVolet');
	var timerAnim = 0.5;


	$('#btnOpenVolet').click(function(){
		if( document.body.clientWidth < 768 ){
			TweenMax.to("#voletAction", timerAnim, {height:"100%"});
		}else{
			TweenMax.to("#voletAction", timerAnim, {height:"300px"});
		}
		btnOpenVolet.style.display = "none";
		btnCloseVolet.style.display = "block";
	return false;  
	});
	$('#btnCloseVolet').click(function(){
		TweenMax.to("#voletAction", timerAnim, {height:50});
		btnCloseVolet.style.display = "none";
		btnOpenVolet.style.display = "block";	
	return false;  
	});
	

	// Supprimer quand travail terminé
	btnOpenVolet.click();

});