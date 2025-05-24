function searchProducts() {
    let query = document.getElementById('search-bar').value;  // Get the value from the search bar

    // Make an AJAX request to the server with the query
    fetch(`/search/?query=${query}`)  // AJAX request to search view
        .then(response => response.json())  // Parse the JSON response
        .then(data => {
            let searchResultsContainer = document.getElementById('search-results');

            // If there is a query, show results
            if (query) {
                if (data.results.length > 0) {
                    let resultsHtml = `<h3>Search Results for "${query}"</h3><ul>`;
                    data.results.forEach(item => {
                        resultsHtml += `
                            <li>
                                <a href="/product/${item.id}/">
                                    <img src="${item.image}" alt="${item.name}" style="width:40px; height:50px;">
                                    <p class="ok">
                                    <span>${item.name}</span> 
                                    <span>$${item.price}</span>
                                    </p>
                                </a>
                            </li>`;
                    });
                    resultsHtml += '</ul>';
                    searchResultsContainer.innerHTML = resultsHtml;
                } else {
                    searchResultsContainer.innerHTML = `<h3>No products found for "${query}"</h3>`;
                }
            } else {
                // If no query, clear results container
                searchResultsContainer.innerHTML = 'Product Display Here';
            }
        });
}

function showSearchResults() {
    document.getElementById('search-results').style.display = 'block';
}

document.addEventListener('click', function (event) {
    let searchBar = document.getElementById('search-bar');
    let searchResults = document.getElementById('search-results');

    // Close the search results if the user clicks outside of the search bar or results
    if (!searchBar.contains(event.target) && !searchResults.contains(event.target)) {
        searchResults.style.display = 'none';
    }
});



