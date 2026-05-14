async function startSearch() {
    const target = document.getElementById('targetInput').value;
    const loading = document.getElementById('loading');
    const output = document.getElementById('output');
    
    if (!target) return;
    
    loading.style.display = 'block';
    output.innerHTML = '';
    
    try {
        const response = await fetch('/search', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({target})
        });
        
        const data = await response.json();
        displayResults(data);
    } catch (error) {
        output.innerHTML = `<p style="color: red;">Erreur: ${error.message}</p>`;
    } finally {
        loading.style.display = 'none';
    }
}

function displayResults(data) {
    const output = document.getElementById('output');
    
    // Dumps de données
    output.innerHTML = `
        <div class="result-section">
            <h3>🌐 Web Scraping</h3>
            <pre>${JSON.stringify(data.web, null, 2)}</pre>
        </div>
        
        <div class="result-section">
            <h3>🔓 Breaches</h3>
            ${data.breaches.map(b => `<div class="data-item">${JSON.stringify(b)}</div>`).join('')}
        </div>
        
        <div class="result-section">
            <h3>📱 Réseaux Sociaux</h3>
            ${Object.entries(data.social).map(([platform, profiles]) => 
                `<div class="data-item">${platform}: ${JSON.stringify(profiles)}</div>`
            ).join('')}
        </div>
        
        <div class="result-section">
            <h3>📊 Metadata</h3>
            <pre>${JSON.stringify(data.metadata, null, 2)}</pre>
        </div>
    `;
}
