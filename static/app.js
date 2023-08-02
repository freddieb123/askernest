// app.js
document.getElementById("userForm").addEventListener("submit", function (event) {
            event.preventDefault();
            const formData = {
                name: document.getElementById("name").value,
                age: Array.from(document.getElementById("age").selectedOptions, option => option.value),
                location: document.getElementById("location").value,
                interests: document.getElementById("interests").value,
            };
            fetch("/submitFormData", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(formData)
                console.log("started")
            })
            .then(response => {
                if (response.ok) {
                    alert("Form data submitted successfully!");
                } else {
                    alert("Error submitting form data. Please try again later.");
                }
            })
            .catch(error => {
                console.error("Error submitting form data:", error);
                alert("Error submitting form data. Please try again later.");
            });
        });
