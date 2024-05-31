from flask import Flask, render_template
from quote_generator import daily_quote

app = Flask(__name__,static_folder='static')

quote = daily_quote()

@app.route('/')
def index_page():
    return render_template('index.html',quote=quote)

if __name__ == "__main__":
    app.run(debug=True)
    
    