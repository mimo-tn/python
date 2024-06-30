var cookie=document.querySelector("#cookie");
async function loading(lat, lon, key) {
    alert("Loading weather report ...");
    
    try {
        var weather = await getCoderData(lat, lon, key);
        
        for (var i = 1; i < 9; i++) {
            var tempSpan = document.querySelector("#span" + i);
            // Check if the weather data is available and update the temperature
            var j = Math.floor((i - 1) / 2);
            if (i % 2 !== 0) {
                var temperatureKelvin = weather.list[j].main.temp_max;
                var temperatureCelsius = temperatureKelvin - 273.15; // Convert Kelvin to Celsius
                var formattedTemp = Math.round(temperatureCelsius); // Get the integer part (closest whole number)
                tempSpan.innerText = formattedTemp + "°";
            }else{
                var temperatureKelvin = weather.list[j].main.temp_min;
                var temperatureCelsius = temperatureKelvin - 273.15; // Convert Kelvin to Celsius
                var formattedTemp = Math.round(temperatureCelsius); // Get the integer part (closest whole number)
                tempSpan.innerText = formattedTemp + "°";
            }
        }
    } catch (error) {
        console.error('Error updating weather data:', error);
    }
}
function remove_cookie(){
    cookie.remove();
}
function c2f(temp){
    return Math.round(9/5 * temp + 32)
}

function f2c(temp){
    return Math.round(5/9 * (temp - 32))
}

function convert(element) {
    for(var i=1; i<9; i++) {
        var tempSpan = document.querySelector("#span" + i);
        var tempVal = parseInt(tempSpan.innerText);
        if(element.value == "°C"){
            tempSpan.innerText = f2c(tempVal)+"°"
        }
        else {
            tempSpan.innerText = c2f(tempVal)+"°";
        }
    }
}
async function getCoderData(lat,lon,key) {
    try {
        var apiUrl = `https://api.openweathermap.org/data/2.5/forecast?lat=${lat}&lon=${lon}&appid=${key}`;
        var response = await fetch(apiUrl);
        
        // Convert the data into JSON format
        var coderData = await response.json();
        return coderData;
        
    } catch (error) {
        console.error('Error fetching user data:', error);
    }
}