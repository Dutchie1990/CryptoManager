if (!flash_element){
    var flash_element = document.getElementById('flashes')
    var style = getComputedStyle(flash_element)
 }
     
 function setElementListener(){
     flash_element.addEventListener('onchange', fadeAway())
 }
 
 function fadeAway(){
     flash_element.style.opacity = "1"
     var timer = setInterval(function () {
         if (flash_element.style.opacity === "0"){
             clearInterval(timer);
             
         }
         flash_element.style.opacity -= 0.05
     }, 200);
 }
