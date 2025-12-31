// ===============================
// HACKER DASHBOARD SCRIPT
// ===============================

// Terminal typing effect
const terminalText = document.getElementById("terminal-text");
const messages = [
    "Initializing Cloud AI Log Analyzer...",
    "Connecting to cloud services...",
    "Scanning system logs...",
    "Detecting anomalies...",
    "AI engine online.",
    "Awaiting log upload..."
];

let msgIndex = 0;
let charIndex = 0;

function typeEffect() {
    if (!terminalText) return;

    if (charIndex < messages[msgIndex].length) {
        terminalText.innerHTML += messages[msgIndex].charAt(charIndex);
        charIndex++;
        setTimeout(typeEffect, 50);
    } else {
        setTimeout(() => {
            terminalText.innerHTML = "";
            charIndex = 0;
            msgIndex = (msgIndex + 1) % messages.length;
            typeEffect();
        }, 1500);
    }
}

typeEffect();

// ===============================
// Fake real-time system stats
// ===============================
function randomNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function updateStats() {
    const totalLogs = document.getElementById("total-logs");
    const errorLogs = document.getElementById("error-logs");
    const warningLogs = document.getElementById("warning-logs");

    if (!totalLogs) return;

    totalLogs.innerText = randomNumber(200, 1200);
    errorLogs.innerText = randomNumber(5, 50);
    warningLogs.innerText = randomNumber(10, 80);
}

setInterval(updateStats, 2000);

// ===============================
// Glitch effect on hover
// ===============================
const glitchElements = document.querySelectorAll(".glitch");

glitchElements.forEach(el => {
    el.addEventListener("mouseover", () => {
        el.classList.add("glitch-active");
    });

    el.addEventListener("mouseout", () => {
        el.classList.remove("glitch-active");
    });
});

// ===============================
// Hacker console sound (optional)
// ===============================
document.addEventListener("click", () => {
    const audio = document.getElementById("key-sound");
    if (audio) {
        audio.currentTime = 0;
        audio.play();
    }
});
