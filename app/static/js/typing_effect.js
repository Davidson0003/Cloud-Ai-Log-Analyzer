// typing_effect.js
// Simple hacker typing effect for intro screens

document.addEventListener("DOMContentLoaded", () => {
    const element = document.getElementById("typing-text");
    if (!element) return;

    const text = "Initializing Cloud AI Engine... Access Granted.";
    let index = 0;

    function typeEffect() {
        if (index < text.length) {
            element.innerHTML += text.charAt(index);
            index++;
            setTimeout(typeEffect, 80);
        }
    }

    typeEffect();
});
