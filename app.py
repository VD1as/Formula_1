from flask import Flask, render_template
from f1_data_loader import load_data

app = Flask(__name__)

drivers, constructors, circuits, races, championships = load_data()

@app.route('/')
def index():
    return render_template('index.html', championships=championships)

if __name__ == '__main__':
    app.run(debug=True)
