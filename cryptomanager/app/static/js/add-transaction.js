var owned_assets;
var supported_assets;
var volume_element = document.getElementById('volume')
var prize_element = document.getElementById('prize')
var symbol_out
var symbol_in

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

$(".selectpicker").change(function () {
    if (this.name === "symbolOut")
        symbol_out = this.options[this.selectedIndex].value.toLowerCase()
    else if (this.name === 'symbolIn'){
        symbol_in = this.options[this.selectedIndex].value.toLowerCase()
    }
    else {
        return;
    }

    getPrize()
})

function getPrize() {
    if (!symbol_in){
        symbol_in = document.getElementsByClassName('filter-option-inner-inner')[0].innerText.toLowerCase()
    }
    if (!symbol_out){
        symbol_out = document.getElementsByClassName('filter-option-inner-inner')[1].innerText.toLowerCase()
    }
    
    let volume = parseFloat(volume_element.value)

    asset_in = supported_assets.filter(x => x.symbol == symbol_in)
    id_in = asset_in[0].id
    instance.get('/simple/price', {
        params: {
            ids: id_in,
            vs_currencies: symbol_out
        }
    }).then(function(response){
        prize_element.value = parseFloat(response.data[id_in][symbol_out]) * volume
    })
}




