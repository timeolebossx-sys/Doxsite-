from flask import Flask, render_template, request, jsonify
from modules.scraper import WebScraper
from modules.breach import BreachChecker
from modules.social import SocialFinder
import asyncio
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    target = data.get('target')
    
    scraper = WebScraper()
    breach = BreachChecker()
    social = SocialFinder()
    
    results = {
        'web': scraper.search(target),
        'breaches': breach.check(target),
        'social': social.find_all(target),
        'metadata': scraper.get_metadata(target)
    }
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
