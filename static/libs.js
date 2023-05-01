$(function(){
	function sendAjax(data, callback) {
		ShowLoading();
		$.ajax({
			url: dle_root + 'engine/mods/emoji_rating/ajax.php',
			type: 'POST',
			dataType: 'json',
			data: data
		})
		.done(callback)
		.fail(function(e) {
			DLEalert(e.responseText, 'Ошибка')
		})
		.always(function() {
			HideLoading()
		});
	}

	$(document).on('click', '.emoji-select-adv-trigger', function(e){
		//Меню дополнительных параметров на странице эмодзи
		e.preventDefault();
		$('.emoji-select-adv-area').slideToggle(200);
	}).on('click', 'body', function(e){
		//Скрыть меню при клике на странице
		if ($(e.target).parents('.emoji-select-adv').length < 1) {
			$('.emoji-select-adv-area').fadeOut(100);
		}
	}).on('click', 'a.rating-emoji-item', function(e){
		//Выбор эмодзи в новости
		e.preventDefault();
		e.stopPropagation();
		var $this = $(this);
		var data = {
			news_id: $this.parents('.rating-emoji').data('id'),
			emoji: $this.data('emoji'),
			hash: $this.parents('.rating-emoji').data('hash')
		};
		sendAjax(data, function(d){
			d['increse'] ? $this.addClass('active') : $this.removeClass('active');
			$('.rating-emoji-item').each(function(){
				var e = $(this).data('emoji');
				$(this).find('.rating-emoji-item-count').html(d['rating'][e]);
			})
		});
	})
})