import functions
from flask import Flask, render_template, request, session
from pprint import pprint
from secrets import token_hex

app = Flask(__name__)
app.secret_key = token_hex(16)

@app.route('/')
def index():
    return render_template("index.html")
@app.route("/results", methods=["GET", "POST"])
def results():
    if request.method == "POST":
        form_data = request.form
        pprint(form_data)
        recipes = functions.search_recipe_by_ingredients(form_data["ingredients"], form_data["number"], form_data["ranking"])

        session["recipes"] = recipes
        session["ingredients"] = form_data["ingredients"]

        return render_template("results-flexbox.html", recipes = recipes, ingredients=form_data["ingredients"])

    elif request.method == "GET" and len(session) != 0:

        return render_template("results-flexbox.html", recipes=session["recipes"], ingredients=session["ingredients"])

    return "Wrong HTTP method", 400

@app.route("/results/<recipe_id>")
def render_recipe(recipe_id):
    pprint(session)
    recipe = functions.get_recipe_info(recipe_id)
    return render_template("render-recipe.html", recipe = recipe)

if __name__ == '__main__':
    app.run(debug=True)