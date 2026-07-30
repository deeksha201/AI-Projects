function addMessage(text, sender) {
    const chat = document.getElementById("chat");
    const message = document.createElement("div");
    message.className = `message ${sender}`;
    message.textContent = text;
    chat.appendChild(message);
    chat.scrollTop = chat.scrollHeight;
}

function sendMessage() {
    const input = document.getElementById("message");
    const submitBtn = document.getElementById("submitBtn");
    const message = input.value.trim();

    if (!message) {
        input.classList.remove("shake");
        void input.offsetWidth;
        input.classList.add("shake");
        return;
    }

    submitBtn.classList.remove("is-sending");
    void submitBtn.offsetWidth;
    submitBtn.classList.add("is-sending");

    addMessage(message, "user");
    input.value = "";

    const typingIndicator = document.createElement("div");
    typingIndicator.className = "message bot typing";
    typingIndicator.innerHTML = "Bot is thinking<span></span><span></span><span></span>";
    document.getElementById("chat").appendChild(typingIndicator);

    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message })
    })
    .then(response => response.json())
    .then(data => {
        typingIndicator.remove();
        const responseText = data.response || data.error || "Sorry, I could not respond.";
        addMessage(responseText, "bot");
    })
    .catch(() => {
        typingIndicator.remove();
        addMessage("Sorry, something went wrong.", "bot");
    });
}

document.addEventListener("DOMContentLoaded", () => {
    const input = document.getElementById("message");
    const themeToggle = document.getElementById("themeToggle");
    const panel = document.querySelector(".panel");

    input.addEventListener("keydown", (event) => {
        if (event.key === "Enter") {
            sendMessage();
        }
    });

    themeToggle.addEventListener("click", () => {
        document.body.classList.toggle("dark");
        themeToggle.textContent = document.body.classList.contains("dark") ? "☀️" : "🌙";
    });

    panel.addEventListener("mousemove", (event) => {
        const rect = panel.getBoundingClientRect();
        const x = (event.clientX - rect.left) / rect.width - 0.5;
        const y = (event.clientY - rect.top) / rect.height - 0.5;
        panel.style.transform = `perspective(1000px) rotateY(${x * 8}deg) rotateX(${y * -8}deg) translateY(-4px)`;
    });

    panel.addEventListener("mouseleave", () => {
        panel.style.transform = "";
    });
});

