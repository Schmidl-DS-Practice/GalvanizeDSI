from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello!'


@app.route('/rainbow')
def rainbow():
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    color_divs = []
    for i in xrange(1000):
        color = colors[i % len(colors)]
        div = '''<div style="background-color: {0};
                             color: white;
                             text-align: center;">
                     {1}
                 </div>'''.format(color, '*' * 100)
        color_divs.append(div)
    return '''
            <!DOCTYPE html>
            <html>
                <head>
                    <meta charset="utf-8">
                    <title>Rainbow</title>
                </head>
                <body>{0}</body>
            </html>
            '''.format('\n'.join(color_divs))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
