let ws = new WebSocket('wss://stream.binance.com:9443/ws/etheur@trade');

let stockPriceElement = document.getElementById('stockPriceElement');
var file="CurrentPrice.txt"
  

ws.onmessage=(event)=>{
    
    let stockPrice=parseFloat(JSON.parse(event.data).p).toFixed(2);

    stockPriceElement.innerHTML =stockPrice
    WritableStreamDefaultWriter
    



};