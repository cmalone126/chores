import requests
from flask import Flask, jsonify, request, render_template, redirect, url_for, flash
from flask_restful import Resource, Api
from dbops import DBFriend
import json
from quotes import Quote
from forms import NewChoreForm
from config import Config
import sys


app = Flask(__name__)
app.config.from_object(Config)


@app.route('/services/chores/complete/<int:chore_id>/<int:gameplan>', methods=['POST'])
def complete(chore_id, gameplan):
    myFriend = DBFriend()
    print(chore_id, file=sys.stderr)
    print(gameplan, file=sys.stderr)
    if gameplan == 0:
        myFriend.completeChores(chore_id)
        return redirect(url_for('main_web_page'))
    elif gameplan == 1:
        myFriend.deleteChore(chore_id)
        return redirect(url_for('main_web_page'))
"""
**************************************************
Web Routings
**************************************************
"""

@app.route('/')
def main_web_page():
    """
    ************************************************************
    Get quote data from quote.py
    ************************************************************
    """
    quoteObject = Quote()
    quoteData = quoteObject.swanson()

    """
    *************************************************************
    Get open chores
    *************************************************************
    """
    choreJSON = []
    choreDB = DBFriend()
    choreJSON = choreDB.openChores()

    """
    ***************************************************************
    Stuff for base
    ***************************************************************
    """
    choreCount = choreDB.choreCount()


    return render_template('index.html', quote = quoteData, \
        chores = choreJSON, choreCount = choreCount)

@app.route('/NewChore', methods = ['GET','POST'])
def newChore():
    choreDB = DBFriend()
    form = NewChoreForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('Form is not valid')
            form = NewChoreForm()
            choreCount = choreDB.choreCount()
            return render_template('newChore.html', choreCount = choreCount, form = form)
        else:
            meChore = choreDB.createChores(form.choreName.data, form.choreDescription.data)
            flash('Chore Added')
            return redirect('/')
    elif request.method == 'GET':
        choreCount = choreDB.choreCount()
        return render_template('newChore.html', choreCount = choreCount, form = form)



@app.route('/quickChore', methods = ['GET','POST'])
def quickChore():
    if request.method == 'POST':
        if request.form.get('Chickens') == 'Chickens':
            meDB = DBFriend()
            meDB.createChores('Chickens', 'Give the chickens food, water and get eggs')
        return render_template('quickChore.html')
    elif request.method == 'GET':
        return render_template('quickChore.html')

@app.route('/storeList', methods = ['GET','POST'])
def storeList():
    storeDB = DBFriend()
    if request.method == 'GET':
        render_template('list.html')

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
