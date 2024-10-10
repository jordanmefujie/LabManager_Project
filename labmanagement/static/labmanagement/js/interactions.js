// Add custom JavaScript interactions for the lab management forms
document.addEventListener('DOMContentLoaded', function() {
    console.log("Lab management JS loaded.");
    // Add dynamic interactions if needed
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
document.addEventListener('DOMContentLoaded', highlightActiveLink);

document.addEventListener('DOMContentLoaded', function() {
    const notificationBell = document.getElementById('notification-bell');
    const notificationDropdown = document.getElementById('notification-dropdown');
    const notificationList = document.getElementById('notification-list');
    const notificationCount = document.getElementById('notification-count');
    
    // Open/Close the dropdown when the bell icon is clicked
    notificationBell.addEventListener('click', function() {
        notificationDropdown.style.display = notificationDropdown.style.display === 'none' ? 'block' : 'none';
    });

    // Connect to WebSocket for notifications
    const socket = new WebSocket('ws://' + window.location.host + '/ws/notifications/');

    socket.onmessage = function(e) {
        const data = JSON.parse(e.data);

        // Update the notification bell count
        const currentCount = parseInt(notificationCount.innerText || '0', 10);
        notificationCount.innerText = currentCount + 1;
        notificationCount.style.display = 'inline'; // Show the count

        // Add the new notification to the dropdown list
        const newNotification = document.createElement('li');
        newNotification.innerText = data.message;
        notificationList.prepend(newNotification);
    };

    socket.onclose = function(e) {
        console.error('WebSocket closed unexpectedly');
    };
});
