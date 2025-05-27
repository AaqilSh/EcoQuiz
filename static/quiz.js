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
