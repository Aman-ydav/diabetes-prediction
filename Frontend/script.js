document.getElementById("predictForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const button = e.target.querySelector('button');
    const result = document.getElementById('result');
    
    button.disabled = true;
    button.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Processing...';

    const requestData = {
        highBP: parseInt(document.getElementById("highBP").value),
        highChol: parseInt(document.getElementById("highChol").value),
        bmi: parseFloat(document.getElementById("bmi").value) || 0,
        stroke: parseInt(document.getElementById("stroke").value),
        heartDisease: parseInt(document.getElementById("heartDisease").value),
        physActivity: parseInt(document.getElementById("physActivity").value),
        genHlth: parseInt(document.getElementById("genHlth").value),
        physHlth: parseInt(document.getElementById("physHlth").value),
        diffWalk: parseInt(document.getElementById("diffWalk").value),
        age: parseInt(document.getElementById("age").value),
    };
    // console.log(requestData);
    try {
        const response = await fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(requestData),
        });

        // const featuresResponse = await fetch("http://127.0.0.1:8000/image", {
        //     method: "GET",
        //     headers: { "Content-Type": "application/json" },
        // });
        // const featuresData = await featuresResponse.json();
        // console.log(featuresData);

        fetch("http://127.0.0.1:8000/image")
            .then(response => response.blob())  // Convert response to Blob
            .then(blob => {
                const url = URL.createObjectURL(blob); // Create object URL
                document.getElementById("image").src = url; // Set as image src
            })
            .catch(error => console.error("Error loading image:", error));
        const resultData = await response.json();

        result.className = 'success';
        console.log(resultData);
        console.log(resultData.probability[1])
        var risk = "";

        if (resultData.probability[1] > 0.8) risk="Very High";
        else if (resultData.probability[1] > 0.6) risk="High";
        else if (resultData.probability[1] > 0.4) risk="Moderate";
        else if (resultData.probability[1] > 0.2) risk="Low";
        else risk="Very Low";
        if (resultData.prediction[0] == 1 || resultData.probability[1] > 0.5) {
            result.innerHTML = `Diabetes Prediction: ${risk} Risk!<br>Please consult a doctor.<br>You are ${Math.round(resultData.probability[1] * 100)}% likely to have a heart disease.`;
        } else {
            result.innerHTML = `Diabetes Prediction: ${risk} Risk!<br>You are ${Math.round(resultData.probability[1] * 100)}% likely to have a heart disease.`;
        }
        document.getElementById("predictForm").reset();

    } catch (error) {
        console.error("Error:", error);
        result.className = 'error';
        result.textContent = 'An error occurred. Please try again.';
    } finally {
        button.disabled = false;
        button.innerHTML = '<i class="fas fa-calculator"></i> Calculate Risk';
        result.style.display = 'block';
    }
});


document.getElementById('bmi').addEventListener('input', (e) => {
    const value = parseFloat(e.target.value);
    if (value < 10 || value > 50) {
        e.target.setCustomValidity('BMI must be between 10 and 50');
    } else {
        e.target.setCustomValidity('');
    }
});
