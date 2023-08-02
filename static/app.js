// app.js
document.getElementById("userForm").addEventListener("submit", function (event) {
            event.preventDefault();
            const formData = {
                name: document.getElementById("name").value,
                age: document.getElementById("age").value,
                location: document.getElementById("location").value,
                interests: document.getElementById("interests").value,
            };
            fetch("/submitFormData", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(formData)
            })
            .then(response => response.json())
            .then(data => {
                if (data.message === "Data inserted successfully") {
                    // Update the page content dynamically with the new data
                    console.log(data.books)
                    updatePageContent(data.books);
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

        // Function to update the page content dynamically
        function updatePageContent(books) {
          // Get the table element
          const table = document.getElementById("bookTable");

          // Clear existing rows (except the header)
          while (table.rows.length > 1) {
            table.deleteRow(1);
          }

          // Create and append new rows for each book
          for (const [title, author] of Object.entries(books)) {
              const newRow = table.insertRow();
              const titleCell = newRow.insertCell();
              const authorCell = newRow.insertCell();
              titleCell.innerText = title;
              authorCell.innerText = author;
              }
          }
