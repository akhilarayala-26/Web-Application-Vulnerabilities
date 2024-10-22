// JavaScript for interacting with the demo app

// Function to simulate a CSRF attack by submitting a form automatically
function simulateCSRF() {
    const csrfForm = document.getElementById("csrfForm");
    if (csrfForm) {
        csrfForm.submit();
    }
}

// Function to alert the user when the XSS comment is loaded
function displayComment() {
    const commentDiv = document.getElementById("comment");
    if (commentDiv && commentDiv.innerHTML.includes("<script>")) {
        alert("XSS Vulnerability: A script has been injected!");
    }
}

// Basic client-side validation to prevent SQL injection (for educational purposes)
// This is just a demonstration and shouldn't be relied upon for real security.
function validateLoginForm() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const sqlInjectionPatterns = ["'", "\"", ";", "--", "/*", "*/"];

    for (let pattern of sqlInjectionPatterns) {
        if (username.includes(pattern) || password.includes(pattern)) {
            alert("Potential SQL Injection detected in your input.");
            return false;
        }
    }

    return true;
}

// Event listener for loading comments (XSS demonstration)
window.addEventListener("DOMContentLoaded", () => {
    displayComment();
});
