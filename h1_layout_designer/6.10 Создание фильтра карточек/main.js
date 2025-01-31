const filter_button_item = document.querySelectorAll('.filter_button_item');
const filter_content = document.querySelectorAll('.filter_content img');
const select = document.querySelector('.filter_options');


for (let button of filter_button_item) {
    button.onclick = function() {
        filter__image(this.dataset.filter);
    };
};


function filter__image(sel) {
    for (let img of filter_content) {
        img.style.display = 'none';
        if (img.classList.contains(sel)) {
            setTimeout(() => {
                img.style.display = 'inline';
            }, 0.1);
        }
    };
    for (let button of filter_button_item) {
        if (button.dataset.filter === sel) {
            button.classList.add('active');
        }
        else {
            button.classList.remove('active');
        }
    };
    select.value = sel;
};


select.addEventListener('change', () => {
    filter__image(select.value);
});