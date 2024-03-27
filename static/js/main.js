// import * as $ from 'jquery';

$(() => {
	var circles = $('.circle');
	var index = 0;
	var text = $('.welcome-text');
	const messages = [
		{
			h1: 'This is our Store for all Your Electronic Needs',
			p: "Get the best deals on all electronics from our store.\nWe have a wide range of products from different brands. We offer the best prices and quality products."
		},
		{
			h1: 'All That which You Seek, And More',
			p: "Our Store contains Electronic devices From all over the world.\nShop at your leisure."
		},
		{
			h1: 'Ensuring Customers\' Comfort and Security',
			p: "Using the latest in Cyber Security Technologies, Purchase all that you want, from the comfort of your house, without worrying about fraud."
		},
	]
	var h1 = $(text[0]).children('h1')[0];
	var p = $(text[0]).children('p')[0];
	$(h1).html(messages[0].h1)
	$(p).html(messages[0].p)
	for (var i = 1; i < text.length; i++) {
		var h1 = $(text[i]).children('h1')[0];
		var p = $(text[i]).children('p')[0];
		$(h1).html(messages[i].h1)
		$(p).html(messages[i].p)
	}
	$(circles[index]).removeClass('light');
	$(circles[index]).addClass('dark');
	setInterval(() => {
		$(circles[index]).addClass('light');
		$(circles[index]).removeClass('dark');
		$(text[index]).addClass('hidden');
		index = (index + 1) % circles.length;
		$(text[index]).removeClass('hidden');
		$(circles[index]).removeClass('light');
		$(circles[index]).addClass('dark');
	}, 2000)
})


const showProduct = (id) => {
	window.location.href = `/product/${id}`;
}
