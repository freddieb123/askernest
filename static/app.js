// app.js
document.getElementById("submitBtn").addEventListener("click", function (event) {
            event.preventDefault();
            const formData = {
                name: document.getElementById("name").value,
                age: document.getElementById("age").value,
                grewup: document.getElementById("grewup").value,
                location: document.getElementById("location").value,
                interests: document.getElementById("interests").value,
                relationship: document.getElementById("relationship").value
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
                    console.log(typeof data.books)
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
          console.log(books)
          console.log(typeof books)
          //const booksobject = JSON.parse(books);



          // Clear existing rows (except the header)
          while (table.rows.length > 1) {
            table.deleteRow(1);
          }

          // Create and append new rows for each book
          for (const [title, { author, thumbnail }] of Object.entries(books)) {
            const newRow = table.insertRow();
            const thumbnailCell = newRow.insertCell();
            const titleCell = newRow.insertCell();
            const authorCell = newRow.insertCell();

            const thumbnailImage = document.createElement("img");
            thumbnailImage.src = thumbnail;
            thumbnailImage.alt = title;
            thumbnailCell.appendChild(thumbnailImage);

            titleCell.innerText = title;
            authorCell.innerText = author;
          }


          // Show the book recommendations section and hide the user info form section
          const formDataName = document.getElementById("name").value;
          const bookRecommendationsSection = document.getElementById("bookRecommendations");
          const userInfoFormSection = document.getElementById("userForm");
          const recTitleElement = document.getElementById("recTitle");

          recTitleElement.innerText = `Book Recommendations for ${formDataName}`;
          bookRecommendationsSection.style.display = "block";
          userInfoFormSection.style.display = "none";


          }
