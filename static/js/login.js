// Show Email Login Form
function showEmailLogin() {

    document.getElementById("login-options").style.display = "none";

    document.getElementById("email-login").style.display = "block";
}

// Back to Login Options
function goBack() {

    document.getElementById("email-login").style.display = "none";

    document.getElementById("login-options").style.display = "block";
}

// Show / Hide Password
function togglePassword() {

    let password = document.getElementById("password");

    let eye = document.getElementById("eye");

    if (password.type === "password") {

        password.type = "text";

        eye.classList.remove("fa-eye");
        eye.classList.add("fa-eye-slash");

    } else {

        password.type = "password";

        eye.classList.remove("fa-eye-slash");
        eye.classList.add("fa-eye");
    }
}

// Fade Animation
window.onload = function () {

    document.querySelector(".login-card").style.opacity = "0";
    document.querySelector(".login-card").style.transform = "translateY(30px)";

    setTimeout(() => {

        document.querySelector(".login-card").style.transition = "0.6s";

        document.querySelector(".login-card").style.opacity = "1";

        document.querySelector(".login-card").style.transform = "translateY(0)";

    }, 200);

};