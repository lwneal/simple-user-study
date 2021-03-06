import os
import time
import flask
import datetime
import json

OUTPUT_DIR = 'user_data/'

app = flask.Flask(__name__)


def save_request(request):
    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)

    entry = {}
    for k, v in request.form.items():
        entry[k] = v[0] if type(v) is list else v
    for k, v in request.args.items():
        entry[k] = v[0] if type(v) is list else v

    milliseconds = int(time.time() * 1000)
    filename = os.path.join(OUTPUT_DIR, 'entry_{}.json'.format(milliseconds))

    entry['timestamp'] = milliseconds
    entry['endpoint'] = request.url

    content = json.dumps(entry, indent=2) + '\n'
    with open(filename, 'w') as fp:
        fp.write(content)
    print('Saved user response to file {}'.format(filename))


@app.route('/')
def hello():
    return flask.redirect('static/intro.html')


@app.route('/submit_page1', methods=['POST'])
def submit_page1():
    save_request(flask.request)
    user_id = flask.request.form.get('user_id')
    return flask.redirect('static/page2.html?user_id={}'.format(user_id))


@app.route('/submit_page2', methods=['POST'])
def submit_page2():
    save_request(flask.request)
    user_id = flask.request.form.get('user_id')
    return flask.redirect('static/page3.html?user_id={}'.format(user_id))


@app.route('/submit_page3', methods=['POST'])
def submit_page3():
    save_request(flask.request)
    return flask.redirect('static/complete.html')


@app.route('/static/<path:path>')
def serve_static(path):
    return flask.send_from_directory('static', path)


if __name__ == '__main__':
    app.run('0.0.0.0', port=8000)
