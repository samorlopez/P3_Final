from secret_api import API_KEY
from pprint import pprint
import requests
BASE_URL = "https://api.spoonacular.com/"

def search_recipe_by_ingredients(ingredients, number, ranking):
    url = BASE_URL + 'recipes/findByIngredients'
    params = {
        'apiKey' : API_KEY,
        'ingredients' : ingredients,
        'number' : number,
        'instructionsRequired' : True,
        'ranking' : ranking,
        'ignorePantry' : True
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        #pprint(data)
        return data
    return []

def search_recipe_required_ingredients(ingredients, number):
    url = BASE_URL + 'recipes/complexSearch'
    params = {
        'apiKey' : API_KEY,
        'number' : number,
        'includeIngredients' : ingredients,
        'instructionsRequired' : True,
        'ignorePantry' : True,
        'fillIngredients' : True
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        pprint(data)
        return data['results']
    return []

def get_recipe_info(recipe_id):
    url = BASE_URL + 'recipes/' + recipe_id + '/information'
    params = {
        'apiKey': API_KEY,
        'includeNutrition' : False
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    return []

def main():
    print("Hello World")
    pprint(search_recipe_required_ingredients("chicken"))

if __name__ == "__main__":
    try:
        main()
    except (NameError, SyntaxError):
        # pass does "nothing" - it is useful if you are trying to nothing in your code,
        # but still need a line to avoid a syntax error
        pass