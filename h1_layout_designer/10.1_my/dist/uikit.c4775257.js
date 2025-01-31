const btn = document.querySelector(".open__modal");
const modal = document.querySelector(".modal");
const close__modal = document.querySelector(".close__modal");
btn.onclick = ()=>{
    modal.classList.add("modalActive");
    close__modal.addEventListener("click", close__modal_2);
    modal.addEventListener("click", hide__modal);
    function close__modal_2() {
        modal.classList.remove("modalActive");
        close__modal.removeEventListener("click", close__modal_2);
        modal.removeEventListener("click", hide__modal);
    }
    function hide__modal(event) {
        if (event.target === modal) close__modal_2();
    }
};

//# sourceMappingURL=uikit.c4775257.js.map
