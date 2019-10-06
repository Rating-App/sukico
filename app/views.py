import datetime
import json

import requests

from app import app

from flask import Flask, render_template, request, make_response, session

def check_auth(resp):

    print(request.cookies)
    if 'userid' not in request.cookies:
        print("SETTING USERID")
        user = User()
        db.session.add(user)
        db.session.commit()

        resp.set_cookie("userid", user.userid)

    return resp

@app.route('/')
def index():
    resp = make_response(render_template('index.html',
                                         AO_sInteger = session.get('AO_sInteger')))
    return check_auth(resp)

