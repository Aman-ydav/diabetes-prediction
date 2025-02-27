document.addEventListener("DOMContentLoaded", function() {
    document.querySelector(".container").style.opacity = "1";
});

document.getElementById("predictForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const button = e.target.querySelector('button');
    const result = document.getElementById('result');

    // Show loading state
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
    console.log(requestData);
    try {
        const response = await fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(requestData),
        });

        const resultData = await response.json();

        // Show success message
        result.className = 'success';
        console.log(resultData);
        if (resultData.prediction == 1) {
            result.textContent = `Prediction: High Risk\nPlease consult a doctor.`;
        } else {
            result.textContent = `Prediction: Low Risk`;
        }
        document.getElementById("predictForm").reset();
        // result.textContent = `Prediction: ${resultData.prediction}`;
    } catch (error) {
        console.error("Error:", error);
        // Show error message
        result.className = 'error';
        result.textContent = 'An error occurred. Please try again.';
    } finally {
        button.disabled = false;
        button.innerHTML = '<i class="fas fa-calculator"></i> Calculate Risk';
        result.style.display = 'block';
    }
});

// Add input validation
document.getElementById('bmi').addEventListener('input', (e) => {
    const value = parseFloat(e.target.value);
    if (value < 10 || value > 50) {
        e.target.setCustomValidity('BMI must be between 10 and 50');
    } else {
        e.target.setCustomValidity('');
    }
});
