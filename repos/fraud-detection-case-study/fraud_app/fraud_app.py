# Demonstrates Bootstrap version 3.3 Starter Template
# available here: https://getbootstrap.com/docs/3.3/getting-started/#examples

from flask import Flask, render_template,request
import os 

app = Flask(__name__)

# home page
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello', methods=['POST'])
def tab_name():
    """Render a page containing a text area input where the user can paste an
    description to be classified."""    
    return render_template('tab_name.html')


@app.route('/score', methods=['GET'])
def another_tab_name():
    return render_template('another_tab_name.html')

if __name__ == '__main__':
    

    app.run(host='0.0.0.0', port=8080, threaded=True, debug=True, )
