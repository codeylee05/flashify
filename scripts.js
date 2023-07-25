//index template//

const textElement = document.querySelector('#text-animated');
const texts = [
  "Who said flashcards are out of fashion?",
  "With flashify, flashcards don't have to be boring",
  "Every flashcard is a building block",
  "Every block covered is a step closer to the final product; the building",
  "Set your confidence on each block and re-place it accordingly",
  "Because at the end of the day,",
  "What is a building without confident blocks?"
];
let textIndex = 0;
let charIndex = 0;
const charactersPerSecond = [14, 14, 16, 14, 14, 14, 14]; // Adjust characters per second for each sentence

function type() {
  const currentText = texts[textIndex];
  textElement.style.opacity = 1;
  textElement.textContent = currentText.slice(0, ++charIndex);

  if (charIndex === currentText.length) {
    const delay = currentText.length / charactersPerSecond[textIndex] * 1000; // Calculate delay based on characters per second
    setTimeout(erase, delay);
    return;
  }

  setTimeout(type, 1000 / charactersPerSecond[textIndex]); // Adjust animation speed based on characters per second
}

function erase() {
  const currentText = texts[textIndex];
  textElement.textContent = currentText.slice(0, --charIndex);

  if (charIndex === 0) {
    textElement.style.opacity = 0;
    textIndex++;
    if (textIndex === texts.length) {
      textIndex = 0;
    
      showResult();
    
    }
    setTimeout(type, 500);
    return;
  }

  const delay = 1000 / charactersPerSecond[textIndex]; // Adjust erasing speed based on characters per second
  setTimeout(erase, delay);
}
//to show the resulting div after the iteration of sentences in the typing animation:
function showResult() {

    const resultElement = document.querySelector("#nav-b")

    textElement.style.display = "none";
    resultElement.style.display = "block";

}

type();

//view-card template
/*
document.addEventListener("DOMContentLoaded", () => {

  const card = document.querySelector(".card-toggle");
  const prompt = card.querySelector("#prompt-data");
  const response = card.querySelector("#response-data");

  card.addEventListener("click", () => {

    response.classList.toggle("toggle-hide");
    prompt.classList.toggle("toggle-hide");

  });

});
*/