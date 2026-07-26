document.getElementById("bookingForm").addEventListener("submit", function (e) {

    e.preventDefault();

    const name = document.getElementById("name").value;
    const vehicle = document.getElementById("vehicle").value;
    const slot = document.getElementById("slot").value;

    fetch("http://127.0.0.1:5000/book", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            name: name,
            vehicle: vehicle,
            slot: slot
        })

    })

    .then(response => response.json())

    .then(data => {

        document.getElementById("result").innerHTML =
        "✅ " + data.message;

    })

    .catch(error => {

        console.error(error);

        document.getElementById("result").innerHTML =
        "❌ Unable to connect to backend.";

    });

});