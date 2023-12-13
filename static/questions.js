let questions = document.querySelectorAll('.question');
let currentIndex = 0;

// Get the total number of questions
let totalQuestions = questions.length;

// Set initial progress bar text
const progressBar = document.querySelector('.progress-bar');
progressBar.style.paddingLeft = '5px'; // Add 5 pixels of left padding
progressBar.innerText = `0/${totalQuestions}`;

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
      // Get the current question and input value
      let currentQuestion = questions[currentIndex];
      let inputValue = currentQuestion.querySelector('.input').value;

      // Track the event with Mixpanel
      mixpanel.track('Next Question Clicked', {
          'Question Number': currentIndex + 1, // +1 because index is 0-based
          'Input Value': inputValue
      });


    // Hide the current question
    questions[currentIndex].style.display = 'none';
    currentIndex++;

    // If the next question is hidden (like the relation question for 'For Yourself'), skip it
    while (currentIndex < questions.length && questions[currentIndex].style.display === 'none') {
        currentIndex++;
    }

    // Update progress bar
    let progress = (currentIndex / questions.length) * 100;
    document.querySelector('.progress-bar').style.width = progress + '%';

    if (currentIndex <= questions.length) {
        document.querySelector('.progress-bar').innerText = `${currentIndex}/${questions.length}`;
    } else {
        document.querySelector('.progress-bar').innerText = 'Completed!';
    }

    // Show the next question if there is one
    if (currentIndex < questions.length) {
        questions[currentIndex].style.display = 'block';
    }
}
