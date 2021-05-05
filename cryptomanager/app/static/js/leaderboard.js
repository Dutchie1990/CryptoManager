window.onload = function () {

    var buttons = [...document.getElementsByClassName('data-collapse')]
    var data_row = [...document.getElementsByClassName('data-row')]

    buttons.forEach(element => element.addEventListener('click', function () {
        shown_row = data_row.find(el => el.id === this.getAttribute('data-target'))
        if(!shown_row.classList.contains('visible')){
            shown_row.classList.add('visible')
        } else{
            hide(shown_row)
        }  
    }))

    function hide(el) {
        el.classList.add("hidden");
        el.classList.remove("visible");
    }
}