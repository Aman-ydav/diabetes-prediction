document.getElementById("predictForm").addEventListener("submit", async (event) => {
    event.preventDefault();

    const state = document.getElementById("state").value;
    const crop = document.getElementById("crop").value;
    const month = document.getElementById("month").value;
    const year = document.getElementById("year").value;

    const requestData = { state, crop, month, year };

    const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST", 
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(requestData),
    });

    const result = await response.json();
    console.log(result);
});
