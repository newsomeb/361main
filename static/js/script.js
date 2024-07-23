document.addEventListener('DOMContentLoaded', function() {
    const searchForm = document.getElementById('search-form');
    const resultsContainer = document.getElementById('results');

    // Event listener for form submission
    searchForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const cardName = document.getElementById('searchbar').value;

        // Make request to server with the search bar input
        fetch(`/search?card_name=${encodeURIComponent(cardName)}`)
            .then(response => response.json())
            .then(data => displayResults(data))

            .catch(error => resultsContainer.innerHTML = `<p>Error: ${error.message}</p>`);


    });

    // Function to display data from data in results container
    function displayResults(data) {
        if (data.num_listings > 0) {
        // display price statistics if results are found
            resultsContainer.innerHTML = `
                <h2> Results for "${data.card_name}"</h2>
                <p>Lowest: $${data.lowest_price.toFixed(2)}</p>
                <p>Highest: $${data.highest_price.toFixed(2)}</p>
                <p>Average: $${data.average_price.toFixed(2)}</p>
                <p>Number of Listings: ${data.num_listings}</p>
            `;
        } else {
        // return no listings if none are found
            resultsContainer.innerHTML = `<p> No listings </p>`;
        }

    }
});

