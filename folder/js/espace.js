
$('.bid_content').hover(
	function(){
		$(this).find('.action_box').on('click', function(event){
			event.preventDefault();
			$(this).closest('.main').css('marginTop', '-300px');
			return false;
		});
	},
	function(){
		$(this).find('.main').css('marginTop', '0px');
	});

$(document).ready(function(){

    var btnOpenVoletEspacePerso = document.getElementById('btnOpenVoletEspacePerso');
    var btnCloseVoletEspacePerso = document.getElementById('btnCloseVoletEspacePerso');
    var espacePerso = document.getElementById('rowEspacePerso');
    var timerAnim = 0.5;

    $('#btnOpenVoletEspacePerso').click(function(){
       TweenMax.to("#voletAction", timerAnim, {height:"100%"});
       $('#voletAction').css('overflow', 'visible');
        btnOpenVoletEspacePerso.style.display = "none";
        btnCloseVoletEspacePerso.style.display = "block";

    });
    $('#btnCloseVoletEspacePerso').click(function(){
        TweenMax.to("#voletAction", timerAnim, {height:"45px"});
        btnCloseVoletEspacePerso.style.display = "none";
        btnOpenVoletEspacePerso.style.display = "block";
        $('#voletAction').css('overflow', 'hidden');
        return false;
    });
    $('.rowEspacePerso').click(function(){
        TweenMax.to("#voletAction", timerAnim, {height:"100%"});
        $('#voletAction').css('overflow', 'visible');
        btnOpenVoletEspacePerso.style.display = "none";
        btnCloseVoletEspacePerso.style.display = "block";
    });

    $("select[name='adresselist']").selectpicker({style: 'btn-primary', menuStyle: 'dropdown-inverse'});
    $("select[name='payementlist']").selectpicker({style: 'btn-primary', menuStyle: 'dropdown-inverse'});

    $('.infoAdresseAjout').find("li:last-child a").append("<span class=\"pull-right glyphicon glyphicon-plus\"></span>");
    $('.infoAdressetAjout').find("li:last-child a").click(function(){
        /* ouverture modale ajout adresse */
    });

    $('.infoPayementAjout').find("li:last-child a").append("<span class=\"pull-right glyphicon glyphicon-plus\"></span>");
    $('.infoPayementAjout').find("li:last-child a").click(function(){
        /* ouverture modale ajout moyen de payement */
    });
});

