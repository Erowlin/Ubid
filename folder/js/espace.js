$(document).ready(function(){

    $.fn.editable.defaults.mode = 'inline';

    // Permet l'action du clic sur les liens des blocs objets dans la vue mes enchères.
    $('.bid_content').hover(
        // lorsqu'on hover et qu'on clique sur le lien, on change le margin pour faire apparaitre la deuxieme partie
        function(){
            $(this).find('.action_box').on('click', function(event){
                event.preventDefault();
                $(this).closest('.main').css('marginTop', '-400px');
                return false;
            });
        },
        // lorsqu'on hover plus, le margin revient à 0
        function(){
            $(this).find('.main').css('marginTop', '0px');
        });

    // slideToggle pour faire apparaitre les légendes pour le bloc des enchères avec changement du + en -
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

    // bete animation pour cacher les messages qu'on ne souhaite plus voir.
    $('.messagerie .close_message').on('click', function(){
        $(this).parent().slideToggle();
        // penser à implémenter une méthode pour supprimer le fil dans la bdd
    });


    var btnOpenVoletEspacePerso = document.getElementById('btnOpenVoletEspacePerso');
    var btnCloseVoletEspacePerso = document.getElementById('btnCloseVoletEspacePerso');
    var espacePerso = document.getElementById('rowEspacePerso');
    var timerAnim = 0.5;

    $('#btnOpenVoletEspacePerso').click(function(){
       TweenMax.to("#voletAction", timerAnim, {height:"100%"});
        btnOpenVoletEspacePerso.style.display = "none";
        btnCloseVoletEspacePerso.style.display = "block";

        if( document.body.clientWidth < 768 ){
            $('#voletAction').css('overflow', 'auto');
        }else{
            $('#voletAction').css('overflow', 'visible');
        }
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
        btnOpenVoletEspacePerso.style.display = "none";
        btnCloseVoletEspacePerso.style.display = "block";

        if( document.body.clientWidth < 768 ){
            $('#voletAction').css('overflow', 'auto');
        }else{
            $('#voletAction').css('overflow', 'visible');
        }
    });

    $("select[name='adresselist']").selectpicker({style: 'btn-primary', menuStyle: 'dropdown-inverse'});
    $("select[name='payementlist']").selectpicker({style: 'btn-primary', menuStyle: 'dropdown-inverse'});

    // Pour le moment en dur, à modifier plus tard pour de l'affichage dynamique
    // Change les infos du formulaire des paiements en fonction du choix du dropdown
    $('.infoPayementAjout').find("li a").click(function(){
        //alert($(this).html());
        //console.log($(this).parent().attr('rel'));
        if($(this).parent().attr('rel') == 1)
        {
            $('#donnees_bancaires .infoPayementNumero p:last-child').html('****.****.**45');
            $('#donnees_bancaires .infoPayementNom p:last-child').html('Steve Benedick');
            $('#donnees_bancaires .infoPayementDateExpiration p:last-child').attr('data-value', '14-05');
            $('#donnees_bancaires .infoPayementCrypto p:last-child').html('***');

            startEditable();
        }
        else if ($(this).parent().attr('rel') == 2)
        {
            $('#donnees_bancaires .infoPayementNumero p:last-child').html('****.****.**71');
            $('#donnees_bancaires .infoPayementNom p:last-child').html('Hugo Zilliox');
            $('#donnees_bancaires .infoPayementDateExpiration p:last-child').attr('data-value', '14-12');
            $('#donnees_bancaires .infoPayementCrypto p:last-child').html('***');

            startEditable();
        }
        else
        {
            alert('Une modal s\'ouvre pour ajouter une nouvelle carte');
        }
    });

    // Pour le moment en dur, à modifier plus tard pour de l'affichage dynamique
    // Change les infos du formulaire des paiements en fonction du choix du dropdown
    $('.infoAdresseAjout').find("li a").click(function(){
        //alert($(this).html());
        console.log($(this).parent().attr('rel'));
        if($(this).parent().attr('rel') == 1)
        {
            console.log($('#donnees_adresse .infoAdresseRue p:last-child').html());
            $('#donnees_adresse .infoAdresseRue p:last-child').html('54 rue de la gare');
            $('#donnees_adresse .infoAdresseVille p:last-child').html('Strasbourg');
            $('#donnees_adresse .infoAdressePays p:last-child').html('France');
            $('#donnees_adresse .infoAdresseCodePostal p:last-child').html('67000');

            startEditable();
        }
        else if ($(this).parent().attr('rel') == 2)
        {
            $('#donnees_adresse .infoAdresseRue p:last-child').html('28 rue de la mairie');
            $('#donnees_adresse .infoAdresseVille p:last-child').html('Colmar');
            $('#donnees_adresse .infoAdressePays p:last-child').html('France');
            $('#donnees_adresse .infoAdresseCodePostal p:last-child').html('68000');

            startEditable();
        }
        else
        {
            alert('Une modal s\'ouvre pour ajouter une nouvelle adresse');
        }
    });

    $('.infoAdresseAjout').find("li:last-child a").append("<span class=\"pull-right glyphicon glyphicon-plus\"></span>");
    $('.infoAdresseAjout').find("li:last-child a").click(function(){
        /* ouverture modale ajout moyen de payement */
    });

    $('.infoPayementAjout').find("li:last-child a").append("<span class=\"pull-right glyphicon glyphicon-plus\"></span>");
    $('.infoPayementAjout').find("li:last-child a").click(function(){
        /* ouverture modale ajout moyen de payement */
    });

    $('#photo_content').on('click',function(){
        //alert(':)')
    });

    function startEditable(){
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

        $('.infoAdresseRue p:last-child').editable({
            highlight:  'invisible'
        });

        $('.infoAdresseVille p:last-child').editable({
            highlight:  'invisible'
        });

        $('.infoAdresseCodePostal p:last-child').editable({
            highlight:  'invisible'
        });

        $('.infoAdressePays p:last-child').editable({
            highlight:  'invisible'
        });

        $('.infoPayementNumero p:last-child').editable({
            highlight: 'invisible'
        });

        $('.infoPayementNom p:last-child').editable({
            highlight: 'invisible'
        });

        $('.infoPayementDateExpiration p:last-child').editable({
            highlight: 'invisible',
            combodate: {
                    minYear: 2014,
                    maxYear: 2020
                }
        });

        $('.infoPayementCrypto p:last-child').editable({
            highlight: 'invisible'
        });
    };
   startEditable();
});