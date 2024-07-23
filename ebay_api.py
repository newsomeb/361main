from ebaysdk.finding import Connection as Finding

import statistics

def search_pokemon_cards(keywords, condition='Used', sort_order='PricePlusShippingLowest'):
    # establish connection to eBay API via .yaml file
    api = Finding(config_file="ebay.yaml", siteid="EBAY-US")
    api_request = {
        'keywords': keywords,
        'itemFilter': [
            {'name': 'Condition', 'value': condition},

        ],
        'sortOrder': sort_order,
        'paginationInput': {
            'entriesPerPage': 100
        }

    }
    response = api.execute('findItemsAdvanced', api_request)

    prices = []
    # parse response to extract prices from items
    for item in response.reply.searchResult.item:
        price = float(item.sellingStatus.currentPrice.value)
        prices.append(price)

    # calculate and return price statistics if prices are found
    if prices:
        return {
            'lowest_price': min(prices),
            'highest_price': max(prices),
            'average_price': statistics.mean(prices),
            'num_listings': len(prices)
        }
    else:
        # return none if no prices are found
        return {
            'lowest_price': None,
            'highest_price': None,
            'average_price': None,
            'num_listings': 0
        }
