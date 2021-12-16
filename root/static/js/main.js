(function($) {
  
  "use strict";

/* 
   CounterUp
   ========================================================================== */
    $('.counter').counterUp({
      time: 500
    });

/* 
   MixitUp
   ========================================================================== */
  $('#portfolio').mixItUp();

/* 
   Clients Sponsor 
   ========================================================================== */
    var owl = $("#clients-scroller");
    owl.owlCarousel({
      items:5,
      itemsTablet:3,
      margin:90,
      stagePadding:90,
      smartSpeed:450,
      itemsDesktop : [1199,4],
      itemsDesktopSmall : [980,3],
      itemsTablet: [768,3],
      itemsTablet: [767,2],
      itemsTabletSmall: [480,2],
      itemsMobile : [479,1],
    });

/* 
   Touch Owl Carousel
   ========================================================================== */
    var owl = $(".touch-slider");
    owl.owlCarousel({
      navigation: false,
      pagination: true,
      slideSpeed: 1000,
      stopOnHover: true,
      autoPlay: true,
      items: 1,
      itemsDesktopSmall: [1024, 1],
      itemsTablet: [600, 1],
      itemsMobile: [479, 1]
    });

    $('.touch-slider').find('.owl-prev').html('<i class="lni-chevron-left"></i>');
    $('.touch-slider').find('.owl-next').html('<i class="lni-chevron-right"></i>');

/* 
   Sticky Nav
   ========================================================================== */
    $(window).on('scroll', function() {
        if ($(window).scrollTop() > 200) {
            $('.header-top-area').addClass('menu-bg');
        } else {
            $('.header-top-area').removeClass('menu-bg');
        }
    });

/* 
   VIDEO POP-UP
   ========================================================================== */
    // $('.video-popup').magnificPopup({
    //     disableOn: 700,
    //     type: 'iframe',
    //     mainClass: 'mfp-fade',
    //     removalDelay: 160,
    //     preloader: false,
    //     fixedContentPos: false,
    // });

/* 
   Back Top Link
   ========================================================================== */
    var offset = 200;
    var duration = 500;
    $(window).scroll(function() {
      if ($(this).scrollTop() > offset) {
        $('.back-to-top').fadeIn(400);
      } else {
        $('.back-to-top').fadeOut(400);
      }
    });

    $('.back-to-top').on('click',function(event) {
      event.preventDefault();
      $('html, body').animate({
        scrollTop: 0
      }, 600);
      return false;
    })

/* 
   One Page Navigation & wow js
   ========================================================================== */
    //Initiat WOW JS
    new WOW().init();

/* stellar js
  ========================================================*/
  // $.stellar({
  //   horizontalScrolling: false,
  //   verticalOffset: 30,
  //   responsive: false
  // });


}(jQuery));

// Переключатель

// const activityWinter = document.querySelector('.activity-winter')
// const activitySummer = document.querySelector('.activity-summer')
// const priceBtn = document.querySelector('.price-btn')

// const summerBtn = document.querySelector('#no')
// const winterBtn = document.querySelector('#yes')

// summerBtn.addEventListener('click', () => {
//   activitySummer.classList.remove('hidden')
//   activityWinter.classList.add('hidden')
//   priceBtn.style.backgroundColor = '#77ce06'
// })

// winterBtn.addEventListener('click', () => {
//   activityWinter.classList.remove('hidden')
//   activitySummer.classList.add('hidden')
//   priceBtn.style.backgroundColor = '#77dbf9'
// })

// Модалки

// const appointmentBtn = document.querySelector('.appointment-btn')
// const closeBtn = document.querySelectorAll('.btn-close')
// const phoneInput = document.querySelector('#phone')

// console.log(appointmentBtn);

// const modalBuy = new bootstrap.Modal(document.getElementById('modalBuy'), {

// })

// const modalSave = new bootstrap.Modal(document.getElementById('modalSave'), {

// })


// function closeModal(modal) {
//   closeBtn.forEach(btn => {
//     btn.addEventListener('click', () => {
//       modal.hide();
//     })
//   });
// }

// appointmentBtn.addEventListener('click', () => {
//   modalBuy.show()
// })


// closeModal(modalBuy)