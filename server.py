import flask

app = flask.Flask(__name__)

@app.route('/')
def hello():
    return flask.render_template('index.html')

@app.route('/static/<path:path>')
def serve_static(path):
    return flask.send_from_directory('static', path)

if __name__ == '__main__':
    app.run('0.0.0.0', port=8080, debug=True)
