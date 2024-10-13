document.getElementById('cityInput').addEventListener('input', function() {
    let query = this.value;
    if (query.length > 2) { // Trigger search after 3 characters
        fetch(`/search-labs?city=${query}`)
            .then(response => response.json())
            .then(data => {
                let suggestionsBox = document.getElementById('suggestions');
                suggestionsBox.innerHTML = ''; // Clear previous suggestions

                data.labs.forEach(lab => {
                    let suggestionItem = document.createElement('div');
                    suggestionItem.textContent = lab.name;
                    suggestionsBox.appendChild(suggestionItem);
                });
            })
            .catch(error => console.error('Error fetching lab data:', error));
    }
});

function searchLabs() {
    let query = document.getElementById('cityInput').value;
    fetch(`/search-labs?city=${query}`)
        .then(response => response.json())
        .then(data => {
            let suggestionsBox = document.getElementById('suggestions');
            suggestionsBox.innerHTML = ''; // Clear previous suggestions

            data.labs.forEach(lab => {
                let suggestionItem = document.createElement('div');
                suggestionItem.textContent = lab.name;
                suggestionsBox.appendChild(suggestionItem);
            });
        })
        .catch(error => console.error('Error fetching lab data:', error));
}
        function performSearch() {
            const searchQuery = document.getElementById('search').value;
            const filterStatus = document.getElementById('filter-status').value;
            // Implement search and filter functionality here
            console.log(`Search Query: ${searchQuery}, Filter Status: ${filterStatus}`);
        }
        const toggle = document.getElementById('theme-toggle');
    toggle.addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');
    });
