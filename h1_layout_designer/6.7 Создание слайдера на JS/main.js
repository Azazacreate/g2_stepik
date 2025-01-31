const img = document.querySelector('.slider_image');
const dots = document.querySelectorAll('.slider_dot');
const imgs = ['./img/html.jpg', './img/css.jpg', './img/js.jpg'];
let indexCurrent = 0;


function indexNext(direction) {
    indexCurrent += direction;
    if (indexCurrent >= imgs.length) {
        indexCurrent = 0;
    }
    else if (indexCurrent < 0) {
        indexCurrent = imgs.length - 1;
    }
    slide(indexCurrent);
}
function slide(index) {
    img.src = imgs[index];
    update__dots(index);
}
function update__dots(index) {
    for (let dot of dots) {
        dot.classList.remove('active');
    }
    dots[index].classList.add('active');
}
