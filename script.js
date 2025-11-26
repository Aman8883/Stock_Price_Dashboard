const API_URL = 'http://127.0.0.1:8000';

async function fetchStocks() {
    try {
        const response = await fetch(`${API_URL}/stocks`);
        const stocks = await response.json();
        const container = document.getElementById('stocks-container');
        container.innerHTML = '';
        
        stocks.forEach(stock => {
            addStockCard(stock);
        });
    } catch (error) {
        console.error('Error fetching stocks:', error);
    }
}

async function trackStock() {
    const input = document.getElementById('stock-symbol');
    const button = document.getElementById('track-btn');
    const errorMsg = document.getElementById('error-message');
    const symbol = input.value.toUpperCase().trim();

    if (!symbol) return;

    button.disabled = true;
    button.textContent = 'Loading...';
    errorMsg.textContent = '';

    try {
        const response = await fetch(`${API_URL}/stock/${symbol}`);
        
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail || 'Failed to fetch stock');
        }

        const stock = await response.json();
        
        // Remove existing card if it exists (to update it)
        const existingCard = document.getElementById(`card-${stock.symbol}`);
        if (existingCard) {
            existingCard.remove();
        }

        addStockCard(stock, true); // true = prepend
        input.value = '';
    } catch (error) {
        errorMsg.textContent = error.message;
    } finally {
        button.disabled = false;
        button.textContent = 'Track Price';
    }
}

function addStockCard(stock, prepend = false) {
    const container = document.getElementById('stocks-container');
    const card = document.createElement('div');
    card.className = 'card';
    card.id = `card-${stock.symbol}`;
    
    // Format date nicely
    const date = new Date(stock.date);
    const dateStr = date.toLocaleString();

    card.innerHTML = `
        <div class="card-header">
            <span class="symbol">${stock.symbol}</span>
        </div>
        <div class="price">$${stock.price.toFixed(2)}</div>
        <div class="date">Last updated: ${stock.date}</div>
    `;

    if (prepend) {
        container.prepend(card);
    } else {
        container.appendChild(card);
    }
}

// Allow Enter key to submit
document.getElementById('stock-symbol').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        trackStock();
    }
});

// Load stocks on start
fetchStocks();
