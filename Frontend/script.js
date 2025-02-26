document.addEventListener("DOMContentLoaded", function() {
    document.querySelector(".container").style.opacity = "1";
});


document
  .getElementById("predictForm")
  .addEventListener("submit", async (event) => {
    event.preventDefault(); 

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

    try {
      const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(requestData),
      });

      const result = await response.json();
      document.getElementById(
        "result"
      ).innerText = `Prediction: ${result.prediction}`;

      document.getElementById("predictForm").reset();
    } catch (error) {
      console.error("Error:", error);
      document.getElementById("result").innerText = "Error fetching prediction";
    }
  });
