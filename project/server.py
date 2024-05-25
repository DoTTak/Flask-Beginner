from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def index():
    random_color = "#%06x" % random.randint(0, 0xFFFFFF)
    return "Random: " + \
        "<strong style='color: "+random_color+";'>" + \
            str(random.random()) + \
        "</strong>"

app.run(port=8000, debug=True)