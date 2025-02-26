document.getElementById('predict-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    let state = document.getElementById('state').value;
    let crop = document.getElementById('crop').value;
    let month = parseInt(document.getElementById('month').value);
    let year = parseInt(document.getElementById('year').value);

    let prev_yield = 20;  
    let prev_price = 30;  
    let weather_factor = 0.9;  

    let response = await fetch('http://127.0.0.1:8000/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ state, crop, month, year, prev_yield, prev_price, weather_factor })
    });

    let result = await response.json();
    document.getElementById('result').textContent = 'Predicted Price: $' + result.predicted_price;
});
