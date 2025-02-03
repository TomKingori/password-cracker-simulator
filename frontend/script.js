const serverURL = "http://localhost:3000";
let isSignUp = false; // Track if we're in sign-up mode

// Toggle between Login and Sign Up
function toggleForm() {
    isSignUp = !isSignUp;
    document.getElementById("form-title").innerText = isSignUp ? "Sign Up" : "Login";
    document.querySelector("button").innerText = isSignUp ? "Sign Up" : "Login";
    document.getElementById("toggle-form").innerHTML = isSignUp
        ? `Already have an account? <a href="#" onclick="toggleForm()">Login</a>`
        : `Don't have an account? <a href="#" onclick="toggleForm()">Sign Up</a>`;
}

// Handle Login / Sign Up
async function handleSubmit() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const endpoint = isSignUp ? "/register" : "/login";

    const response = await fetch(`${serverURL}${endpoint}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
    });

    const data = await response.json();
    document.getElementById("message").innerText = data.message || data.error;
}
