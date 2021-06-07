var form_elements = [...document.getElementsByTagName('input')];
var email_el = form_elements.find(element => element['id'] === "email");
var password_el_old = form_elements.find(element => element['id'] === "old_password");
var password_el_new = form_elements.find(element => element['id'] === "new_password");

var submit_button = document.getElementById('submit-button');
var clear_button = document.getElementById('clear-button');

window.onload = function () {
    setElementListener();
    clear_button.addEventListener('click', (event) => {
        event.preventDefault();
        submit_button.setAttribute("disabled", true);
        clear_button.setAttribute("disabled", true);
        form_elements.slice(2, form_elements.length).forEach(element => {
            element.value = "";
            element.classList.remove('is-valid');
            element.classList.remove('is-invalid');
        });
    });

    form_elements.slice(2).forEach(element => element.addEventListener('change', function () {
        validate(this);
        if (hasValue(password_el_old) || hasValue(password_el_new)) {
            clear_button.removeAttribute("disabled");
        } else {
            clear_button.setAttribute("disabled", true);
        }
    }));
};

function validate(element) {
    if (!(hasValue(element, 5))) {
        element.classList.add("is-invalid");
        element.classList.remove("is-valid");
    } else {
        element.classList.remove("is-invalid");
        element.classList.add("is-valid");
    }

    if (password_el_old.classList.contains('is-valid') && password_el_new.classList.contains('is-valid')) {
        if (submit_button.getAttribute("disabled") === "" || submit_button.getAttribute("disabled") === "true") {
            submit_button.removeAttribute("disabled");
        }
    } else {
        submit_button.setAttribute("disabled", true);
    }
}

function hasValue(element, val = 0) {
    return (element.value.length > val) ? true : false;
}