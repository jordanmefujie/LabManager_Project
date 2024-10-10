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
