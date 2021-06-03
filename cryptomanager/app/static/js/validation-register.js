var form_elements = [...document.getElementsByTagName('input')];
var firstname_el = form_elements.find(element => element['id'] === "firstname");
var email_el = form_elements.find(element => element['id'] === "email");
var password_el = form_elements.find(element => element['id'] === "password");
var passwordconfirm_el = form_elements.find(element => element['id'] === "password_confirm");
var submit_button = document.getElementById('submit-button');
var clear_button = document.getElementById('clear-button')

window.onload = function () {
    clear_button.addEventListener('click', (event) => {
        event.preventDefault()
        submit_button.setAttribute("disabled", true)
        clear_button.setAttribute("disabled", true) 
        form_elements.slice(1, form_elements.length).forEach(element => {
            element.value = ""
            element.classList.remove('is-valid')
            element.classList.remove('is-invalid')
        })
    })
    form_elements.forEach(element => element.addEventListener('change', function () {
        validate()
        if (hasValue(email_el) || hasValue(password_el) || hasValue(passwordconfirm_el) || hasValue(firstname_el)) {
            clear_button.removeAttribute("disabled")
        } else {
            clear_button.setAttribute("disabled", true) 
        }
    }))
    setElementListener()
}

function validate() {
    let email_valid;
    let password_valid;
    let firstname_valid;

    if(hasValue(firstname_el)){
        if(hasValue(firstname_el, 1)){
            firstname_valid = true;
            firstname_el.classList.remove("is-invalid");
            firstname_el.classList.add("is-valid");
        } else{
            firstname_valid = false
            firstname_el.classList.add("is-invalid");
            firstname_el.classList.remove("is-valid");
        }
    }

    if (hasValue(email_el)) {
        if (!(hasValue(email_el, 5)) || !(email_el.value.includes('@'))) {
            email_el.classList.add("is-invalid");
            email_el.classList.remove("is-valid");
            email_valid = false;
        } else {
            email_valid = true;
            email_el.classList.remove("is-invalid");
            email_el.classList.add("is-valid");
        }
    }

    if (hasValue(password_el, 5) && hasValue(passwordconfirm_el)) {
        if (!(password_el.value === passwordconfirm_el.value)) {
            passwordconfirm_el.classList.add("is-invalid");
            passwordconfirm_el.classList.remove("is-valid");
            password_el.classList.remove('is-valid')
            password_valid = false;
        } else {
            password_valid = true;
            passwordconfirm_el.classList.remove("is-invalid")
            passwordconfirm_el.classList.add("is-valid")
            password_el.classList.add('is-valid')
        }
    }

    if (email_valid && password_valid && firstname_valid) {
        if (submit_button.getAttribute("disabled") === "" || submit_button.getAttribute("disabled") === "true") {
            submit_button.removeAttribute("disabled")
        }
    } else {
        submit_button.setAttribute("disabled", true)
    }
}

function hasValue(element, val = 0) {
    return (element.value.length > val) ? true : false
}
