import flask
import datetime

app = flask.Flask(__name__)

@app.route('/')
def hello():
    kwargs = {
        'current_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    }
    return flask.render_template('index.html', **kwargs)


@app.route('/submit_page1', methods=['POST'])
def submit_page1():
    # TODO: save the user's input to a file
    print('Submission from page 1: {}'.format(flask.request.data))
    return flask.redirect('static/page2.html')


@app.route('/static/<path:path>')
def serve_static(path):
    return flask.send_from_directory('static', path)

if __name__ == '__main__':
    app.run('0.0.0.0', port=8080, debug=True)
