//define elements
var volume_element = document.getElementById('volume')
var prize_element = document.getElementById('prize')
var usd_prize_element = document.getElementById('usd_prize')
var submit_button = document.getElementById('submit-button')

//define variables
var vs_currency
var coin_symbol
var ordertype
var owned_assets;
var supported_assets;

//define xpaths
var xpath_ordertype = "//button[@data-id='ordertype']"
var xpath_vs_currency = "//button[@data-id='vs_currency']"
var xpath_coin_symbol = "//button[@data-id='coin_symbol']"

const instance = axios.create({
    baseURL: 'https://api.coingecko.com/api/v3',
});

//get the user's assets
fetch('/fetch_owned_assets')
    .then(function (response) {
        return response.json();
    }).then(function (text) {
        owned_assets = text;
    });

//get the supported vs_currencies
fetch('/fetch_supported_assets')
    .then(function (response) {
        return response.json();
    }).then(function (text) {
        supported_assets = text;
    })

volume_element.addEventListener('blur', getPrize)
prize_element.addEventListener('blur', getUsdPrize)

$(".selectpicker").change(function () {
    //get current values
    ordertype = getValueByXpath(xpath_ordertype)
    coin_symbol = getValueByXpath(xpath_coin_symbol)
    vs_currency = getValueByXpath(xpath_vs_currency)

    //overwrite with selected value depend on which button is changed
    if (this.name === "vs_currency")
        vs_currency = this.options[this.selectedIndex].value.toLowerCase()
    else if (this.name === 'coin_symbol') {
        coin_symbol = this.options[this.selectedIndex].value.toLowerCase()
    }
    else {
        ordertype = this.options[this.selectedIndex].value.toLowerCase()
    }

    //get the current prize
    getPrize()
})

function getPrize() {
    // disable submit-button
    submit_button.setAttribute("disabled", true)

    //if volume is not filled exit function
    let volume = parseFloat(volume_element.value)
    if (volume === 0) {
        return
    }

    if (!ordertype){
        ordertype = getValueByXpath(xpath_ordertype)
    }
    if (!coin_symbol){
        coin_symbol = getValueByXpath(xpath_coin_symbol)
    }
    if (!vs_currency){
        vs_currency = getValueByXpath(xpath_vs_currency)
    }

    asset_in = supported_assets.filter(x => x.symbol == coin_symbol)
    id_in = asset_in[0].id
    instance.get('/simple/price', {
        params: {
            ids: id_in,
            vs_currencies: vs_currency + ",usd"
        }
    }).then(function (response) {
        prize_element.value = parseFloat(response.data[id_in][vs_currency]) * volume;
        if (ordertype === "sell") {
            usd_prize_element.value = parseFloat(calcPrize(volume_element.value, response.data[id_in]['usd'], prize_element.value))
            console.log(usd_prize_element.value + "normal sell")
        } else {
            usd_prize_element.value = parseFloat(response.data[id_in]['usd'])
            console.log(usd_prize_element.value + "normal buy")
        }
        submit_button.removeAttribute("disabled")
    });
}

function getUsdPrize() {
    //disable submit
    submit_button.setAttribute("disabled", true)

    if (vs_currency === "usd") {
        usd_prize_element.value = prize_element.value / volume_element.value;
    } else {
        if (ordertype === "sell") {
            currency_out = supported_assets.filter(x => x.symbol == coin_symbol)
        } else {
            currency_out = supported_assets.filter(x => x.symbol == vs_currency)
        }

        id_in = currency_out[0].id
        instance.get('/simple/price', {
            params: {
                ids: id_in,
                vs_currencies: "usd"
            }
        }).then(function (response) {
            if (ordertype === "sell") {
                usd_prize_element.value = parseFloat(calcPrize(response.data[id_in]['usd'], volume_element.value, prize_element.value))
                console.log(usd_prize_element.value + "adjusted sell")
            } else {
                usd_prize_element.value = parseFloat(calcPrize(response.data[id_in]['usd'], prize_element.value, volume_element.value))
                console.log(usd_prize_element.value + "adjusted buy")
            }
            submit_button.removeAttribute("disabled")
        });
    }
}

function getValueByXpath(Xpath){
    let element = document.evaluate(Xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null)
    return element.singleNodeValue.title.toLowerCase()
}

function calcPrize(a, b, c){
    return (a * b ) / c 
}


