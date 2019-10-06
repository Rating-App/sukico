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

def make_page(page):
    resp = make_response(render_template(page,
                                         AO_sInteger = session.get('AO_sInteger')))
    return check_auth(resp)

@app.route('/')
def index_page():
    return make_page('index.html')

@app.route('/about/')
def about_page():
    resp = make_response(render_template('about.html',
                                         AO_sInteger = session.get('AO_sInteger'),
                                         userid=request.cookies.get('userid')))
    return check_auth(resp)

@app.route('/contact/')
def contact_page():
    return make_page('contact.html')

@app.route('/settings/')
def settings_page():
    return make_page('settings.html')

@app.route('/new_item/')
def new_item():
    return ""
