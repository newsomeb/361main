from flask import Flask, render_template, jsonify, request
from ebay_api import search_pokemon_cards


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search')
def search():
    # get card name from query string
    card_name = request.args.get('card_name', '')
    # call ebay_api function to search eBay API
    pokemon_card_data = search_pokemon_cards(card_name)
    pokemon_card_data['card_name'] = card_name
    #return data from eBay API
    return jsonify(pokemon_card_data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)