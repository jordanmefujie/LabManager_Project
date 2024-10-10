document.getElementById('commodity-search').addEventListener('input', function() {
    const searchValue = this.value.toLowerCase();
    // Code to filter commodities in the dashboard
});

document.getElementById('filter-category').addEventListener('change', function() {
    const selectedCategory = this.value;
    // Code to filter commodities by category
});

document.getElementById('filter-status').addEventListener('change', function() {
    const selectedStatus = this.value;
    // Code to filter commodities by status
});
// logistics.js

document.addEventListener('DOMContentLoaded', function() {
    // Add logic here for handling real-time updates in logistics
    // E.g., fetching updated stock levels via AJAX, updating the DOM, etc.
});

document.addEventListener('DOMContentLoaded', function () {
    const logisticsOverview = document.getElementById('logistics-overview');
    const socket = new WebSocket('ws://' + window.location.host + '/ws/logistics/');

    socket.onmessage = function (event) {
        const data = JSON.parse(event.data);
        logisticsOverview.innerHTML = '';  // Clear current data
        data.commodities.forEach(commodity => {
            const item = document.createElement('div');
            item.textContent = `${commodity.name}: ${commodity.quantity}`;
            logisticsOverview.appendChild(item);
        });
    };

    socket.onclose = function (event) {
        console.error('WebSocket closed unexpectedly');
    };
});

const socket = new WebSocket('ws://' + window.location.host + '/ws/logistics/');

socket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    alert(data.message);  // Notify the user of real-time updates.
    location.reload();  // Reload the page to update the logistics view.
};
