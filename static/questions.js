let questions = document.querySelectorAll('.question');
let currentIndex = 0;

// Display the first question initially
questions[currentIndex].style.display = 'block';

questions.forEach((question, index) => {
    let input = question.querySelector('.input');
    let nextBtn = question.querySelector('.nextBtn');

    // Handle the "Enter" key within the input
    input.addEventListener('keyup', function(event) {
        if (event.key === 'Enter') {
            showNextQuestion();
        }
    });

    // Handle the "Next" button click
    if (nextBtn) {
        nextBtn.addEventListener('click', showNextQuestion);
    }
});

function showNextQuestion() {
    // Hide the current question
    questions[currentIndex].style.display = 'none';
    currentIndex++;

    // Show the next question if there is one
    if (currentIndex < questions.length) {
        questions[currentIndex].style.display = 'block';
    }
}
