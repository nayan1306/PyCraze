from flask import Flask, jsonify, render_template
from assets import recipe

app = Flask(__name__,static_folder='assets', static_url_path='/assets')

recipes = recipe.recipes_data


@app.route('/')
def index_page():
    return render_template('index.html',recipes=recipes['recipes'])

@app.route('/api/recipe')
def list_recipe():
    return jsonify(recipes)

if __name__ == "__main__":
    app.run(debug=True)
