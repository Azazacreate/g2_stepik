(function() {   // возьми и вызови:сразу функцию
    const tab_head_item = document.querySelectorAll('.tab_head_item');
    const tab_content_item = document.querySelectorAll('.tab_content_item')


    tab_head_item.forEach((tab, i) => {
        tab.onclick = () => {
            change__tab(i)
        }
    })     // функция:высшего-порядка


    function change__tab(i) {
        set__classActive(tab_head_item, i);
        set__classActive(tab_content_item, i);
    }
    function set__classActive(array, i) {
        for (let el of array) {
            el.classList.remove('active');
        }
        array[i].classList.add('active');
    }
}) ();
