const summarizeBtn = document.getElementById("summarize-btn");
const dialogueInput = document.getElementById("dialogue-input");
const summaryText = document.getElementById("summary-text");

const modal = document.getElementById("error-modal");
const errorMessage = document.getElementById("error-message");
const closeModal = document.getElementById("close-modal");
const modalOk = document.getElementById("modal-ok");

function showError(message) {
  errorMessage.innerText = message;
  modal.style.display = "flex";
}

function hideModal() {
  modal.style.display = "none";
}

summarizeBtn.addEventListener("click", async () => {
  const dialogue = dialogueInput.value.trim();

  if (!dialogue) {
    showError("Please enter some text to summarize.");
    return;
  }

  summaryText.innerText = "Processing...";
  summarizeBtn.disabled = true;

  try {
    const response = await fetch("/summarize/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ dialogue }),
    });

    if (!response.ok) {
      throw new Error("Server error occurred.");
    }

    const data = await response.json();

    summaryText.innerText =
      data.summary || "No summary was returned from the server.";
  } catch (error) {
    showError(error.message);
  } finally {
    summarizeBtn.disabled = false;
  }
});

closeModal.addEventListener("click", hideModal);

modalOk.addEventListener("click", hideModal);

window.addEventListener("click", (e) => {
  if (e.target === modal) {
    hideModal();
  }
});
