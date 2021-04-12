document.addEventListener('DOMContentLoaded', function (event) {

    $('#table').DataTable({
        "searching": false,
        "order": [["2", "asc"]],
        "aLengthMenu": [2, 5, 10, 25],
        "iDisplayLength": 2,
        "pagingType": "numbers",
        "info": false,
    });
    var table_el = document.getElementById("table_wrapper");
    var input_el = document.getElementById('deposit_amount')
    var clear_button = document.getElementById('clear-button')
    setElementListener()
    table_el.addEventListener('click', addIcon);
    input_el.addEventListener('change', function (event) {
        validate(event)
        if (hasValue(input_el)) {
            clear_button.removeAttribute("disabled")
        } else {
            clear_button.setAttribute("disabled", true)
        }
    })
    clear_button.addEventListener('click', (event) => {
        event.preventDefault()
        input_el.value = ""
        input_el.classList.remove('is-valid')
        input_el.classList.remove('is-invalid')
        clear_button.setAttribute("disabled", true)
        clear_button.blur()
    })
    addIcon();
})

function addIcon() {
    let elements = $("td[scope$='row']");
    for (let index = 0; index < elements.length; index++) {
        let symbol = elements[index].innerText.toLowerCase().replace(/\s+/g, '');
        imagesource = `/static/img/symbols/${symbol}.png`;
        let el = elements[index].children;
        el[0].src = imagesource;
    }
}

function validate() {
    let is_valid;
    let submit_button = document.getElementById('submit-button')
    if (hasValue(event.target)) {
        if (isNaN(event.srcElement.value)) {
            event.target.classList.add('is-invalid')
            event.target.classList.remove('is-valid')
            is_valid = false;
        } else {
            event.target.classList.remove('is-invalid')
            event.target.classList.add('is-valid')
            is_valid = true
        }
        if (is_valid) {
            if (submit_button.getAttribute("disabled") === "" || submit_button.getAttribute("disabled") === "true") {
                submit_button.removeAttribute("disabled")
            }
        } else {
            submit_button.setAttribute("disabled", true)
        }
    } else{
        event.target.classList.remove('is-valid')
        event.target.classList.remove('is-invalid')
        submit_button.setAttribute("disabled", true)
    }

}

function hasValue(element, val = 0) {
    return (element.value.length > val) ? true : false
}

