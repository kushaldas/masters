#!/usr/bin/env python

import os
import flask
import json
from flask import request, flash

# Create the application.
APP = flask.Flask(__name__)


@APP.route('/', methods=['POST', 'GET'])
def index():
    """ Displays the index page accessible at '/'
    """
    msg = ''
    if request.method == 'POST':
        o = {}

        o['filename'] = request.form['filename'].strip()
        if request.form['radios'] == 'A':
            o['typeside'] = 'Appellete'
        else:
            o['typeside'] = 'Original'
        o['typecase'] = request.form['typecase'].strip()
        o['casenumber'] = request.form['casenumber'].strip()
        o['casename'] = request.form['casename'].strip()
        o['heardon'] = request.form['heardon'].strip()
        o['judgementdate'] = request.form['judgementdate'].strip()
        o['bench'] = request.form['bench'].strip()
        o['padvocate'] = request.form['petitioner'].strip()
        o['oadvocate'] = request.form['opposite'].strip()

        try:
           outstring = json.dumps(o,indent=4,sort_keys=True)
           filename = o['filename'][:-3] + 'json'
           filename = os.path.join('output',filename)
           if os.path.exists(filename):
               msg = "File already exists."
           else:
               with open(filename, 'w') as fobj:
                   fobj.write(outstring)
               msg =  filename + ' saved properly.'
        except Exception, err:
            print err
            flash("Error in saving data.")
        else:
            flash(msg)
    return flask.render_template('index.html')


if __name__ == '__main__':
    APP.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    APP.debug=True
    APP.run()