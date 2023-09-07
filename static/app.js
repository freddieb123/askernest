// app.js
// Function to update the submit button text
function setButtonThinking() {
  const submitBtn = document.getElementById("submitBtn");
  submitBtn.disabled = true;
  submitBtn.textContent = 'Thinking...';
}

// Function to revert the submit button text to the original
function setButtonSubmit() {
  const submitBtn = document.getElementById("submitBtn");
  submitBtn.disabled = false;
  submitBtn.textContent = 'Submit';
}

document.getElementById("submitBtn").addEventListener("click", function (event) {
            event.preventDefault();
            setButtonThinking();
            const formData = {
                name: document.getElementById("name").value,
                relation: document.getElementById("relation").value,
                age: document.getElementById("age").value,
                grewup: document.getElementById("grewup").value,
                location: document.getElementById("location").value,
                interests: document.getElementById("interests").value,
                relationship: document.getElementById("relationship").value,
                fic_nonfic: document.querySelector('input[name="fic_nonfic"]:checked').value,
                email: document.getElementById("email").value
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
            })
            .finally(() => {
              setButtonSubmit(); // Revert the button text after API call is complete
            });
        });

        // Function to update the page content dynamically
  function updatePageContent(books) {
      // Get the container for the books
      const booksContainer = document.getElementById("booksContainer");

      // Clear existing book items
      booksContainer.innerHTML = '';

      // Create and append new divs for each book
      for (const [title, { authors, thumbnail, amazonLink }] of Object.entries(books)) {
          const bookItem = document.createElement("div");
          bookItem.className = "bookItem";

          const bookLink = document.createElement("a");
          bookLink.href = amazonLink;
          bookLink.target = "_blank";  // Opens the link in a new tab

          const thumbnailImage = document.createElement("img");
          thumbnailImage.src = thumbnail;
          thumbnailImage.alt = title;
          thumbnailImage.className = "bookCover";

          bookLink.appendChild(thumbnailImage);  // Append the image to the link
          bookItem.appendChild(bookLink);  // Append the link to the book item

          const bookTitle = document.createElement("div");
          bookTitle.innerText = title;
          bookTitle.className = "bookTitle";

          const bookAuthor = document.createElement("div");
          bookAuthor.innerText = authors;
          bookAuthor.className = "bookAuthor";

          bookItem.appendChild(bookTitle);
          bookItem.appendChild(bookAuthor);

          booksContainer.appendChild(bookItem);
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
