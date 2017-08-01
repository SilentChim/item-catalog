from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///application.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Main Handlers
# Shows all applications
@app.route('/')
@app.route('/application')
def showApplications():
    return "This page will display all created applications"

# Creates new application
@app.route('/application/new', methods=['GET','POST'])
def newApplication():
    return "This page will create a new application for the user"

# Edit exhisting application
@app.route('/application/<int:application_id>/edit', methods=['GET','POST'])
def editApplication(application_id):
    return "This page will edit an application created by the user"

# Deletes exhisting application
@app.route('/application/<int:application_id>/delete', methods=['GET','POST'])
def deleteApplication(application_id):
    return "This page will delete an application created by the user"

@app.route('/application/<int:application_id>/', methods=['GET','POST'])
def showFeatures(application_id):


@app.route('/application/<int:application_id>/feature/new', methods=['GET','POST'])
def createFeature(application_id):


@app.route('/application/<int:application_id>/feature/<int:feature_id>/edit', methods=['GET','POST'])
def editFeature(application_id, feature_id):


@app.route('/application/<int:application_id>/feature/<int:feature_id>/delete', methods=['GET','POST'])
def deleteFeature(application_id, feature_id):


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
