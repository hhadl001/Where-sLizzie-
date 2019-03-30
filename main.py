# accesses flak's libraries and import the one holding Flask itse;f
from flask import Flask , render_template, request
import requests
import json
import pprint
from airtable import Airtable
from pprint import pprint
#defines the app as a function called Flask using arguments called "my app"
app = Flask("MyApp")
api_key = "keyXMnAiofGSmJtgA"
airtable = Airtable("app3lZZfvIqAj2lwc", "Log")

#decorator that talks to the server and flask
@app.route("/")
#defines a function called hello using arguments visitor
def hello():
    #defines variable m string + visitor variable's title
    m = "Welcome to my page"
#return's the result of a new function using the index file and variable m
    return render_template("index.html", message=m)
#decorator talks to the server and flask

def addEntry_in_airtable(serialnumber, location, date, notes):
    recordEntry = '["fields": {serialnumber:'+serialnumber +'}, {location:'+location +'}, {date:'+date +'}, {notes:'+notes +'}]'
    response = requests.post('https://api.airtable.com/v0/app3lZZfvIqAj2lwc/Log', data=recordEntry)
    print response.url
    print response.status_code

def addEntry_in_airtable2(serialnumber, location, date, notes):
    records = {'serialnumber': serialnumber, 'location': location,  'date': date,  'notes': notes}
    airtable = Airtable("app3lZZfvIqAj2lwc", "Log")
    airtable.insert(records)

@app.route("/recordEntry" , methods=["POST"])
#defines a function called hello using arguments visitor


def newEntry():
    form_data = request.form #Getting hold of a Form object that is sent from a browser.
    serialnumber = form_data["serialnumber"]
    location = form_data["location"]
    date = form_data["date"]
    notes = form_data["notes"]
    addEntry_in_airtable2(serialnumber, location, date, notes)
    travels = airtable.search('serialnumber', serialnumber)
    return render_template("trace.html", message=travels)

#json.load method converts JSON string to Python Object
#decorator talks to the server and flask

#keyXMnAiofGSmJtgA
app.run(debug=True)




# from flask import Flask
#
# app = Flask("MyApp")
#
# @app.route("/<visitor>")
# def hello(visitor):
#     m = "Welcome to my page:" + vistor.title()
#     return render_template("index.html", message=m)
#     #return "Hello World"
# @app.route("/welcome")
# def welcome():
#     return "Hello welcome to my page"
#
# app.run(debug=True)
