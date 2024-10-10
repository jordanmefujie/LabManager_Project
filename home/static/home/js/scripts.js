/**
 * Perform a search and filter action based on user input.
 */
function performSearch() {
    // Get the value of the search input
    const searchQuery = document.getElementById('search').value.toLowerCase();
    
    // Get the selected filter option
    const filterStatus = document.getElementById('filter-status').value;

    // Example data structure to simulate the items being searched (replace this with real data)
    const items = [
        { name: 'Experiment 1', status: 'completed' },
        { name: 'Experiment 2', status: 'in-progress' },
        { name: 'Experiment 3', status: 'pending' },
        { name: 'Experiment 4', status: 'completed' }
    ];

    // Filter items based on search query and filter status
    const filteredItems = items.filter(item => {
        const matchesSearch = item.name.toLowerCase().includes(searchQuery);
        const matchesFilter = filterStatus === 'all' || item.status === filterStatus;
        return matchesSearch && matchesFilter;
    });

    // Log the filtered items (this can be replaced with actual UI rendering code)
    console.log('Filtered Items:', filteredItems);

    // Render the results (if needed, implement this part in your UI)
    renderSearchResults(filteredItems);
}

/**
 * Render search results to the UI (to be implemented based on your HTML structure).
 * @param {Array} items - The filtered items to be displayed.
 */
function renderSearchResults(items) {
    // Example: Display the filtered results in a list (replace this with your HTML structure)
    const resultsContainer = document.getElementById('results-container');
    resultsContainer.innerHTML = ''; // Clear previous results

    if (items.length === 0) {
        resultsContainer.innerHTML = '<p>No results found.</p>';
    } else {
        items.forEach(item => {
            const listItem = document.createElement('li');
            listItem.textContent = `${item.name} (${item.status})`;
            resultsContainer.appendChild(listItem);
        });
    }
}

// Add hover effect to social media icons
const socialIcons = document.querySelectorAll('.social-media .social-icon');

socialIcons.forEach(icon => {
    icon.addEventListener('mouseover', () => {
        icon.style.transform = 'scale(1.2)';
        icon.style.transition = 'transform 0.3s';
    });

    icon.addEventListener('mouseout', () => {
        icon.style.transform = 'scale(1)';
    });
});

// Add click alert for external links
const externalLinks = document.querySelectorAll('.external-links ul li a');

externalLinks.forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        alert(`You are about to visit ${link.href}`);
        window.open(link.href, '_blank');
    });
});
