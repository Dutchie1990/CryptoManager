var owned_assets;
var supported_assets;
var volume_element = document.getElementById('volume')
var prize_element = document.getElementById('prize')
var usd_prize_element = document.getElementById('usd_prize')
var vs_currency
var coin_symbol
var ordertype

const instance = axios.create({
    baseURL: 'https://api.coingecko.com/api/v3',
});

fetch('/fetch_owned_assets')
    .then(function (response) {
        return response.json();
    }).then(function (text) {
        owned_assets = text;
    });

fetch('/fetch_supported_assets')
    .then(function (response) {
        return response.json();
    }).then(function (text) {
        supported_assets = text;
    })

volume_element.addEventListener('change', getPrize)
prize_element.addEventListener('blur', getUsdPrize)

$(".selectpicker").change(function () {
    let xpath_ordertype = "//button[@data-id='ordertype']"
    var ordertype_el = document.evaluate(xpath_ordertype, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null)
    ordertype = ordertype_el.singleNodeValue.title.toLowerCase()

    let xpath_coin_symbol = "//button[@data-id='coin_symbol']"
    var coin_symbol_el = document.evaluate(xpath_coin_symbol, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null)
    coin_symbol = coin_symbol_el.singleNodeValue.title.toLowerCase()

    let xpath_vs_currency = "//button[@data-id='vs_currency']"
    var vs_currency_el = document.evaluate(xpath_vs_currency, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null)
    vs_currency = vs_currency_el.singleNodeValue.title.toLowerCase()

    if (this.name === "vs_currency")
        vs_currency = this.options[this.selectedIndex].value.toLowerCase()
    else if (this.name === 'coin_symbol') {
        coin_symbol = this.options[this.selectedIndex].value.toLowerCase()
    }
    else {
        ordertype = this.options[this.selectedIndex].value.toLowerCase()
    }

    getPrize()
})

function getPrize() {
    if (!coin_symbol) {
        coin_symbol = document.getElementsByClassName('filter-option-inner-inner')[0].innerText.toLowerCase()
    }
    if (!vs_currency) {
        vs_currency = document.getElementsByClassName('filter-option-inner-inner')[1].innerText.toLowerCase()
    }

    let volume = parseFloat(volume_element.value)
    if (volume === 0) {
        return
    }
    //let xpath = "//button[@data-id='ordertype']"
    //var ordertype_el = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null)
    //ordertype = ordertype_el.singleNodeValue.title

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
            usd_prize_element.value = parseFloat((volume_element.value * response.data[id_in]['usd']) / prize_element.value)
            console.log(usd_prize_element.value + "normal sell")
        } else {
            usd_prize_element.value = parseFloat(response.data[id_in]['usd'])
            console.log(usd_prize_element.value + "normal buy")
        }
    });
}

function getUsdPrize() {
    if (!vs_currency) {
        vs_currency = document.getElementsByClassName('filter-option-inner-inner')[1].innerText.toLowerCase()
    }
    if (!coin_symbol) {
        coin_symbol = document.getElementsByClassName('filter-option-inner-inner')[0].innerText.toLowerCase()
    }
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
                usd_prize_element.value = parseFloat((response.data[id_in]['usd'] * volume_element.value) / prize_element.value)
                console.log(usd_prize_element.value + "adjusted sell")
            } else {
                usd_prize_element.value = parseFloat((response.data[id_in]['usd'] * prize_element.value) / volume_element.value)
                console.log(usd_prize_element.value + "adjusted buy")
            }
        });
    }
}




