#!/usr/bin/env python

import flask
from flask import request, flash

# Create the application.
APP = flask.Flask(__name__)


@APP.route('/', methods=['POST', 'GET'])
def index():
    """ Displays the index page accessible at '/'
    """
    if request.method == 'POST':
        print request.form['filename']
        flash("File data saved.")
    return flask.render_template('index.html')


if __name__ == '__main__':
    APP.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    APP.debug=True
    APP.run()