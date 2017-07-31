from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///application.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Shows all applications in the database
@app.route('/')
@app.route('/application')
def showApplications():
    return "This page will display all created applications"

# Creates a new application by the user
@app.route('/application/new')
def newApplication():
    return "This page will create a new application for the user"

# Edits application created by the user
@app.route('/application/<int:application_id>/edit')
def editApplication():
    return "This page will edit an application created by the user"

# Deletes application created by the user
@app.route('/application/<int:application_id>/delete')
def deleteApplication():
    return "This page will delete an application created by the user"

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
