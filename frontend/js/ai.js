function getSuggestion() {

    const capacity = document.getElementById("capacity").value;
    const date = document.getElementById("date").value;
    const start_time = document.getElementById("start_time").value;
    const end_time = document.getElementById("end_time").value;

    if (!capacity || !date || !start_time || !end_time) {
        alert("Please fill all fields ❌");
        return;
    }

    fetch("http://127.0.0.1:5001/ai/suggest-room", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            capacity,
            date,
            start_time,
            end_time
        })
    })
    .then(res => res.json())
    .then(data => {
        console.log(data);

        const result = document.getElementById("result");

        if (data.status === "success") {
    result.innerHTML = `
        <h3>✅ Suggested Room: ${data.room.room_number}</h3>
        <p>💡 Reason: ${data.room.reason}</p>
    `;
    result.style.color = "green";
} else {
    result.innerText = data.message;
    result.style.color = "red";
}
    })
    .catch(err => {
        console.error(err);
        alert("Server error ❌");
    });
}

function goBack() {
    window.location.href = "../dashboard.html";
}