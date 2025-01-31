const heading = $('.h1');
heading.css({
    'text-transform': 'lowercase',
    'color': 'blue',
}); // несколько-свойств

// обработать клик
$('.button_1').on('click', () => {
    heading.toggleClass('active');
})


// коллапсер
$('.button_2').on('click', () => {
    div.fadeToggle();
})