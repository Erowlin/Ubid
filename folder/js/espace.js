$(document).ready(function(){

    $.fn.editable.defaults.mode = 'inline';

    $('.bid_content').hover(
        function(){
            $(this).find('.action_box').on('click', function(event){
                event.preventDefault();
                $(this).closest('.main').css('marginTop', '-400px');
                return false;
            });
        },
        function(){
            $(this).find('.main').css('marginTop', '0px');
        });

    $('#legende').on('click', function(){
        $('#content_legende').slideToggle();
        if($('#legende').html() == "+ Légende")
        {
            $('#legende').html('&mdash; Légende');
        }
        else
        {
            $('#legende').html('+ Légende');
        }
    });

    $('.messagerie .close_message').on('click', function(){
        $(this).parent().slideToggle();
    });


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
        TweenMax.to("#voletAction", timerAnim, {height:"50px"});
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

    $('.infoPayementAjout').find("li a").click(function(){
        alert($(this).html());
    });

    $('.infoAdresseAjout').find("li:last-child a").append("<span class=\"pull-right glyphicon glyphicon-plus\"></span>");
    $('.infoAdresseAjout').find("li:last-child a").click(function(){
        /* ouverture modale ajout moyen de payement */
    });

    $('.infoPayementAjout').find("li:last-child a").append("<span class=\"pull-right glyphicon glyphicon-plus\"></span>");
    $('.infoPayementAjout').find("li:last-child a").click(function(){
        /* ouverture modale ajout moyen de payement */
    });

    $('.infoPersoPseudo p').editable({
        highlight:  'invisible'
    });

    $('.infoPersoCouriel p').editable({
        highlight:  'invisible'
    });

    $('.infoPersoNumDomicile p:last-child').editable({
        highlight:  'invisible'
    });

    $('.infoPersoNumMobile p:last-child').editable({
        highlight:  'invisible'
    });
});