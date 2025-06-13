let timeLeft = 10;
const timerDisplay = document.getElementById("timer");
const form = document.getElementById("quizForm");

const countdown = setInterval(() => {
  timeLeft--;
  timerDisplay.textContent = timeLeft;

  if (timeLeft <= 0) {
    clearInterval(countdown);
    if (form) form.submit();
  }
}, 1000);
document.querySelectorAll('input[name="answer"]').forEach((input) => {
  input.addEventListener("change", () => {
    document.getElementById("submitBtn").disabled = false;
  });
});

document.addEventListener("DOMContentLoaded", () => {
  const correctSound = document.getElementById("correctSound");
  const wrongSound = document.getElementById("wrongSound");
  const form = document.getElementById("quizForm");

  if (form) {
    form.addEventListener("submit", () => {
      const selected = form.querySelector('input[name="answer"]:checked');
      const correct = document.querySelector(".text-green-400");
      const wrong = document.querySelector(".text-red-400");

      setTimeout(() => {
        if (correct) {
          correctSound.play();
          triggerConfetti();
        } else if (wrong) {
          wrongSound.play();
        }
      }, 100);
    });
  }

  function triggerConfetti() {
    confetti({
      particleCount: 100,
      spread: 70,
      origin: { y: 0.6 },
    });
  }
});
