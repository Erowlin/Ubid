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