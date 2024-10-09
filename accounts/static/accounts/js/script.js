// Function to toggle password visibility
function togglePasswordVisibility() {
    const passwordInput = document.getElementById('password');
    const toggleIcon = document.getElementById('toggle-password-visibility');

    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        toggleIcon.classList.remove('fa-eye');
        toggleIcon.classList.add('fa-eye-slash');
    } else {
        passwordInput.type = 'password';
        toggleIcon.classList.remove('fa-eye-slash');
        toggleIcon.classList.add('fa-eye');
    }
}

// Attach event listener to the password visibility toggle icon
document.addEventListener('DOMContentLoaded', function() {
    const toggleIcon = document.getElementById('toggle-password-visibility');
    toggleIcon.addEventListener('click', togglePasswordVisibility);
});

document.addEventListener('DOMContentLoaded', function () {
    const registerForm = document.querySelector('.register-container form');
    const password1 = document.getElementById('password1');
    const password2 = document.getElementById('password2');

    registerForm.addEventListener('submit', function (event) {
        const passwordError = document.querySelector('.password-error');
        if (password1.value !== password2.value) {
            event.preventDefault();  // Prevent form submission
            if (!passwordError) {
                // Display error message if passwords do not match
                const errorMessage = document.createElement('p');
                errorMessage.textContent = "Passwords do not match!";
                errorMessage.classList.add('error-message', 'password-error');
                password2.parentNode.appendChild(errorMessage);
            }
        } else {
            // Remove the error message if passwords match
            if (passwordError) {
                passwordError.remove();
            }
        }
    });

    // Remove the error message when the user starts typing in the password fields
    password1.addEventListener('input', function () {
        const passwordError = document.querySelector('.password-error');
        if (passwordError) {
            passwordError.remove();
        }
    });

    password2.addEventListener('input', function () {
        const passwordError = document.querySelector('.password-error');
        if (passwordError) {
            passwordError.remove();
        }
    });
});

// Function to highlight the active navigation link
function highlightActiveLink() {
    // Get the current URL path
    const currentPath = window.location.pathname;

    // Get all navigation links
    const navLinks = document.querySelectorAll('nav ul li a');

    // Loop through each link and compare its href with the current URL
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            // Add the 'active' class to the matching link
            link.classList.add('active');
        }
    });
}

// Call the function when the page loads
document.addEventListener('DOMContentLoaded', highlightActiveLink);:

document.addEventListener('DOMContentLoaded', function () {
    const profileForm = document.getElementById('profile-form');

    profileForm.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent the default form submission

        // Handle the form submission (e.g., using AJAX or a fetch request)
        alert('Profile updated successfully!');

        // Optionally, you can submit the form after processing
        // profileForm.submit();
    });
});
