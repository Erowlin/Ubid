$(document).ready(function(){

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


    var btnOpenVoletEspacePerso = document.getElementById('btnOpenVoletEspacePerso');
    var btnCloseVoletEspacePerso = document.getElementById('btnCloseVoletEspacePerso');
    var espacePerso = document.getElementById('rowEspacePerso');
    var timerAnim = 0.5;

    $('#btnOpenVoletEspacePerso').click(function(){
        if( document.body.clientWidth < 768 ){
            TweenMax.to("#voletAction", timerAnim, {height:"100%"});
        }else{
            TweenMax.to("#voletAction", timerAnim, {height:"300px"});
        }
        btnOpenVoletEspacePerso.style.display = "none";
        btnCloseVoletEspacePerso.style.display = "block";
        return false;
    });
    $('#btnCloseVoletEspacePerso').click(function(){
        TweenMax.to("#voletAction", timerAnim, {height:"50px"});
        btnCloseVoletEspacePerso.style.display = "none";
        btnOpenVoletEspacePerso.style.display = "block";
        return false;
    });
    $('.rowEspacePerso').click(function(){
        if( document.body.clientWidth < 768 ){
            TweenMax.to("#voletAction", timerAnim, {height:"100%"});
        }else{
            TweenMax.to("#voletAction", timerAnim, {height:"300px"});
        }
        btnOpenVoletEspacePerso.style.display = "none";
        btnCloseVoletEspacePerso.style.display = "block";
        return false;
    });
});