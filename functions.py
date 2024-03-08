from secrets import API_KEY
from pprint import pprint
import requests
BASE_URL = "https://api.spoonacular.com/"

def search_recipe(query):
    url = BASE_URL + 'recipes/complexSearch'
    params = {
        'apiKey' : API_KEY,
        'query' : query,
        'number' : 10,
        'instructionsRequired' : True
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data['results']

    return []

def search_recipe_by_ingredients(ingredients, ranking, number):
    url = BASE_URL + 'recipes/findByIngredients'
    params = {
        'apiKey' : API_KEY,
        'ingredients' : ingredients,
        'number' : number,
        'instructionsRequired' : True,
        'ranking' : ranking
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    return []

def main():
    print("Hello World")
    #pprint(search_recipe("Pasta"))
    pprint(search_recipe_by_ingredients("chicken", 1, 3))

if __name__ == "__main__":
    try:
        main()
    except (NameError, SyntaxError):
        # pass does "nothing" - it is useful if you are trying to nothing in your code,
        # but still need a line to avoid a syntax error
        pass