#!/usr/bin/env python
from flask import Flask, render_template, request
from airtable import Airtable
import requests
import json
from json2table import convert

app = Flask("MyApp")
api_key = "keyXMnAiofGSmJtgA"
API_URL = 'https://api.airtable.com/v%s/'
API_VERSION = '0'
table = Airtable('app3lZZfvIqAj2lwc', "Log")

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

def addEntry_in_airtable2(serialnumber, location, date, notes, typecast=False):
    table = Airtable("app3lZZfvIqAj2lwc", "Log")
    records = {'serialnumber': serialnumber, 'location': location,  'date': date,  'notes': notes}
    table.insert(records)

@app.route("/recordEntry" , methods=["POST"])
#defines a function called hello using arguments visitor


def newEntry():
    form_data = request.form #Getting hold of a Form object that is sent from a browser.
    serialnumber = form_data["serialnumber"]
    location = form_data["location"]
    date = form_data["date"]
    notes = form_data["notes"]
    addEntry_in_airtable2(serialnumber, location, date, notes)
    travels = table.search('serialnumber', serialnumber)
    msg = ""
    for x in range (0, len(travels)):
        json_object = travels[x]
        json_object = json_object["fields"]
        build_direction = "TOP_TO_BOTTOM"
        table_attributes = {"style" : "width:100%", "class" : "table table-striped"}
        html = convert(json_object, build_direction=build_direction, table_attributes=table_attributes)
        msg = msg + html
    return render_template("trace.html", message=msg)

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
