// Owl carousel Image Media Section

$('.js-carousel').owlCarousel({
	loop:true,
	autoplay:true,
	stagePadding:7,
	margin:20,
	animateOut: 'fadeOut',
	animateIn: 'fadeIn',
	nav:true,
	autoplayHoverPause:true,
	items:3,
	navText: ["<span class='fa fa-chevron-left'</span>","<span class='fa fa-chevron-right'</span>"],
	responsive:{
		0:{
		  items:1,
		  nav:false		
		},
		600:{
		  items:2,
		  nav:false				
		},
		1000:{
		  items:3,
		  nav:true
		  loop:false	
		}
	}

});
