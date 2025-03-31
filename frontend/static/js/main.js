document.addEventListener('DOMContentLoaded', () => {
    let allQuotes = [];
    const quotesContainer = document.getElementById('quotes-container');
    const authorFilter = document.getElementById('author-filter');
    const searchInput = document.getElementById('search-input');
    const randomQuoteBtn = document.getElementById('random-quote-btn');
    
    // Fetch all quotes
    fetch('/api/quotes')
        .then(response => response.json())
        .then(data => {
            allQuotes = data;
            displayQuotes(allQuotes);
            populateAuthorFilter(allQuotes);
            displayRandomQuote();
        })
        .catch(error => console.error('Error fetching quotes:', error));
    
    // Display random quote in featured section
    function displayRandomQuote() {
        fetch('/api/random-quote')
            .then(response => response.json())
            .then(quote => {
                document.getElementById('featured-text').textContent = quote.text;
                document.getElementById('featured-author').textContent = `— ${quote.author}`;
                
                const tagsElement = document.getElementById('featured-tags');
                tagsElement.innerHTML = '';
                quote.tags.forEach(tag => {
                    const tagSpan = document.createElement('span');
                    tagSpan.className = 'tag';
                    tagSpan.textContent = tag;
                    tagsElement.appendChild(tagSpan);
                });
            })
            .catch(error => console.error('Error fetching random quote:', error));
    }
    
    // Display all quotes
    function displayQuotes(quotes) {
        quotesContainer.innerHTML = '';
        
        quotes.forEach(quote => {
            const quoteCard = document.createElement('div');
            quoteCard.className = 'card';
            
            const quoteText = document.createElement('p');
            quoteText.className = 'quote-text';
            quoteText.textContent = quote.text;
            
            const quoteAuthor = document.createElement('cite');
            quoteAuthor.className = 'quote-author';
            quoteAuthor.textContent = `— ${quote.author}`;
            
            const quoteTags = document.createElement('div');
            quoteTags.className = 'quote-tags';
            
            quote.tags.forEach(tag => {
                const tagSpan = document.createElement('span');
                tagSpan.className = 'quote-tag';
                tagSpan.textContent = tag;
                quoteTags.appendChild(tagSpan);
            });
            
            quoteCard.appendChild(quoteText);
            quoteCard.appendChild(quoteAuthor);
            quoteCard.appendChild(quoteTags);
            
            quotesContainer.appendChild(quoteCard);
        });
    }
    
    // Populate author filter dropdown
    function populateAuthorFilter(quotes) {
        const authors = [...new Set(quotes.map(quote => quote.author))];
        authors.sort();
        
        authors.forEach(author => {
            const option = document.createElement('option');
            option.value = author;
            option.textContent = author;
            authorFilter.appendChild(option);
        });
    }
    
    // Filter quotes by author and search term
    function filterQuotes() {
        const authorValue = authorFilter.value;
        const searchValue = searchInput.value.toLowerCase();
        
        const filteredQuotes = allQuotes.filter(quote => {
            const matchesAuthor = authorValue === '' || quote.author === authorValue;
            const matchesSearch = searchValue === '' || 
                                quote.text.toLowerCase().includes(searchValue) ||
                                quote.author.toLowerCase().includes(searchValue) ||
                                quote.tags.some(tag => tag.toLowerCase().includes(searchValue));
            
            return matchesAuthor && matchesSearch;
        });
        
        displayQuotes(filteredQuotes);
    }
    
    // Event listeners
    authorFilter.addEventListener('change', filterQuotes);
    searchInput.addEventListener('input', filterQuotes);
    randomQuoteBtn.addEventListener('click', displayRandomQuote);
});