from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def index():
    return "Random: " + "<strong>" + str(random.random()) + "</strong>"

app.run(port=8000, debug=True)